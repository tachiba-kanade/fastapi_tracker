# FastAPI Beginner Project: Personal Expense Tracker API

## Project Goal

Build a REST API that allows users to register, log in, create expense categories, record expenses, and view simple spending reports.

This project is designed to help you practice real-world FastAPI development without Docker.

---

## What You Will Practice

- FastAPI routes and dependencies
- Pydantic request and response validation
- SQLAlchemy ORM
- Alembic database migrations
- JWT authentication
- Password hashing
- CRUD operations
- Filtering and pagination
- Authorization and data ownership
- Error handling
- Automated testing with Pytest
- Environment variables

---

## Recommended Technology Stack

- Python 3.11 or newer
- FastAPI
- Uvicorn
- SQLAlchemy
- Alembic
- SQLite for the first version
- Pydantic Settings
- PyJWT
- pwdlib with Argon2
- Pytest
- HTTPX

SQLite does not require a separate database installation.

---

## Main Features

### 1. User Registration

A new user should be able to create an account using:

- Full name
- Email address
- Password

Requirements:

- Email must be valid.
- Email must be unique.
- Password must be hashed before being stored.
- Password must never be returned by the API.

Suggested endpoint:

```http
POST /auth/register
```

Example request:

```json
{
  "full_name": "Sudo",
  "email": "sudo@example.com",
  "password": "StrongPassword123"
}
```

---

### 2. User Login

A registered user should be able to log in using email and password.

Suggested endpoint:

```http
POST /auth/login
```

The response should contain a JWT access token.

Example response:

```json
{
  "access_token": "jwt-token",
  "token_type": "bearer"
}
```

Protected endpoints must require:

```http
Authorization: Bearer <access_token>
```

---

### 3. User Profile

A logged-in user should be able to:

- View their profile
- Update their full name
- Delete their account

Suggested endpoints:

```http
GET    /users/me
PATCH  /users/me
DELETE /users/me
```

---

### 4. Expense Categories

Users should be able to create and manage their own categories.

Examples:

- Food
- Travel
- Rent
- Shopping
- Entertainment
- Utilities

Category fields:

```text
id
user_id
name
description
created_at
updated_at
```

Suggested endpoints:

```http
POST   /categories
GET    /categories
GET    /categories/{category_id}
PATCH  /categories/{category_id}
DELETE /categories/{category_id}
```

Business rules:

- Category name is required.
- Category names should be unique for each user.
- A user cannot access another user's categories.
- Decide how deletion works when a category contains expenses:
  - Block deletion, or
  - Move the expenses to an "Uncategorized" category.

For the first version, blocking deletion is simpler.

---

### 5. Expenses

Users should be able to create, read, update, and delete expenses.

Expense fields:

```text
id
user_id
category_id
title
description
amount
expense_date
payment_method
created_at
updated_at
```

Suggested payment methods:

```text
cash
credit_card
debit_card
bank_transfer
upi
other
```

Suggested endpoints:

```http
POST   /expenses
GET    /expenses
GET    /expenses/{expense_id}
PATCH  /expenses/{expense_id}
DELETE /expenses/{expense_id}
```

Example request:

```json
{
  "title": "Lunch",
  "description": "Lunch with team",
  "amount": 350.50,
  "category_id": 1,
  "expense_date": "2026-07-11",
  "payment_method": "upi"
}
```

Business rules:

- Amount must be greater than zero.
- Title is required.
- Expense date is required.
- Category must belong to the logged-in user.
- A user cannot access another user's expenses.
- Use a decimal type for money instead of a floating-point database type.

---

## Filtering and Pagination

The expense list endpoint should support filters.

Examples:

```http
GET /expenses?category_id=1
GET /expenses?start_date=2026-07-01&end_date=2026-07-31
GET /expenses?min_amount=100&max_amount=1000
GET /expenses?payment_method=upi
GET /expenses?page=1&page_size=20
```

Optional sorting:

```http
GET /expenses?sort_by=expense_date&sort_order=desc
```

Validation rules:

- `page` must be at least 1.
- `page_size` should have a maximum, such as 100.
- `min_amount` cannot be greater than `max_amount`.
- `start_date` cannot be after `end_date`.

---

## Reports

Create simple report endpoints for the logged-in user.

### Monthly Summary

```http
GET /reports/monthly?year=2026&month=7
```

Example response:

```json
{
  "year": 2026,
  "month": 7,
  "total_spent": 12500.75,
  "expense_count": 18
}
```

### Category Summary

```http
GET /reports/category-summary?year=2026&month=7
```

Example response:

```json
{
  "items": [
    {
      "category_id": 1,
      "category_name": "Food",
      "total_spent": 4200.50
    },
    {
      "category_id": 2,
      "category_name": "Travel",
      "total_spent": 2500.00
    }
  ]
}
```

---

## Database Tables

### users

```text
id
full_name
email
hashed_password
is_active
created_at
updated_at
```

### categories

```text
id
user_id
name
description
created_at
updated_at
```

### expenses

```text
id
user_id
category_id
title
description
amount
expense_date
payment_method
created_at
updated_at
```

Relationships:

- One user has many categories.
- One user has many expenses.
- One category has many expenses.
- Every category and expense belongs to exactly one user.

---

## Suggested Folder Structure

```text
expense-tracker/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   └── security.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── category.py
│   │   └── expense.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── auth.py
│   │   ├── category.py
│   │   └── expense.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── categories.py
│   │   ├── expenses.py
│   │   └── reports.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── category_service.py
│   │   ├── expense_service.py
│   │   └── report_service.py
│   └── dependencies/
│       ├── __init__.py
│       └── auth.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_categories.py
│   ├── test_expenses.py
│   └── test_reports.py
├── alembic/
├── .env
├── .env.example
├── .gitignore
├── alembic.ini
├── req.txt
└── README.md
```

---

## Environment Variables

Create a `.env` file:

```env
APP_NAME=Expense Tracker API
DATABASE_URL=sqlite:///./expense_tracker.db
JWT_SECRET_KEY=replace-this-with-a-long-random-secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Do not commit the real `.env` file to Git.

Create a `.env.example` file containing safe example values.

---

## Installation

### 1. Create the project folder

```bash
mkdir expense-tracker
cd expense-tracker
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r req.txt
```

### 4. Start the application

```bash
uvicorn app.main:app --reload
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Alembic Migration Commands

Initialize Alembic once:

```bash
alembic init alembic
```

Create a migration:

```bash
alembic revision --autogenerate -m "create initial tables"
```

Apply migrations:

```bash
alembic upgrade head
```

---

## Minimum API Responses

Use appropriate HTTP status codes:

```text
200 OK
201 Created
204 No Content
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
422 Unprocessable Entity
```

Use a consistent error format:

```json
{
  "detail": "Expense not found"
}
```

---

## Testing Requirements

Write tests for at least the following cases:

### Authentication

- User can register.
- Duplicate email registration is rejected.
- User can log in with correct credentials.
- Invalid credentials are rejected.
- Protected endpoints reject missing tokens.
- Protected endpoints reject invalid tokens.

### Categories

- User can create a category.
- Duplicate category name is rejected.
- User can list their categories.
- User cannot access another user's category.
- Category with expenses cannot be deleted.

### Expenses

- User can create an expense.
- Expense with zero or negative amount is rejected.
- Expense with another user's category is rejected.
- User can filter expenses by date.
- User can filter expenses by category.
- User cannot access another user's expense.
- Pagination works correctly.

### Reports

- Monthly total is calculated correctly.
- Category totals are calculated correctly.
- Reports contain only the logged-in user's data.

Run tests with:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

---

## Development Milestones

### Milestone 1: Basic Application

- Create the FastAPI application.
- Add a health endpoint.
- Configure SQLite.
- Create SQLAlchemy models.
- Configure Alembic.

Health endpoint:

```http
GET /health
```

Example response:

```json
{
  "status": "ok"
}
```

### Milestone 2: Authentication

- Register users.
- Hash passwords.
- Log users in.
- Generate JWT access tokens.
- Protect private routes.

### Milestone 3: Categories

- Add category CRUD.
- Enforce category ownership.
- Handle duplicate category names.

### Milestone 4: Expenses

- Add expense CRUD.
- Validate amount and category ownership.
- Add pagination and filters.

### Milestone 5: Reports

- Add monthly summary.
- Add category-wise summary.

### Milestone 6: Quality

- Add tests.
- Improve errors.
- Add logging.
- Complete the README.
- Add sample API requests.

---

## Completion Checklist

The project is complete when:

- [ ] Users can register and log in.
- [ ] Passwords are securely hashed.
- [ ] JWT authentication protects private routes.
- [ ] Users can manage their profile.
- [ ] Users can create and manage categories.
- [ ] Users can create and manage expenses.
- [ ] Users cannot access another user's data.
- [ ] Expense filtering and pagination work.
- [ ] Monthly and category reports work.
- [ ] Alembic migrations work.
- [ ] Automated tests cover important behavior.
- [ ] The API runs locally without Docker.
- [ ] Swagger documentation is available at `/docs`.

---

## Optional Features After the Core Version

Add these only after the main requirements are complete:

- Monthly budgets
- Recurring expenses
- CSV export
- Refresh tokens
- Password reset
- Email verification
- Multiple currencies
- Soft deletion
- PostgreSQL support
- CI pipeline with GitHub Actions


## How do i visualise this - example

Client
  │
  │ POST /expenses
  ▼
Router
  │
  │ ExpenseCreate
  ▼
Service
  │
  │ ownership checks
  ▼
Repository
  │
  │ INSERT
  ▼
PostgreSQL
  │
  │ saved Expense model
  ▼
Response schema
  │
  ▼
Client



User clicks “Add expense”
        ↓
Frontend sends POST /expenses
        ↓
FastAPI receives the request
        ↓
Pydantic validates the expense
        ↓
Service checks business rules
        ↓
Repository saves it
        ↓
PostgreSQL stores it
        ↓
FastAPI returns the saved expense



## NOTE


Every Pydantic schema is technically a Pydantic model, but in our architecture we call it a schema so we don't confuse it with SQLAlchemy database models.


python -m alembic init alembic
Alembic creates a migration environment containing alembic/env.py, alembic/versions/, and alembic.ini.