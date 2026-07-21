"""
AuthService      → registration, login, JWT

UserService      → profile, update account, deactivate account. 
(Get a user profile
Update a user profile
Deactivate an account
Reactivate an account, if allowed
Check whether a user exists)

CategoryService  → category rules

ExpenseService   → expense rules

ReportService    → weekly/monthly calculations

"""

from sqlalchemy.orm import Session

from app.schemas import user
from app.models import User

class UserService:
    def __init__(self, session: Session):
        self._db = session