"""Create an admin user. Run from the project root:
   python -m scripts.create_admin
"""
import sys
import getpass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.database.user_db import init_db, create_user, get_user_by_email
from app.auth.dependencies import hash_password


def main():
    init_db()

    email = input("Admin email: ").strip()
    if not email:
        print("Email is required.")
        return

    if get_user_by_email(email):
        print(f"User {email} already exists.")
        return

    name = input("Name: ").strip() or email
    password = getpass.getpass("Password: ")
    if len(password) < 6:
        print("Password must be at least 6 characters.")
        return

    user_id = create_user(
        email=email,
        password_hash=hash_password(password),
        name=name,
        is_admin=True,
    )
    print(f"Admin user created: {email} (id={user_id})")


if __name__ == "__main__":
    main()
