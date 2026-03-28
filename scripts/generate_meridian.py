"""Generate Meridian Corp multi-division, multi-system enterprise data.
10 systems, 41 tables, realistic cross-system friction.
Run: python -m scripts.generate_meridian
"""
import os
import random
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import duckdb
from faker import Faker

fake = Faker()
Faker.seed(42)
np.random.seed(42)
random.seed(42)

BASE_DIR = Path("data/meridian")
DATE_START = date(2023, 1, 1)
DATE_END = date(2025, 12, 31)

REGIONS_INDUSTRIAL = ["Northeast", "Midwest"]
REGIONS_ENERGY = ["West", "Gulf Coast"]
PRODUCTS_INDUSTRIAL = ["Fasteners", "Tools", "Electrical"]
PRODUCTS_ENERGY = ["Safety Equipment", "HVAC", "Electrical"]
PRODUCTS_SAFETY = ["Safety Equipment"]


def random_date(start=DATE_START, end=DATE_END):
    return start + timedelta(days=random.randint(0, (end - start).days))


def to_parquet(df, system, table_name):
    out_dir = BASE_DIR / system
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{table_name}.parquet"
    con = duckdb.connect()
    con.execute(f"COPY (SELECT * FROM df) TO '{str(path).replace(chr(92), '/')}' (FORMAT PARQUET)")
    con.close()
    print(f"  {system}/{table_name}: {len(df)} rows")


# ============================================================
# SHARED FOUNDATION: Customers that appear across divisions
# ============================================================
print("=== Building shared foundations ===")

# ~25 companies that appear in multiple divisions, with different names
MULTI_DIV_CUSTOMERS = [
    {"canonical": "General Electric", "salesforce": "General Electric", "legacy_crm": "GE Industrial Solutions", "hubspot": "GE Safety Division", "zendesk": "General Electric"},
    {"canonical": "Caterpillar", "salesforce": "Caterpillar Inc.", "legacy_crm": "CAT Energy Services", "hubspot": None, "zendesk": "Caterpillar"},
    {"canonical": "3M", "salesforce": "3M Company", "legacy_crm": "3M Energy Products", "hubspot": "3M Safety Solutions", "zendesk": "3M"},
    {"canonical": "Honeywell", "salesforce": "Honeywell International", "legacy_crm": "Honeywell Process Solutions", "hubspot": "Honeywell Safety Products", "zendesk": "Honeywell"},
    {"canonical": "Emerson Electric", "salesforce": "Emerson Electric Co.", "legacy_crm": "Emerson Process Mgmt", "hubspot": None, "zendesk": "Emerson Electric"},
    {"canonical": "Parker Hannifin", "salesforce": "Parker Hannifin Corp", "legacy_crm": "Parker Energy Division", "hubspot": "Parker Safety Systems", "zendesk": "Parker Hannifin"},
    {"canonical": "Eaton Corporation", "salesforce": "Eaton Corporation", "legacy_crm": "Eaton Electrical", "hubspot": "Eaton Safety", "zendesk": "Eaton"},
    {"canonical": "Illinois Tool Works", "salesforce": "Illinois Tool Works", "legacy_crm": "ITW Energy Group", "hubspot": None, "zendesk": "ITW"},
    {"canonical": "Danaher", "salesforce": "Danaher Corporation", "legacy_crm": "Danaher Instruments", "hubspot": "Danaher Safety", "zendesk": "Danaher"},
    {"canonical": "Rockwell Automation", "salesforce": "Rockwell Automation", "legacy_crm": "Rockwell Collins Energy", "hubspot": None, "zendesk": "Rockwell Automation"},
    {"canonical": "Dover Corporation", "salesforce": "Dover Corporation", "legacy_crm": "Dover Energy", "hubspot": "Dover Safety", "zendesk": "Dover Corp"},
    {"canonical": "Hubbell", "salesforce": "Hubbell Incorporated", "legacy_crm": "Hubbell Power Systems", "hubspot": None, "zendesk": "Hubbell"},
    {"canonical": "Ametek", "salesforce": "Ametek Inc.", "legacy_crm": "Ametek Process Instruments", "hubspot": "Ametek Safety Analytics", "zendesk": "Ametek"},
    {"canonical": "Roper Technologies", "salesforce": "Roper Technologies", "legacy_crm": "Roper Pump & Energy", "hubspot": None, "zendesk": "Roper Technologies"},
    {"canonical": "Fortive", "salesforce": "Fortive Corporation", "legacy_crm": "Fortive Field Solutions", "hubspot": "Fortive Safety Tech", "zendesk": "Fortive"},
    {"canonical": "Nordson", "salesforce": "Nordson Corporation", "legacy_crm": "Nordson Energy Adhesives", "hubspot": None, "zendesk": "Nordson"},
    {"canonical": "Watts Water", "salesforce": "Watts Water Technologies", "legacy_crm": "Watts Energy Systems", "hubspot": "Watts Safety Valves", "zendesk": "Watts Water"},
    {"canonical": "Rexnord", "salesforce": "Rexnord Corporation", "legacy_crm": "Rexnord Process Energy", "hubspot": None, "zendesk": "Rexnord"},
    {"canonical": "Graco", "salesforce": "Graco Inc.", "legacy_crm": "Graco Fluid Systems", "hubspot": "Graco Safety Equipment", "zendesk": "Graco"},
    {"canonical": "Kennametal", "salesforce": "Kennametal Inc.", "legacy_crm": "Kennametal Energy Tooling", "hubspot": None, "zendesk": "Kennametal"},
    {"canonical": "Lincoln Electric", "salesforce": "Lincoln Electric Holdings", "legacy_crm": "Lincoln Electric Welding", "hubspot": "Lincoln Safety Products", "zendesk": "Lincoln Electric"},
    {"canonical": "Snap-on", "salesforce": "Snap-on Incorporated", "legacy_crm": None, "hubspot": "Snap-on Safety Tools", "zendesk": "Snap-on"},
    {"canonical": "Stanley Black & Decker", "salesforce": "Stanley Black & Decker", "legacy_crm": "SBD Energy Tools", "hubspot": "SBD Safety Division", "zendesk": "Stanley Black & Decker"},
    {"canonical": "Pentair", "salesforce": "Pentair plc", "legacy_crm": "Pentair Thermal Management", "hubspot": None, "zendesk": "Pentair"},
    {"canonical": "Xylem", "salesforce": "Xylem Inc.", "legacy_crm": "Xylem Water Solutions", "hubspot": "Xylem Safety Systems", "zendesk": "Xylem"},
]

INDUSTRIES = ["Manufacturing", "Construction", "Energy", "Utilities", "Mining", "Transportation"]
SEGMENTS = ["Enterprise", "Mid-Market", "Small Business"]


# ============================================================
# WORKDAY (Corporate HR) — generate first, others reference this
# ============================================================
print("\n=== Workday (Corporate HR) ===")

DIVISIONS = ["Industrial", "Energy", "Safety", "Corporate"]
DIV_HEADCOUNT = {"Industrial": 350, "Energy": 250, "Safety": 120, "Corporate": 80}
DEPTS = ["Sales", "Operations", "Warehouse", "Finance", "HR", "Marketing", "Executive", "Engineering", "Support"]

titles_by_dept = {
    "Sales": ["VP Sales", "Regional Sales Director", "Account Executive", "Sales Development Rep"],
    "Operations": ["VP Operations", "Operations Manager", "Supply Chain Analyst", "Logistics Coordinator"],
    "Warehouse": ["Warehouse Manager", "Warehouse Associate", "Shipping Clerk", "Inventory Specialist"],
    "Finance": ["CFO", "Controller", "Senior Accountant", "Staff Accountant", "Financial Analyst"],
    "HR": ["VP HR", "HR Manager", "HR Generalist", "Recruiter"],
    "Marketing": ["VP Marketing", "Marketing Manager", "Content Specialist", "Digital Analyst"],
    "Executive": ["CEO", "COO", "CIO", "General Counsel"],
    "Engineering": ["VP Engineering", "Senior Engineer", "Engineer", "Technician"],
    "Support": ["Support Manager", "Support Specialist", "Technical Support Rep"],
}

salary_by_level = {1: (35000, 50000), 2: (50000, 80000), 3: (75000, 120000),
                   4: (100000, 160000), 5: (140000, 250000), 6: (200000, 350000)}

level_prefixes = {"CEO": 6, "CFO": 6, "COO": 6, "CIO": 6, "VP": 5, "General": 5,
                  "Director": 4, "Controller": 4, "Regional": 4, "Senior": 3, "Manager": 3}

def get_level(title):
    for p, l in level_prefixes.items():
        if title.startswith(p):
            return l
    return 2

workers = []
system_id_rows = []
worker_id_counter = 1

# Track sales reps per division for CRM linking
sales_reps_by_div = {"Industrial": [], "Energy": [], "Safety": []}

for div, target_hc in DIV_HEADCOUNT.items():
    # Distribute across departments
    if div == "Corporate":
        dept_dist = {"Finance": 25, "HR": 20, "Executive": 10, "Marketing": 15, "Support": 10}
    elif div == "Safety":
        dept_dist = {"Sales": 40, "Operations": 30, "Warehouse": 20, "Finance": 10, "Support": 10, "Marketing": 10}
    else:
        dept_dist = {"Sales": int(target_hc * 0.2), "Operations": int(target_hc * 0.25),
                     "Warehouse": int(target_hc * 0.25), "Finance": int(target_hc * 0.08),
                     "Engineering": int(target_hc * 0.1), "Support": int(target_hc * 0.07),
                     "Marketing": int(target_hc * 0.05)}

    for dept, count in dept_dist.items():
        titles = titles_by_dept.get(dept, ["Specialist", "Coordinator", "Analyst"])
        for i in range(count):
            wid = f"WD-{worker_id_counter:04d}"
            worker_id_counter += 1
            title = titles[0] if i == 0 else random.choice(titles[1:] if len(titles) > 1 else titles)
            level = get_level(title)
            hire = random_date(date(2010, 1, 1), date(2025, 6, 1))
            termed = random.random() < 0.12
            term_date = random_date(max(hire + timedelta(days=90), DATE_START), DATE_END) if termed else None
            status = "Terminated" if termed else "Active"

            if div == "Industrial":
                loc = random.choice(["Cleveland", "Chicago", "Detroit", "Pittsburgh", "Indianapolis"])
            elif div == "Energy":
                loc = random.choice(["Houston", "Denver", "Phoenix", "Dallas", "Tulsa"])
            elif div == "Safety":
                loc = random.choice(["Atlanta", "Nashville", "Charlotte", "Tampa", "Raleigh"])
            else:
                loc = "New York HQ"

            workers.append({
                "worker_id": wid, "first_name": fake.first_name(), "last_name": fake.last_name(),
                "email": f"{fake.user_name()}@meridian-corp.com",
                "hire_date": hire, "termination_date": term_date,
                "division": div, "department": dept, "job_title": title,
                "job_level": level, "manager_id": None, "location": loc, "status": status,
            })

            # Track sales reps for CRM system_ids
            if dept == "Sales" and title == "Account Executive" and status == "Active" and div in sales_reps_by_div:
                sales_reps_by_div[div].append(wid)

to_parquet(pd.DataFrame(workers), "workday", "wd_workers")

# Compensation
comp_rows = []
cid = 1
for w in workers:
    for yr in [2023, 2024, 2025]:
        eff = date(yr, 1, 1)
        if w["hire_date"] > eff or (w["termination_date"] and w["termination_date"] < eff):
            continue
        low, high = salary_by_level[w["job_level"]]
        base = round(random.uniform(low, high) * (1 + 0.03 * (yr - 2023)), -2)
        bonus_tgt = round(random.uniform(0.05, 0.15 + w["job_level"] * 0.05), 2) if w["job_level"] >= 3 else 0.0
        bonus_act = round(base * bonus_tgt * random.uniform(0.5, 1.3), 2)
        comp_rows.append({
            "comp_id": cid, "worker_id": w["worker_id"], "effective_date": eff,
            "base_pay": round(base, 2), "bonus_target_pct": bonus_tgt, "bonus_actual": bonus_act,
        })
        cid += 1
to_parquet(pd.DataFrame(comp_rows), "workday", "wd_compensation")

# Reviews
rev_rows = []
rid = 1
for w in workers:
    for yr in [2023, 2024, 2025]:
        if w["hire_date"] > date(yr, 6, 1) or (w["termination_date"] and w["termination_date"] < date(yr, 1, 1)):
            continue
        rev_rows.append({
            "review_id": rid, "worker_id": w["worker_id"], "review_period": f"FY{yr}",
            "reviewer_id": w["manager_id"],
            "rating": random.choices([1, 2, 3, 4, 5], weights=[5, 10, 40, 35, 10])[0],
            "goals_pct": round(random.uniform(0.4, 1.2), 2),
        })
        rid += 1
to_parquet(pd.DataFrame(rev_rows), "workday", "wd_reviews")

# Headcount monthly
hc_rows = []
for yr in [2023, 2024, 2025]:
    for mo in range(1, 13):
        for div in DIVISIONS:
            for dept in DEPTS:
                base = DIV_HEADCOUNT[div] // 5
                if base < 2:
                    continue
                hc_rows.append({
                    "snapshot_date": date(yr, mo, 1), "division": div, "department": dept,
                    "location": "Various", "headcount": base + random.randint(-2, 3),
                    "open_reqs": random.randint(0, 3),
                })
to_parquet(pd.DataFrame(hc_rows), "workday", "wd_headcount")

# System IDs — map workers to CRM IDs (generated below)
# We'll populate this after generating CRMs
sf_owner_ids = {}
lcrm_rep_codes = {}
hs_owner_ids = {}

for wid in sales_reps_by_div["Industrial"]:
    sf_id = f"005{fake.bothify('??########').upper()}"
    sf_owner_ids[wid] = sf_id
    system_id_rows.append({"worker_id": wid, "system_name": "salesforce", "external_id": sf_id})

for wid in sales_reps_by_div["Energy"]:
    rep_code = f"{fake.last_name()[:2].upper()}{random.randint(100, 999)}"
    lcrm_rep_codes[wid] = rep_code
    system_id_rows.append({"worker_id": wid, "system_name": "legacy_crm", "external_id": rep_code})

for wid in sales_reps_by_div["Safety"]:
    hs_id = str(random.randint(100000, 999999))
    hs_owner_ids[wid] = hs_id
    system_id_rows.append({"worker_id": wid, "system_name": "hubspot", "external_id": hs_id})

to_parquet(pd.DataFrame(system_id_rows), "workday", "wd_system_ids")


# ============================================================
# SALESFORCE (Meridian Industrial CRM) — CamelCase
# ============================================================
print("\n=== Salesforce (Industrial CRM) ===")

sf_accounts = []
for i in range(200):
    # Use multi-div customer names for first ~25
    if i < len(MULTI_DIV_CUSTOMERS):
        name = MULTI_DIV_CUSTOMERS[i]["salesforce"]
        if name is None:
            name = fake.company()
    else:
        name = fake.company()

    aid = f"001{fake.bothify('??######').upper()}"
    rep_wid = random.choice(sales_reps_by_div["Industrial"]) if sales_reps_by_div["Industrial"] else None
    owner = sf_owner_ids.get(rep_wid, "005DEFAULT")

    sf_accounts.append({
        "AccountId": aid, "AccountName": name,
        "Industry": random.choice(INDUSTRIES),
        "BillingState": random.choice(["OH", "IL", "MI", "PA", "IN", "WI", "MN"]),
        "OwnerId": owner,
        "AnnualRevenue": round(random.uniform(1e6, 500e6), -3),
        "Type": random.choice(["Customer", "Prospect", "Partner"]),
    })
to_parquet(pd.DataFrame(sf_accounts), "salesforce", "sf_accounts")
sf_account_ids = [a["AccountId"] for a in sf_accounts]

sf_contacts = []
for acc in sf_accounts:
    for j in range(random.randint(1, 3)):
        sf_contacts.append({
            "ContactId": f"003{fake.bothify('??######').upper()}",
            "AccountId": acc["AccountId"],
            "FirstName": fake.first_name(), "LastName": fake.last_name(),
            "Title": random.choice(["VP Procurement", "Plant Manager", "Buyer", "Purchasing Agent"]),
            "Email": fake.email(),
        })
to_parquet(pd.DataFrame(sf_contacts), "salesforce", "sf_contacts")

sf_opps = []
sf_stages = ["Prospecting", "Qualification", "Proposal", "Negotiation", "Closed Won", "Closed Lost"]
for i in range(600):
    acc = random.choice(sf_accounts)
    stage = random.choices(sf_stages, weights=[10, 10, 15, 10, 40, 15])[0]
    sf_opps.append({
        "OpportunityId": f"006{fake.bothify('??######').upper()}",
        "AccountId": acc["AccountId"],
        "OwnerId": acc["OwnerId"],
        "Name": f"{fake.bs().title()} - {acc['AccountName'][:20]}",
        "StageName": stage,
        "Amount": round(random.uniform(5000, 2000000), -2),
        "CloseDate": random_date(),
        "CreatedDate": random_date(DATE_START, date(2025, 6, 1)),
    })
to_parquet(pd.DataFrame(sf_opps), "salesforce", "sf_opportunities")

won_sf = [o for o in sf_opps if o["StageName"] == "Closed Won"]
sf_orders = []
sf_items = []
so_num = 1
item_num = 1
for opp in won_sf:
    oid = f"SO-IND-{so_num:05d}"
    so_num += 1
    odate = opp["CloseDate"]
    total = 0
    nlines = random.randint(1, 5)
    for _ in range(nlines):
        cat = random.choice(PRODUCTS_INDUSTRIAL)
        price = round(random.uniform(5, 5000), 2)
        qty = random.randint(1, 200)
        disc = round(random.uniform(0, 0.15), 2)
        lt = round(qty * price * (1 - disc), 2)
        total += lt
        sf_items.append({
            "OrderItemId": f"OLI-{item_num:06d}", "OrderId": oid,
            "ProductCode": f"MAT-{random.randint(10001, 10400):05d}",
            "Quantity": qty, "UnitPrice": price, "Discount": disc,
        })
        item_num += 1
    sf_orders.append({
        "OrderId": oid, "AccountId": opp["AccountId"], "OpportunityId": opp["OpportunityId"],
        "OrderDate": odate, "TotalAmount": round(total, 2),
        "Status": random.choices(["Activated", "Fulfilled", "Cancelled"], weights=[15, 80, 5])[0],
    })
to_parquet(pd.DataFrame(sf_orders), "salesforce", "sf_orders")
to_parquet(pd.DataFrame(sf_items), "salesforce", "sf_order_items")


# ============================================================
# LEGACY CRM (Meridian Energy) — snake_case, dates as VARCHAR
# ============================================================
print("\n=== Legacy CRM (Energy CRM) ===")

def date_to_str(d):
    """Convert date to MM/DD/YYYY string (the legacy system's format)."""
    return d.strftime("%m/%d/%Y")

lcrm_clients = []
for i in range(150):
    if i < len(MULTI_DIV_CUSTOMERS):
        name = MULTI_DIV_CUSTOMERS[i]["legacy_crm"]
        if name is None:
            name = fake.company()
    else:
        name = fake.company()

    rep_wid = random.choice(sales_reps_by_div["Energy"]) if sales_reps_by_div["Energy"] else None
    rep_code = lcrm_rep_codes.get(rep_wid, "XX000")

    lcrm_clients.append({
        "client_id": i + 1, "client_name": name,
        "sector": random.choice(["Oil & Gas", "Utilities", "Mining", "Petrochemical", "Renewable Energy"]),
        "state": random.choice(["TX", "CO", "AZ", "NM", "OK", "LA", "CA"]),
        "sales_rep_code": rep_code,
        "annual_rev": round(random.uniform(500000, 300e6), -3),
        "date_added": date_to_str(random_date(date(2018, 1, 1), date(2025, 1, 1))),
    })
to_parquet(pd.DataFrame(lcrm_clients), "legacy_crm", "clients")

lcrm_deals = []
deal_statuses = ["Open", "Won", "Lost", "Stalled"]
for i in range(400):
    cl = random.choice(lcrm_clients)
    status = random.choices(deal_statuses, weights=[15, 40, 30, 15])[0]
    lcrm_deals.append({
        "deal_id": i + 1, "client_id": cl["client_id"],
        "rep_code": cl["sales_rep_code"],
        "deal_name": f"{fake.bs().title()}",
        "status": status,
        "value_usd": round(random.uniform(10000, 1500000), -2),
        "expected_close": date_to_str(random_date()),
        "created": date_to_str(random_date(DATE_START, date(2025, 6, 1))),
    })
to_parquet(pd.DataFrame(lcrm_deals), "legacy_crm", "deals")

won_deals = [d for d in lcrm_deals if d["status"] == "Won"]
lcrm_orders = []
lcrm_details = []
on = 1
did = 1
for deal in won_deals[:200]:
    order_dt = random_date()
    total = 0
    nlines = random.randint(1, 4)
    for _ in range(nlines):
        price = round(random.uniform(10, 8000), 2)
        qty = random.randint(1, 100)
        disc = round(random.uniform(0, 0.12), 2)
        lt = round(qty * price * (1 - disc), 2)
        total += lt
        lcrm_details.append({
            "detail_id": did, "order_num": on,
            "item_id": f"ITEM-{random.randint(5001, 5300)}",
            "qty": qty, "price": price, "disc_pct": disc,
        })
        did += 1
    lcrm_orders.append({
        "order_num": on, "client_id": deal["client_id"], "deal_id": deal["deal_id"],
        "order_dt": date_to_str(order_dt), "ship_dt": date_to_str(order_dt + timedelta(days=random.randint(1, 7))),
        "total": round(total, 2),
    })
    on += 1

# Add recurring orders
for _ in range(300):
    cl = random.choice(lcrm_clients)
    order_dt = random_date()
    total = 0
    nlines = random.randint(1, 3)
    for _ in range(nlines):
        price = round(random.uniform(10, 5000), 2)
        qty = random.randint(1, 50)
        disc = round(random.uniform(0, 0.10), 2)
        lt = round(qty * price * (1 - disc), 2)
        total += lt
        lcrm_details.append({
            "detail_id": did, "order_num": on,
            "item_id": f"ITEM-{random.randint(5001, 5300)}",
            "qty": qty, "price": price, "disc_pct": disc,
        })
        did += 1
    lcrm_orders.append({
        "order_num": on, "client_id": cl["client_id"], "deal_id": None,
        "order_dt": date_to_str(order_dt), "ship_dt": date_to_str(order_dt + timedelta(days=random.randint(1, 7))),
        "total": round(total, 2),
    })
    on += 1

to_parquet(pd.DataFrame(lcrm_orders), "legacy_crm", "client_orders")
to_parquet(pd.DataFrame(lcrm_details), "legacy_crm", "order_details")


# ============================================================
# HUBSPOT (Meridian Safety CRM) — HubSpot conventions
# ============================================================
print("\n=== HubSpot (Safety CRM) ===")

hs_companies = []
for i in range(100):
    if i < len(MULTI_DIV_CUSTOMERS):
        name = MULTI_DIV_CUSTOMERS[i]["hubspot"]
        if name is None:
            name = fake.company()
    else:
        name = fake.company()

    rep_wid = random.choice(sales_reps_by_div["Safety"]) if sales_reps_by_div["Safety"] else None
    owner = hs_owner_ids.get(rep_wid, "000000")

    hs_companies.append({
        "company_id": i + 1, "name": name,
        "industry": random.choice(INDUSTRIES),
        "lifecycle_stage": random.choice(["customer", "customer", "customer", "opportunity", "lead"]),
        "owner_id": owner,
        "annual_revenue": round(random.uniform(500000, 200e6), -3),
        "create_date": random_date(date(2020, 1, 1), date(2025, 6, 1)),
    })
to_parquet(pd.DataFrame(hs_companies), "hubspot", "hs_companies")

hs_deals_list = []
hs_stages = ["appointmentscheduled", "qualifiedtobuy", "presentationscheduled",
             "decisionmakerboughtin", "contractsent", "closedwon", "closedlost"]
for i in range(250):
    comp = random.choice(hs_companies)
    stage = random.choices(hs_stages, weights=[8, 10, 12, 10, 10, 38, 12])[0]
    hs_deals_list.append({
        "deal_id": i + 1, "company_id": comp["company_id"],
        "owner_id": comp["owner_id"],
        "dealname": f"{fake.bs().title()}",
        "dealstage": stage,
        "amount": round(random.uniform(5000, 500000), -2),
        "closedate": random_date(),
        "createdate": random_date(DATE_START, date(2025, 6, 1)),
    })
to_parquet(pd.DataFrame(hs_deals_list), "hubspot", "hs_deals")

hs_line_items = []
li_id = 1
for deal in hs_deals_list:
    if deal["dealstage"] != "closedwon":
        continue
    for _ in range(random.randint(1, 4)):
        hs_line_items.append({
            "line_item_id": li_id, "deal_id": deal["deal_id"],
            "product_id": f"HS-PROD-{random.randint(1, 80)}",
            "quantity": random.randint(1, 100),
            "price": round(random.uniform(20, 3000), 2),
            "discount": round(random.uniform(0, 0.10), 2),
        })
        li_id += 1
to_parquet(pd.DataFrame(hs_line_items), "hubspot", "hs_line_items")


# ============================================================
# NETSUITE INDUSTRIAL (Finance) — 5-digit account codes
# ============================================================
print("\n=== NetSuite Industrial (Finance) ===")

ns_accounts = [
    {"account_code": "40000", "account_name": "Product Revenue", "account_type": "Revenue", "department": "Sales"},
    {"account_code": "40100", "account_name": "Service Revenue", "account_type": "Revenue", "department": "Sales"},
    {"account_code": "50000", "account_name": "Cost of Goods Sold", "account_type": "COGS", "department": "Operations"},
    {"account_code": "50100", "account_name": "Freight & Shipping", "account_type": "COGS", "department": "Operations"},
    {"account_code": "60000", "account_name": "Salaries & Wages", "account_type": "OpEx", "department": "HR"},
    {"account_code": "60100", "account_name": "Benefits", "account_type": "OpEx", "department": "HR"},
    {"account_code": "60200", "account_name": "Commissions", "account_type": "OpEx", "department": "Sales"},
    {"account_code": "60300", "account_name": "Rent & Facilities", "account_type": "OpEx", "department": "Operations"},
    {"account_code": "60400", "account_name": "Technology", "account_type": "OpEx", "department": "Finance"},
    {"account_code": "60500", "account_name": "Marketing", "account_type": "OpEx", "department": "Marketing"},
]
to_parquet(pd.DataFrame(ns_accounts), "netsuite_industrial", "ns_accounts")

ns_trans = []
tid = 1
for so in sf_orders:
    if so["Status"] == "Cancelled":
        continue
    # Invoice
    ns_trans.append({
        "transaction_id": tid, "entity_id": so["AccountId"],
        "tran_date": so["OrderDate"], "tran_type": "Invoice",
        "amount": so["TotalAmount"], "status": "Paid" if random.random() > 0.1 else "Open",
        "account_code": "40000",
    })
    tid += 1
    # COGS
    ns_trans.append({
        "transaction_id": tid, "entity_id": so["AccountId"],
        "tran_date": so["OrderDate"], "tran_type": "Journal",
        "amount": round(so["TotalAmount"] * random.uniform(0.55, 0.70), 2), "status": "Posted",
        "account_code": "50000",
    })
    tid += 1
to_parquet(pd.DataFrame(ns_trans), "netsuite_industrial", "ns_transactions")

ns_budget = []
bid = 1
for yr in [2023, 2024, 2025]:
    growth = 1.0 + 0.08 * (yr - 2023)
    for mo in range(1, 13):
        for ac in ["40000", "50000", "60000"]:
            base = 250e6 / 12 * growth
            mult = {"40000": 1.0, "50000": 0.60, "60000": 0.18}[ac]
            ns_budget.append({
                "budget_id": bid, "fiscal_year": yr, "fiscal_month": mo,
                "account_code": ac, "department": "All",
                "amount": round(base * mult * random.uniform(0.95, 1.05), 2),
            })
            bid += 1
to_parquet(pd.DataFrame(ns_budget), "netsuite_industrial", "ns_budget")


# ============================================================
# QUICKBOOKS ENERGY (Finance) — 4-digit account codes
# ============================================================
print("\n=== QuickBooks Energy (Finance) ===")

qb_accounts = [
    {"acct_num": "4000", "acct_name": "Sales Revenue", "acct_type": "Income", "detail_type": "Sales"},
    {"acct_num": "4010", "acct_name": "Service Income", "acct_type": "Income", "detail_type": "Service"},
    {"acct_num": "5000", "acct_name": "Cost of Sales", "acct_type": "COGS", "detail_type": "Supplies"},
    {"acct_num": "5010", "acct_name": "Shipping Costs", "acct_type": "COGS", "detail_type": "Freight"},
    {"acct_num": "6000", "acct_name": "Payroll Expenses", "acct_type": "Expense", "detail_type": "Payroll"},
    {"acct_num": "6010", "acct_name": "Rent Expense", "acct_type": "Expense", "detail_type": "Occupancy"},
    {"acct_num": "6020", "acct_name": "Utilities", "acct_type": "Expense", "detail_type": "Utilities"},
    {"acct_num": "6030", "acct_name": "Insurance", "acct_type": "Expense", "detail_type": "Insurance"},
]
to_parquet(pd.DataFrame(qb_accounts), "quickbooks_energy", "qb_accounts")

qb_invoices = []
for order in lcrm_orders:
    qb_invoices.append({
        "invoice_num": f"INV-E-{order['order_num']:05d}",
        "customer_ref": order["client_id"],
        "invoice_date": random_date(),  # proper date type in QB
        "due_date": random_date(),
        "total": order["total"],
        "balance_due": 0 if random.random() > 0.12 else order["total"],
    })
to_parquet(pd.DataFrame(qb_invoices), "quickbooks_energy", "qb_invoices")

qb_payments = []
pid = 1
for inv in qb_invoices:
    if inv["balance_due"] == 0:
        qb_payments.append({
            "payment_id": pid, "invoice_num": inv["invoice_num"],
            "payment_date": inv["invoice_date"] + timedelta(days=random.randint(15, 60)),
            "amount": inv["total"],
            "method": random.choice(["ACH", "Wire", "Check", "Credit Card"]),
        })
        pid += 1
to_parquet(pd.DataFrame(qb_payments), "quickbooks_energy", "qb_payments")

qb_journal = []
jid = 1
for yr in [2023, 2024, 2025]:
    for mo in range(1, 13):
        rev = round(150e6 / 12 * random.uniform(0.85, 1.15), 2)
        for acct, mult in [("4000", rev), ("5000", round(rev * 0.62, 2)), ("6000", round(rev * 0.16, 2))]:
            qb_journal.append({
                "journal_id": jid, "txn_date": date(yr, mo, 15),
                "acct_num": acct,
                "debit": mult if acct != "4000" else 0,
                "credit": mult if acct == "4000" else 0,
                "memo": f"Monthly {acct} entry",
            })
            jid += 1
to_parquet(pd.DataFrame(qb_journal), "quickbooks_energy", "qb_journal")


# ============================================================
# NETSUITE CORPORATE (Consolidation)
# ============================================================
print("\n=== NetSuite Corporate (Consolidation) ===")

ns_acct_mapping = []
# Map Industrial 5-digit to corporate
for code in ["40000", "50000", "60000"]:
    corp_code = {"40000": "REV-001", "50000": "COGS-001", "60000": "OPEX-001"}[code]
    ns_acct_mapping.append({"division_account_code": code, "corporate_account_code": corp_code, "division": "Industrial"})
# Map Energy 4-digit to corporate
for code in ["4000", "5000", "6000"]:
    corp_code = {"4000": "REV-001", "5000": "COGS-001", "6000": "OPEX-001"}[code]
    ns_acct_mapping.append({"division_account_code": code, "corporate_account_code": corp_code, "division": "Energy"})
to_parquet(pd.DataFrame(ns_acct_mapping), "netsuite_corporate", "ns_acct_mapping")

ns_corp_budget = []
ns_corp_actuals = []
bid = 1
aid = 1
for yr in [2023, 2024, 2025]:
    growth = 1.0 + 0.08 * (yr - 2023)
    for mo in range(1, 13):
        for div, rev_base in [("Industrial", 250e6), ("Energy", 150e6), ("Safety", 100e6)]:
            monthly = rev_base / 12 * growth
            ns_corp_budget.append({"budget_id": bid, "division": div, "fiscal_year": yr, "fiscal_month": mo,
                                   "account_code": "REV-001", "amount": round(monthly, 2)})
            bid += 1
            ns_corp_actuals.append({"actual_id": aid, "division": div, "fiscal_year": yr, "fiscal_month": mo,
                                    "account_code": "REV-001", "amount": round(monthly * random.uniform(0.88, 1.12), 2)})
            aid += 1
to_parquet(pd.DataFrame(ns_corp_budget), "netsuite_corporate", "ns_corp_budget")
to_parquet(pd.DataFrame(ns_corp_actuals), "netsuite_corporate", "ns_corp_actuals")


# ============================================================
# SAP (Meridian Industrial Operations)
# ============================================================
print("\n=== SAP (Industrial Operations) ===")

sap_materials = []
for i in range(400):
    cat = random.choice(PRODUCTS_INDUSTRIAL)
    cost = round(random.uniform(0.5, 2000), 2)
    sap_materials.append({
        "material_number": f"MAT-{10001 + i:05d}",
        "description": f"{fake.word().title()} {cat} Component {fake.bothify('##?').upper()}",
        "material_group": cat, "standard_price": cost,
        "list_price": round(cost / (1 - random.uniform(0.15, 0.45)), 2),
    })
to_parquet(pd.DataFrame(sap_materials), "sap", "sap_materials")

sap_vendors = []
# One vendor with chronic late deliveries
for i in range(40):
    is_bad = (i == 0)
    sap_vendors.append({
        "vendor_code": f"V-{1000 + i}",
        "vendor_name": fake.company() if not is_bad else "Pacific Rim Components Ltd.",
        "country": "China" if is_bad else random.choice(["US", "US", "Mexico", "Germany", "Canada"]),
        "payment_terms": random.choice(["Net 30", "Net 45", "Net 60"]),
        "quality_score": round(random.uniform(2.0, 3.5) if is_bad else random.uniform(3.5, 5.0), 1),
    })
to_parquet(pd.DataFrame(sap_vendors), "sap", "sap_vendors")

sap_pos = []
sap_po_items = []
po_num = 1
pi_num = 1
for i in range(1500):
    vc = sap_vendors[0]["vendor_code"] if random.random() < 0.08 else random.choice(sap_vendors)["vendor_code"]
    po_date = random_date()
    del_date = po_date + timedelta(days=random.randint(7, 60))
    is_bad_vendor = (vc == "V-1000")
    late = is_bad_vendor and random.random() < 0.35
    actual = del_date + timedelta(days=random.randint(5, 25)) if late else del_date - timedelta(days=random.randint(0, 3))
    if actual > DATE_END:
        actual = None
    total = 0
    for _ in range(random.randint(1, 4)):
        mat = random.choice(sap_materials)
        qty = random.randint(10, 500)
        price = round(mat["standard_price"] * random.uniform(0.9, 1.1), 2)
        lt = round(qty * price, 2)
        total += lt
        sap_po_items.append({
            "item_number": pi_num, "po_number": f"PO-IND-{po_num:05d}",
            "material_number": mat["material_number"], "quantity": qty, "net_price": price,
        })
        pi_num += 1
    sap_pos.append({
        "po_number": f"PO-IND-{po_num:05d}", "vendor_code": vc,
        "po_date": po_date, "delivery_date": del_date,
        "actual_delivery": actual,
        "total_value": round(total, 2),
        "status": "Received" if actual else "Open",
    })
    po_num += 1
to_parquet(pd.DataFrame(sap_pos), "sap", "sap_purchase_orders")
to_parquet(pd.DataFrame(sap_po_items), "sap", "sap_po_items")

sap_inventory = []
plants = ["Cleveland Plant", "Chicago DC", "Detroit Warehouse"]
for mat in sap_materials:
    for plant in plants:
        sap_inventory.append({
            "material_number": mat["material_number"], "plant": plant,
            "unrestricted_qty": random.randint(0, 5000),
            "reorder_point": random.randint(50, 500),
        })
to_parquet(pd.DataFrame(sap_inventory), "sap", "sap_inventory")

sap_deliveries = []
dn = 1
for so in sf_orders:
    if so["Status"] == "Cancelled":
        continue
    ship = so["OrderDate"] + timedelta(days=random.randint(1, 5))
    promised = ship + timedelta(days=random.randint(3, 10))
    late = random.random() < 0.08
    actual = promised + timedelta(days=random.randint(3, 14)) if late else promised - timedelta(days=random.randint(0, 2))
    sap_deliveries.append({
        "delivery_number": f"DN-{dn:06d}", "sales_order": so["OrderId"],
        "ship_date": ship, "actual_delivery": actual,
        "carrier": random.choice(["UPS", "FedEx", "Freight Co", "Internal Fleet"]),
        "on_time": not late,
    })
    dn += 1
to_parquet(pd.DataFrame(sap_deliveries), "sap", "sap_deliveries")


# ============================================================
# ORACLE SCM (Meridian Energy Operations)
# ============================================================
print("\n=== Oracle SCM (Energy Operations) ===")

ora_items = []
for i in range(300):
    cat = random.choice(PRODUCTS_ENERGY)
    cost = round(random.uniform(1, 3000), 2)
    ora_items.append({
        "item_id": f"ITEM-{5001 + i}",
        "item_description": f"{fake.word().title()} {cat} Unit {fake.bothify('##?').upper()}",
        "category": cat,
        "subcategory": f"{cat} - {random.choice(['Standard', 'Premium', 'Heavy Duty', 'Compact'])}",
        "unit_cost": cost,
        "unit_price": round(cost / (1 - random.uniform(0.15, 0.40)), 2),
    })
to_parquet(pd.DataFrame(ora_items), "oracle_scm", "ora_items")

ora_suppliers = []
for i in range(30):
    ora_suppliers.append({
        "supplier_num": f"SUP-{2001 + i}",
        "supplier_name": fake.company(),
        "country": random.choice(["US", "US", "Mexico", "China", "Canada"]),
        "lead_time": random.randint(5, 75),
        "performance_rating": round(random.uniform(2.5, 5.0), 1),
    })
to_parquet(pd.DataFrame(ora_suppliers), "oracle_scm", "ora_suppliers")

ora_pos = []
ora_po_lines = []
opn = 1
opl = 1
for i in range(800):
    sup = random.choice(ora_suppliers)
    od = random_date()
    promise = od + timedelta(days=random.randint(7, 60))
    received = promise + timedelta(days=random.randint(-3, 10))
    if received > DATE_END:
        received = None
    total = 0
    for _ in range(random.randint(1, 4)):
        item = random.choice(ora_items)
        qty = random.randint(5, 300)
        uc = round(item["unit_cost"] * random.uniform(0.9, 1.1), 2)
        lt = round(qty * uc, 2)
        total += lt
        ora_po_lines.append({
            "line_id": opl, "po_id": f"PO-ENR-{opn:05d}",
            "item_id": item["item_id"], "quantity": qty, "unit_cost": uc,
        })
        opl += 1
    ora_pos.append({
        "po_id": f"PO-ENR-{opn:05d}", "supplier_num": sup["supplier_num"],
        "order_date": od, "promise_date": promise,
        "received_date": received,
        "total": round(total, 2),
        "status": "Received" if received else "Open",
    })
    opn += 1
to_parquet(pd.DataFrame(ora_pos), "oracle_scm", "ora_purchase_orders")
to_parquet(pd.DataFrame(ora_po_lines), "oracle_scm", "ora_po_lines")

ora_shipments = []
sn = 1
for order in lcrm_orders:
    ship = random_date()
    promised = ship + timedelta(days=random.randint(3, 10))
    late = random.random() < 0.10
    delivery = promised + timedelta(days=random.randint(3, 12)) if late else promised - timedelta(days=random.randint(0, 2))
    ora_shipments.append({
        "shipment_id": f"SHIP-{sn:05d}", "order_ref": str(order["order_num"]),
        "ship_from": random.choice(["Houston DC", "Denver DC", "Phoenix Warehouse"]),
        "ship_date": ship, "delivery_date": delivery,
        "carrier": random.choice(["FedEx Freight", "XPO Logistics", "Old Dominion", "Internal"]),
        "delivery_status": "Late" if late else "On Time",
    })
    sn += 1
to_parquet(pd.DataFrame(ora_shipments), "oracle_scm", "ora_shipments")


# ============================================================
# ZENDESK (Corporate Support)
# ============================================================
print("\n=== Zendesk (Corporate Support) ===")

# Use zendesk organization names from MULTI_DIV_CUSTOMERS
zd_org_names = [c["zendesk"] for c in MULTI_DIV_CUSTOMERS if c["zendesk"]]
# Add some single-division customers
zd_org_names += [random.choice(sf_accounts)["AccountName"] for _ in range(30)]
zd_org_names += [random.choice(lcrm_clients)["client_name"] for _ in range(20)]

zd_tickets = []
zd_tags = []
zd_assignees = []
support_emails = [w["email"] for w in workers if w["department"] == "Support" and w["status"] == "Active"]

for i in range(600):
    org = random.choice(zd_org_names)
    created = random_date()
    priority = random.choices(["low", "normal", "high", "urgent"], weights=[15, 45, 30, 10])[0]
    ttype = random.choice(["delivery_issue", "product_defect", "billing", "technical_support",
                           "return_request", "order_inquiry", "warranty"])
    days_to_solve = {"low": random.randint(3, 14), "normal": random.randint(1, 7),
                     "high": random.randint(0, 3), "urgent": random.randint(0, 1)}[priority]
    solved = created + timedelta(days=days_to_solve) if random.random() < 0.85 else None
    sat = random.choices([1, 2, 3, 4, 5], weights=[5, 10, 25, 40, 20])[0] if solved else None

    zd_tickets.append({
        "ticket_id": i + 1, "requester_email": fake.email(),
        "organization": org, "created_at": created, "solved_at": solved,
        "priority": priority, "ticket_type": ttype,
        "satisfaction_rating": sat,
        "status": "closed" if solved else random.choice(["open", "pending", "hold"]),
        "subject": f"{ttype.replace('_', ' ').title()} - {org[:30]}",
    })

    # Tags: division + product category
    div_tag = random.choice(["industrial", "energy", "safety"])
    cat_tag = random.choice(["fasteners", "tools", "electrical", "safety_equipment", "hvac"])
    zd_tags.append({"ticket_id": i + 1, "tag": div_tag})
    zd_tags.append({"ticket_id": i + 1, "tag": cat_tag})
    if random.random() < 0.3:
        zd_tags.append({"ticket_id": i + 1, "tag": random.choice(["escalated", "vip", "recurring"])})

    # Assignees
    if support_emails:
        agent = random.choice(support_emails)
        zd_assignees.append({"ticket_id": i + 1, "assignee_email": agent, "assigned_at": created})
        if random.random() < 0.2:
            zd_assignees.append({"ticket_id": i + 1, "assignee_email": random.choice(support_emails),
                                 "assigned_at": created + timedelta(days=random.randint(0, 2))})

to_parquet(pd.DataFrame(zd_tickets), "zendesk", "zd_tickets")
to_parquet(pd.DataFrame(zd_tags), "zendesk", "zd_ticket_tags")
to_parquet(pd.DataFrame(zd_assignees), "zendesk", "zd_assignees")


# ============================================================
# SUMMARY
# ============================================================
print("\n=== Generation complete ===")
import glob
con = duckdb.connect()
total = 0
systems = {}
for f in sorted(glob.glob(str(BASE_DIR / "**" / "*.parquet"), recursive=True)):
    parts = Path(f).relative_to(BASE_DIR).parts
    system = parts[0]
    table = parts[1].replace(".parquet", "")
    n = con.execute(f"SELECT COUNT(*) FROM read_parquet('{f.replace(chr(92), '/')}')").fetchone()[0]
    total += n
    systems.setdefault(system, []).append((table, n))

for sys_name, tables in sorted(systems.items()):
    sys_total = sum(n for _, n in tables)
    print(f"\n  {sys_name} ({len(tables)} tables, {sys_total:,} rows):")
    for tbl, n in tables:
        print(f"    {tbl}: {n:,}")

con.close()
print(f"\n  TOTAL: {total:,} rows across {sum(len(t) for t in systems.values())} tables in {len(systems)} systems")
