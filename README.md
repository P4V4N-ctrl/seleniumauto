🚀 Selenium POM Automation Framework
A professional-grade test automation framework built with Python, Selenium, and Pytest. This project automates the end-to-end journey of a user on the SauceDemo website, including secure login and dynamic form submission.

🌟 Key Features
Page Object Model (POM): Clean separation between page elements and test logic.

Single-Session Execution: Optimized to run the entire suite in one browser window.

Dynamic Data: Uses the Faker library to generate unique user data for every test run.

Robust Waiting: Implements Explicit Waits (WebDriverWait) to handle asynchronous elements—no time.sleep() used.

Automated Reporting: Generates detailed HTML reports with embedded failure screenshots.

📁 Project Structure
Plaintext
selenium-automation/
├── pages/               # Page Classes (Locators & Actions)
│   ├── login_page.py
│   └── form_page.py
├── tests/               # Test Scripts
│   ├── test_login.py
│   └── test_form_submission.py
├── config/              # Configuration (URLs, Credentials)
│   └── config.json
├── screenshots/         # Automated failure captures
├── conftest.py          # Pytest Fixtures & Browser Setup
├── pytest.ini           # Test Configuration
└── requirements.txt     # Dependency list
🛠️ Setup & Installation
Clone the repository:

Bash
git clone <your-repo-url>
cd selenium-automation
Create and activate a virtual environment:

Bash
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
Install dependencies:

Bash
pip install -r requirements.txt
🚦 How to Run the Tests
To run all tests and generate a professional HTML report, use the following command:

Bash
pytest --html=report.html --self-contained-html
📈 Viewing Results
Terminal: You will see a summary of passed/failed tests.

HTML Report: Open report.html in any browser to see the visual dashboard.

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
