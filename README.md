# QA Test Automation - Selenium

Automated UI testing framework using Selenium WebDriver, Python, and pytest with Page Object Model pattern.

## Tech Stack

- **Selenium WebDriver** - Browser automation
- **pytest** - Test runner and assertions
- **Page Object Model** - Maintainable test architecture
- **WebDriver Manager** - Automatic driver management
- **GitHub Actions** - CI/CD integration

## Test Coverage

| Test | Description |
|------|-------------|
| Successful login | Valid credentials redirect to inventory |
| Failed login | Invalid credentials show error |
| Empty username | Validation error for missing username |
| Full purchase flow | Login → add item → checkout → success |
| Multiple items | Add two items and verify cart count |

## Setup

```bash
pip install -r requirements.txt
pytest tests/ --html=reports/report.html
```

## CI

Tests run automatically on every push via GitHub Actions.
