Playwright Pytest QA Automation Framework

Project Overview

This project is a QA Automation Test Framework built using Playwright with Python and Pytest. It is designed to demonstrate real‑world automated testing practices such as

* Page Object Model (POM)
* Data‑driven testing
* Session & authentication handling
* Positive and negative test coverage
* Scalable and maintainable test architecture

The application under test is OrangeHRM, commonly used for demo and practice automation projects.



# Tech Stack

* Language:** Python 3
* Automation Tool: Playwright
* Test Framework: Pytest
* Design Pattern: Page Object Model (POM)
* Data Sources: JSON & CSV
* Reporting: Pytest HTML reports (configurable)



## Project Structure


PLAYWRIGHT-PROJECTS/
│
├── pages/                  # Page Object classes
│   ├── orangehrm_login_page.py
│   └── orangehrm_home_page.py
│
├── tests/                  # Test cases
│   ├── api/                # API-related tests (if applicable)
│   ├── utils/              # Helper utilities for tests
│   ├── test_auth_session.py
│   ├── test_datadrivendemo.py
│   ├── test_login_invalid.py
│   ├── test_login_req_fields.py
│   ├── test_login_valid.py
│   └── test_logout.py
│
├── test_data/              # Test data files
│   ├── data.csv
│   └── data.json
│
├── reports/                # Test execution reports
│
├── conftest.py             # Pytest fixtures & setup
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Project dependencies
└── README.md




##  Test Coverage

The framework currently includes:

*  Valid login scenarios
*  Invalid login scenarios
*  Required field validation tests
*  Authentication & session persistence tests
*  Logout functionality tests
*  Data‑driven login tests using CSV & JSON



##  Setup & Installation

###  Clone the Repository

bash
git clone <repository-url>
cd playwright-projects


###  Create & Activate Virtual Environment

bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


###  Install Dependencies

bash
pip install -r requirements.txt


###  Install Playwright Browsers

bash
playwright install




##  Running Tests

### Run all tests

bash
pytest


### Run tests with detailed output

bash
pytest -v


### Run a specific test file

bash
pytest tests/test_login_valid.py




##  Reports

Test execution reports can be configured to generate HTML reports and are stored in the `reports/` directory.

Example:

bash
pytest --html=reports/report.html




## Design Principles Used

* **Page Object Model (POM)** for maintainability
* **Fixtures** for browser & test setup
* **Data‑Driven Testing** for scalability
* **Separation of concerns** between tests, pages, and data


##  Future Improvements

* CI/CD integration (GitHub Actions)
* Parallel test execution
* Cross‑browser testing
* Enhanced reporting & screenshots on failure

---

## Author

**Daniel Okpanachi **
QA Automation Engineer (Python | Playwright | Pytest)



 *This project is actively maintained and improved as part of a professional QA automation learning path.*
