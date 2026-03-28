"""Bulk-create student accounts from a CSV file.
   CSV format: email,name,password
   Run: python -m scripts.seed_users students.csv
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.database.user_db import init_db, create_user, get_user_by_email
from app.auth.dependencies import hash_password


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m scripts.seed_users <csv_file>")
        return

    init_db()
    csv_path = Path(sys.argv[1])
    if not csv_path.exists():
        print(f"File not found: {csv_path}")
        return

    created = 0
    skipped = 0
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            email = row["email"].strip()
            name = row.get("name", "").strip() or email
            password = row.get("password", "").strip() or "changeme"

            if get_user_by_email(email):
                print(f"  SKIP (exists): {email}")
                skipped += 1
                continue

            create_user(
                email=email,
                password_hash=hash_password(password),
                name=name,
            )
            print(f"  CREATED: {email}")
            created += 1

    print(f"\nDone. Created: {created}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
