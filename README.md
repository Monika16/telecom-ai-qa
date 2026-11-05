# AI-Assisted Guru99 Telecom QA Automation Project

## 1. Project Overview

This project focuses on building a real-world QA automation framework for the Guru99 Telecom application using Python, Playwright, and pytest.

The goal is to demonstrate practical software testing skills, including test scenario design, test automation, Page Object Model (POM), dynamic test data generation, and AI-assisted test design.

The project follows an incremental approach, starting with the Add Customer module and gradually expanding to other telecom application features.

**Application Under Test:**
https://demo.guru99.com/telecom/index.html

## 2. Project Objectives

* Design positive and negative test scenarios.
* Identify missing test scenarios with AI assistance.
* Build a maintainable automation framework using Python and Playwright.
* Implement Page Object Model (POM).
* Use pytest fixtures for reusable test setup.
* Generate dynamic test data.
* Automate functional and validation scenarios.
* Maintain traceability between test cases and automation scripts.
* Integrate automated tests with CI/CD pipelines in future phases.

## 3. Technology Stack

| Technology | Purpose                             |
|------------|-------------------------------------|
| Python     | Programming language                |
| Playwright | Browser automation                  |
| pytest     | Test execution and framework        |
| PyCharm    | Development environment             |
| Git        | Version control                     |
| GitHub     | Source code repository              |
| AI         | Test scenario generation and review |

## 4. Project Structure

```text
telecom-ai-qa/
│
├── pages/
│   ├── home_page.py
│   └── customer_page.py
│
├── tests/
│   └── ui/
│       └── test_customer.py
│
├── utils/
│   ├── test_data.py
│   └── dialog_handler.py
│
├── test_cases/
│   ├── customer_test_cases.md
│   ├── day1_test_scenarios.md
│   ├── day3_test_scenarios.md
│   └── test_traceability.md
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

*The structure will evolve as additional modules and testing capabilities are implemented.*

## 5. Automation Framework Design

The project uses the Page Object Model (POM) design pattern.

Key components:

* **Page Objects:** Maintain page locators and reusable page actions.
* **pytest Fixtures:** Handle browser and page setup.
* **Dynamic Test Data:** Generate unique customer details for test execution.
* **Reusable Dialog Handler:** Handle browser JavaScript dialogs.
* **Test Scripts:** Keep test scenarios separate from page interaction logic.

## 6. Current Automation Scope – Add Customer Module

The initial focus is the Add Customer functionality.

### Automated Test Scenarios

| Test ID    | Scenario                            | Status    | Result |
|------------|-------------------------------------|-----------|--------|
| AC-001     | Add customer with valid details     | Automated | Passed |
| AC-011     | Leading spaces in First Name        | Automated | Passed |
| AC-012     | Trailing spaces in First Name       | Automated | Passed |
| AC-015     | Submit with empty First Name        | Automated | Passed |
| AC-016     | Submit with empty Last Name         | Automated | Passed |
| AC-017     | Submit with empty Email             | Automated | Passed |
| AC-018     | Submit with empty Address           | Automated | Passed |
| AC-019     | Submit with empty Telephone         | Automated | Passed |
| AC-020     | Submit with invalid Email format    | Automated | Passed |

**Current automation progress:** 7 test scenarios automated and reported as passed.

Additional scenarios are documented and will be automated incrementally.

## 7. AI-Assisted Testing

AI is used as an assistant during test design and review.

Current activities:

* Generate additional test scenarios from application requirements.
* Identify missing positive and negative scenarios.
* Review scenarios for duplicates and overlapping coverage.
* Prioritize scenarios for automation.
* Support test documentation and test coverage analysis.

AI-generated scenarios are reviewed and validated before being included in the automation suite.

## 8. Parameterized Testing
Pytest parameterization is used to execute multiple input variations using a single test function.

Current implementation includes:

First Name validation with leading spaces.
First Name validation with trailing spaces.
Multiple input combinations with expected validation results.
Reusable test logic to reduce duplicate automation code.

Example:

@pytest.mark.parametrize(
    "first_name, expected_output",
    [
        ("      John", "First character can not have space"),
        ("John        ", ""),
    ]
)
def test_add_customer_firstname_with_spaces(...):
    ...

Parameterized tests improve test coverage, maintainability, and code reusability.

## 9. Installation and Setup

### Prerequisites

* Python 3.x
* PyCharm
* Git
* GitHub account

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/telecom-ai-qa.git
```

Navigate to the project directory:

```bash
cd telecom-ai-qa
```

### Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate the environment on macOS:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Install Playwright browser:

```bash
playwright install chromium
```

## 10. Execute Automation Tests

Run all tests:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/ui/test_customer.py -v
```

Generate an HTML report (if pytest-html is installed):

```bash
pytest -v --html=reports/report.html --self-contained-html
```

## 11. Test Documentation

Test scenarios and detailed test cases are maintained separately.

* `day1_test_scenarios.md` – Initial requirements-based test scenarios.
* `day3_test_scenarios.md` – Additional AI-assisted scenarios.
* `customer_test_cases.md` – Detailed functional test cases.
* `test_traceability.md` – Mapping between test IDs and automation scripts.

## 12. Future Enhancements

The following capabilities are planned:

* Complete Add Customer test coverage.
* Pytest parameterization and data-driven testing.
* API testing using Python Requests.
* API and UI test integration.
* AI-assisted test case generation and optimization.
* AI-assisted failure analysis.
* GitHub Actions CI/CD integration.
* Agentic AI for software testing.
* Extend automation to Create Tariff Plan, Assign Tariff Plan, and View Customer Billing.

## 13. Project Status

**Current Phase:** Add Customer Module – UI Automation

| Milestone                     | Status      |
|-------------------------------|-------------|
| Requirements analysis         | Completed   |
| Test scenario identification  | Completed   |
| Python and Playwright setup   | Completed   |
| Page Object Model             | Implemented |
| Dynamic test data             | Implemented |
| Positive test automation      | Completed   |
| Required-field negative tests | Completed   |
| Invalid email validation      | Completed   |
| Whitespace validation         | Completed   |
| Parameterized testing         | Completed   |
| API testing                   | Planned     |
| CI/CD integration             | Planned     |
| Agentic AI testing            | Planned     |

## Day-wise Progress section

| Day  | Work completed                                           |
|------|----------------------------------------------------------|
| Day1 | Requirements analysis and test scenario documentation    |
| Day2 | POM, fixtures, dynamic test data and positive automation |
| Day3 | AI-assisted test scenario review and negative testing    |
| Day4 | Required-field validation automation                     |
| Day5 | Whitespace validation and pytest parameterization        |

---

## Author's Note

This is a hands-on QA automation portfolio project demonstrating practical testing knowledge, automation framework development, AI-assisted test design, and continuous improvement of software quality.

The project is being developed incrementally, with test coverage and framework capabilities expanded as each milestone is completed.
