"""Convert course datasets to parquet format.
   Run: python -m scripts.import_data
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import duckdb

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

BI_TO_AI = Path(r"C:\Users\kerry\repos\bi-to-ai\files\data")

# 1. Superstore CSV -> parquet (fix non-UTF8 bytes first)
print("Converting superstore.csv ...")
src = BI_TO_AI / "superstore.csv"
clean = DATA_DIR / "_superstore_clean.csv"
with open(src, "rb") as f:
    raw = f.read()
# Replace all non-ASCII bytes with spaces
raw = bytes(b if b < 128 else 0x20 for b in raw)
with open(clean, "wb") as f:
    f.write(raw)

con = duckdb.connect()
con.execute(f"""
    COPY (SELECT * FROM read_csv_auto('{clean}'))
    TO '{DATA_DIR / "superstore.parquet"}' (FORMAT PARQUET)
""")
clean.unlink()
rows = con.execute(f"SELECT COUNT(*) FROM read_parquet('{DATA_DIR / 'superstore.parquet'}')").fetchone()[0]
print(f"  -> {rows} rows")

# 2. Employee attrition CSV -> parquet
print("Converting employee-attrition.csv ...")
con.execute(f"""
    COPY (SELECT * FROM read_csv_auto('{BI_TO_AI / "employee-attrition.csv"}'))
    TO '{DATA_DIR / "employee_attrition.parquet"}' (FORMAT PARQUET)
""")
rows = con.execute(f"SELECT COUNT(*) FROM read_parquet('{DATA_DIR / 'employee_attrition.parquet'}')").fetchone()[0]
print(f"  -> {rows} rows")

# 3. Chinook SQLite -> individual parquet tables
print("Converting chinook.db ...")
chinook_dir = DATA_DIR / "chinook"
chinook_dir.mkdir(exist_ok=True)
chinook_path = BI_TO_AI / "chinook.db"

con.execute(f"ATTACH '{chinook_path}' AS chinook (TYPE SQLITE)")
tables = con.execute("SELECT table_name FROM information_schema.tables WHERE table_catalog='chinook'").fetchall()

for (table_name,) in tables:
    out_path = chinook_dir / f"{table_name.lower()}.parquet"
    con.execute(f"""
        COPY (SELECT * FROM chinook.{table_name})
        TO '{out_path}' (FORMAT PARQUET)
    """)
    rows = con.execute(f"SELECT COUNT(*) FROM read_parquet('{out_path}')").fetchone()[0]
    print(f"  {table_name} -> {rows} rows")

con.close()
print("\nDone. All parquet files in:", DATA_DIR.resolve())
