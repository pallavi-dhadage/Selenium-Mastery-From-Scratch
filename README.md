# 🚀 Selenium Mastery From Scratch

> A complete beginner-to-expert journey in Selenium WebDriver automation with Python

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.15.0-green.svg)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

---

## 📖 About

This repository contains a structured learning path for mastering **Selenium WebDriver** automation using Python. Each lesson builds upon the previous, taking you from absolute beginner to confident automation engineer.

### What You'll Learn
- ✅ Environment setup with virtual environments
- ✅ Finding elements using ID, Name, Class, XPath, CSS
- ✅ Form filling, login automation, dropdowns, checkboxes
- ✅ Professional wait strategies (Explicit, Implicit, Fluent)
- ✅ Screenshots, multiple windows, iframes, JavaScript execution
- ✅ Real-world automation projects

---

## 📁 Project Structure
Selenium-Mastery-From-Scratch/
├── 01_basics/ # Lesson 1: Getting Started
│ └── first_script.py
├── 02_element_finders/ # Lesson 2: Locators
│ └── by_xpath.py
├── 03_actions/ # Lesson 3: Interactions
│ ├── login_automation.py
│ ├── form_filling.py
│ ├── dropdown_handling.py
│ └── checkboxes_radio.py
├── 04_waits/ # Lesson 4: Professional Waits
├── 05_advanced/ # Lesson 5: Advanced Topics
├── 06_projects/ # Lesson 6: Real Projects
├── requirements.txt # Python dependencies
└── README.md # Documentation

text

---

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/pallavi-dhadage/Selenium-Mastery-From-Scratch.git
cd Selenium-Mastery-From-Scratch
2. Create Virtual Environment
bash
python3 -m venv selenium_env
source selenium_env/bin/activate  # On Windows: selenium_env\Scripts\activate
3. Install Dependencies
bash
pip install -r requirements.txt
4. Run Your First Script
bash
python 01_basics/first_script.py
5. Deactivate Environment
bash
deactivate
📚 Learning Path
Lesson	Topic	Status
1	Basics - First script, browser navigation	✅
2	Locators - XPath, ID, Name, CSS	✅
3	Actions - Forms, login, dropdowns, checkboxes	✅
4	Waits - Implicit, Explicit, Fluent	🚧
5	Advanced - Screenshots, windows, frames	🚧
6	Projects - Real-world automation	🚧
🛠️ Tech Stack
Python 3.8+ - Programming language

Selenium WebDriver - Browser automation

WebDriver Manager - Automatic driver management

Pytest - Testing framework

📊 Scripts Overview
Script	Description
first_script.py	Open browser, navigate, get page title
by_xpath.py	Google search using XPath locators
login_automation.py	Automate login with credentials
form_filling.py	Complete form filling with various inputs
dropdown_handling.py	Handle dropdown menus (Select class)
checkboxes_radio.py	Handle checkboxes and radio buttons
🔧 Common Issues & Solutions
ModuleNotFoundError: No module named 'selenium'
bash
source selenium_env/bin/activate
pip install -r requirements.txt
externally-managed-environment Error
bash
python3 -m venv selenium_env
source selenium_env/bin/activate
pip install selenium webdriver-manager
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository

Create your feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👩‍💻 Author
Pallavi Dhadage

GitHub: @pallavi-dhadage

⭐ Show Your Support
If this repository helped you, please give it a ⭐ Star on GitHub!

Happy Automating! 🚀
