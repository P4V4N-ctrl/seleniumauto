🚀 Selenium POM Automation Framework (Python + Pytest)

A scalable and maintainable test automation framework built using Python, Selenium WebDriver, and Pytest following the Page Object Model (POM) design pattern.
This framework automates the end-to-end user workflow of the SauceDemo web application, including login and checkout form submission scenarios.

⸻

🌟 Key Features
	•	Page Object Model (POM): Separation of locators and test logic for better maintainability.
	•	Pytest Fixtures: Centralized browser setup and teardown using conftest.py.
	•	Explicit Waits: Implemented WebDriverWait for handling dynamic web elements.
	•	Dynamic Test Data: Faker library used to generate unique test data for each test run.
	•	HTML Reporting: Automated report generation using pytest-html.
	•	Screenshot on Failure: Automatically captures screenshots for failed test cases.
	•	Headless Execution: Tests can run in headless mode.
	•	Modular Framework Structure: Organized into pages, tests, config, and utilities.

📁 Project Structure
selenium-automation/
│
├── pages/           # Page Object classes (locators + actions)
├── tests/           # Test cases
├── config/          # Configuration files (URL, test data)
├── screenshots/     # Failure screenshots
├── conftest.py      # Pytest fixtures (browser setup/teardown)
├── pytest.ini       # Pytest configuration
├── report.html      # HTML test report
├── requirements.txt # Dependencies
└── README.md        # Project documentation

🛠️ Setup & Installation
Clone the repository:

git clone <your-repository-url>
cd selenium-automation

Create virtual environment and install dependencies

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt


🚦 How to Run Tests
Run all tests
pytest -v

Run tests with HTML report
pytest --html=report.html --self-contained-html

To run all tests and generate a professional HTML report, use the following command:

Bash
pytest --html=report.html --self-contained-html
📈 Viewing Results
Terminal: You will see a summary of passed/failed tests.

HTML Report: Open report.html in any browser to see the visual dashboard.

🧪 Technologies Used
	•	Python
	•	Selenium WebDriver
	•	Pytest
	•	Page Object Model (POM)
	•	Pytest HTML Reports
	•	Faker (Test Data Generation)
	•	Git

⸻

🧪 Test Scenarios Covered
	•	Login functionality
	•	Form submission
	•	End-to-end user workflow
	•	UI validation and assertions
	•	Error handling and screenshot capture


Screenshots: If a test fails, a time-stamped screenshot is automatically saved in the screenshots/ folder.

🧪 Implementation Details (Task Requirements)

Task 1: Environment configured with venv and requirements.txt.

Task 2: Automated Login and Checkout Form with navigation logic.

Task 3: Implemented Explicit Waits and used pytest assertions for validation.

Task 4: Full Page Object Model implementation for scalability.

Task 5: Integrated pytest-html for reporting and custom screenshot hooks in conftest.py.

Bonus (Optional): Browser setup includes detach options and support for headless execution.

👨‍💻 Author
Pavan - Quality Assurance Automation
