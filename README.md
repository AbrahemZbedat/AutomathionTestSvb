
---

````markdown
# SVBurger Automation Testing 🧪🍔

This project contains automated tests using Selenium for the website: [svburger1.co.il](https://svburger1.co.il)

## 📋 Description

Automated UI test suite for end-to-end testing of the SVBurger web application, including:

- Sign Up with valid and invalid data
- Login with valid and invalid credentials
- Duplicate account detection
- Form validation (empty fields)
- Weather feature search
- Access control to protected pages

## 🧰 Technologies Used

- Python 3
- Selenium WebDriver
- webdriver-manager
- Chrome browser

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/svburger-automation.git
   cd svburger-automation
````

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create `requirements.txt` if missing:

   ```txt
   selenium
   webdriver-manager
   ```

## 🚀 How to Run the Tests

You can run the test functions individually by calling them in your main file or using a test runner like `pytest` (with slight adaptation).

Example (run manually from Python script):

```python
test_signUp_with_correct_data()
test_signUp_with_wrong_data()
test_signInWithCorrectData()
test_signInWithWrongData()
test_weather_correct_data()
test_weather_wrong_data()
test_signUp_with_empty_fields()
test_signUp_duplicate_email()
test_access_protected_page_without_login()
```

## ✅ Test Coverage

| Test                                       | Description                               |
| ------------------------------------------ | ----------------------------------------- |
| `test_signUp_with_correct_data`            | Valid registration flow                   |
| `test_signUp_with_wrong_data`              | Registration with mismatched passwords    |
| `test_signInWithCorrectData`               | Login with correct credentials            |
| `test_signInWithWrongData`                 | Login with incorrect credentials          |
| `test_weather_correct_data`                | Search for valid weather location         |
| `test_weather_wrong_data`                  | Search for invalid weather location       |
| `test_signUp_with_empty_fields`            | Submitting form with no input             |
| `test_signUp_duplicate_email`              | Attempt to register with same email again |
| `test_access_protected_page_without_login` | Check unauthorized access                 |

## 📌 Notes

* Test automation uses randomly generated emails to avoid duplication.
* Alerts and error messages are handled via Selenium alerts or body text.
* Requires Google Chrome to be installed on the system.

## 🧑‍💻 Author

Abrahem Zbedat

## 📄 License

This project is licensed under the MIT License.

```

```
