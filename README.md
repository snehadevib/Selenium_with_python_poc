# Selenium + Python Test Automation Framework — Saucedemo

A test automation framework built with **Python**, **Selenium WebDriver**, and **pytest**, using the **Page Object Model (POM)** design pattern, to test [saucedemo.com](https://www.saucedemo.com/) — a demo e-commerce application.

## Why this project

Built as a learning project and portfolio piece to demonstrate practical, industry-standard test automation skills: page object design, explicit waits, data-driven testing, fixture composition, and CI-friendly reporting.

## Tech stack

| Tool | Purpose |
|---|---|
| Python 3.14 | Language |
| Selenium WebDriver 4.x | Browser automation |
| pytest | Test runner |
| pytest-html | HTML test reports |

## Project structure
Selenium_with_python/
├── pages/ # Page Object classes (one per app page)
│ ├── login_page.py
│ ├── inventory_page.py
│ ├── cart_page.py
│ └── checkout_page.py
├── tests/ # Test files (one per feature area)
│ ├── test_login.py
│ ├── test_inventory.py
│ └── test_checkout.py
├── data/ # Externalized test data
│ ├── users.py
│ └── invalid_logins.json
├── conftest.py # Shared fixtures + screenshot-on-failure hook
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md


## Design decisions

- **Page Object Model**: each page's locators and actions live in one dedicated class, so a UI change only requires updating one file, not every test that touches that page.
- **Explicit waits** (`WebDriverWait` + `expected_conditions`) instead of `time.sleep()`, to avoid flaky, slow tests.
- **Fixture chaining**: a base `driver` fixture (fresh browser per test) and a `logged_in_driver` fixture built on top of it, avoiding repeated login code across tests.
- **Data-driven tests** via `@pytest.mark.parametrize`, with test data externalized to Python constants and JSON, separating test data from test logic.
- **Automatic screenshot capture on failure**, via a pytest hook, to aid debugging without needing to reproduce failures manually.

## Setup

```bash
git clone https://github.com/snehadevib/Selenium_with_python_poc.git
cd Selenium_with_python_poc
python -m venv venv
source venv/Scripts/activate      # Windows Git Bash
pip install -r requirements.txt
```

## Running the tests

Run everything:
```bash
python -m pytest tests/ -v
```

Run a single file:
```bash
python -m pytest tests/test_login.py -v
```

Generate an HTML report:
```bash
python -m pytest tests/ -v --html=report.html --self-contained-html
```

## Test coverage

- Valid login
- Locked-out user login
- Invalid login combinations (empty username, empty password, wrong credentials) — data-driven
- Add item to cart
- Full checkout flow (cart → checkout info → order confirmation)

## Possible next steps

- Cross-browser support (Firefox, Edge)
- GitHub Actions CI pipeline
- Allure reporting