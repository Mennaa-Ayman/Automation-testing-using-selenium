# Selenium Automation Testing Suite

## Overview

Selenium-based automation testing project for testing user authentication flows including login and signup functionality Validating successful and error scenarios.

## Project Structure

```
SeleniumAutomation/
├── tests/
│   ├── test_login.py        # Login test cases (valid & invalid credentials)
│   └── test_signup.py       # Signup test cases (empty fields & invalid email)
├── Utils/
│   └── Config.py            # Configuration file (URLs, test data)
├── conftest.py              # Pytest configuration & fixtures
├── requirements.txt         # Python dependencies
├── test-case.md             # Detailed test case documentation
└── README.md                # This file
```

## Installation & Setup

**1. Install Dependencies**
```bash
pip install -r requirements.txt
```
No manual driver setup required. The project uses `webdriver-manager` to automatically download and manage the correct ChromeDriver version.

**2. Configure Test Data**
Update `Utils/Config.py` with your test credentials:
```python
BASE_URL = "https://automationexercise.com/login"
VALID_EMAIL = "your-email@example.com"
VALID_PASSWORD = "your-password"
INVALID_EMAIL = "wrong@email.com"
INVALID_PASSWORD = "wrongpassword"
```

## Running Tests

**Run All Tests**
```bash
pytest -v
```

**Run Specific Test File**
```bash
# Login tests only
pytest -v tests/test_login.py

# Signup tests only
pytest -v tests/test_signup.py
```

### Run Specific Test Case
```bash
pytest -v tests/test_login.py::test_login_valid
```

## Requirements

- Python 3.7+
- Selenium 4.0+
- pytest 8.0+
- webdriver-manager 4.0+



