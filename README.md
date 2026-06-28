# 🚀 Selenium Mastery From Scratch

> **A complete beginner-to-expert journey in Selenium WebDriver automation**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.45.0-green.svg)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/pallavi-dhadage/Selenium-Mastery-From-Scratch)](https://github.com/pallavi-dhadage/Selenium-Mastery-From-Scratch/stargazers)

---

## 📚 Table of Contents
- [About This Repository](#-about-this-repository)
- [Who Is This For](#-who-is-this-for)
- [What You'll Learn](#-what-youll-learn)
- [Repository Structure](#-repository-structure)
- [Quick Start](#-quick-start)
- [Learning Path](#-learning-path)
- [Prerequisites](#-prerequisites)
- [Common Issues & Solutions](#-common-issues--solutions)
- [Contributing](#-contributing)
- [Support](#-support)
- [License](#-license)

---

## 📖 About This Repository

Welcome to the **Selenium Mastery** repository! This is a complete, hands-on guide to mastering Selenium WebDriver automation. Whether you're a complete beginner or an experienced tester looking to brush up your skills, this repository has everything you need.

This repository is designed to be your **one-stop resource** for learning Selenium WebDriver with Python. Each folder contains carefully crafted scripts that build upon the previous ones, taking you from absolute beginner to confident automation engineer.

---

## 👨‍🎓 Who Is This For?

- ✅ **Absolute Beginners** - Start from "Hello World" level
- ✅ **Manual Testers** - Transition to test automation
- ✅ **DevOps Engineers** - Add UI testing to your CI/CD pipeline
- ✅ **Students** - Complete your academic projects
- ✅ **Anyone** who wants to automate web tasks!

---

## 🎯 What You'll Learn

| Topic | Description |
|-------|-------------|
| **Environment Setup** | Virtual environments, package installation, WebDriver management |
| **Locators** | ID, Name, Class, XPath, CSS Selectors - Master them all |
| **Actions** | Click, type, select dropdowns, check boxes |
| **Waits** | Implicit, Explicit, Fluent Waits - Professional strategies |
| **Advanced Topics** | Screenshots, windows, frames, JavaScript execution |
| **Real Projects** | Google search, Amazon scraping, YouTube automation |

---

## 🗂️ Repository Structure
Selenium-Mastery-From-Scratch/
├── 📄 README.md - You're here!
├── 📄 requirements.txt - All Python dependencies
├── 📄 .gitignore - Git ignore rules
│
├── 📁 01_basics/ - Lesson 1: Getting Started ✅
│ └── first_script.py - Open browser, navigate, get title
│
├── 📁 02_element_finders/ - Lesson 2: Finding Elements ✅
│ └── by_xpath.py - Google search using XPath
│
├── 📁 03_actions/ - Lesson 3: Interactions 🚧
│ ├── click_buttons.py - Click different types of buttons
│ ├── send_keys.py - Type into input fields
│ ├── dropdowns.py - Handle dropdown menus
│ ├── checkboxes.py - Check/Uncheck boxes
│ └── alerts.py - Handle pop-up alerts
│
├── 📁 04_waits/ - Lesson 4: Professional Waits 🚧
│ ├── implicit_wait.py - Implicit wait example
│ ├── explicit_wait.py - WebDriverWait examples
│ ├── fluent_wait.py - Fluent wait examples
│ └── wait_conditions.py - Different expected conditions
│
├── 📁 05_advanced/ - Lesson 5: Advanced Topics 🚧
│ ├── screenshots.py - Take screenshots
│ ├── multiple_windows.py - Handle multiple windows
│ ├── iframes.py - Work with iframes
│ └── javascript.py - Execute JavaScript
│
├── 📁 06_projects/ - Lesson 6: Real Projects 🚧
│ ├── google_search_automation.py
│ ├── amazon_product_scraper.py
│ └── youtube_playlist_automation.py
│
└── 📁 practice_exercises/ - Homework with solutions 🚧
├── exercise_1.md
├── exercise_2.md
└── 📁 solutions/

text

**Legend:** ✅ Available | 🚧 Coming Soon

---

## ⚡ Quick Start

### Step 1: Clone the Repository
```bash
git clone https://github.com/pallavi-dhadage/Selenium-Mastery-From-Scratch.git
cd Selenium-Mastery-From-Scratch
Step 2: Create Virtual Environment
bash
python3 -m venv selenium_env
source selenium_env/bin/activate  # On Windows: selenium_env\Scripts\activate
Step 3: Install Dependencies
bash
pip install -r requirements.txt
Step 4: Run Your First Script
bash
python 01_basics/first_script.py
Step 5: Deactivate Virtual Environment (When Done)
bash
deactivate
📚 Learning Path
Lesson	Topic	Status	What You'll Build
1️⃣	Introduction	✅	Open browser, get page title
2️⃣	Locators	✅	Find elements using XPath
3️⃣	Actions	🚧	Click, type, select, check
4️⃣	Waits	🚧	Make scripts robust and fast
5️⃣	Advanced	🚧	Screenshots, windows, frames
6️⃣	Projects	🚧	Real-world automation scripts
📋 Prerequisites
Before you start, make sure you have:

✅ Python 3.8+ installed

✅ pip (Python package manager)

✅ Google Chrome browser installed

✅ Git for version control

✅ VS Code or any code editor (recommended)

Verify Your Setup
bash
# Check Python version
python3 --version

# Check pip version
pip --version

# Check Chrome version
google-chrome --version
🔧 Common Issues & Solutions
Issue 1: ModuleNotFoundError: No module named 'selenium'
Solution: Activate your virtual environment and install dependencies

bash
source selenium_env/bin/activate  # Activate venv
pip install -r requirements.txt   # Install packages
Issue 2: externally-managed-environment Error
Solution: You're trying to install globally. Use a virtual environment:

bash
python3 -m venv selenium_env
source selenium_env/bin/activate
pip install selenium webdriver-manager
Issue 3: ChromeDriver Not Found
Solution: We use webdriver-manager which handles this automatically. Make sure it's installed:

bash
pip install webdriver-manager
Issue 4: Chrome Browser Not Found
Solution: Install Google Chrome:

bash
# On Ubuntu/WSL
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
sudo apt update
sudo apt install google-chrome-stable -y
🚀 Running Scripts
bash
# Activate virtual environment
source selenium_env/bin/activate

# Run any script
python 01_basics/first_script.py
python 02_element_finders/by_xpath.py

# Deactivate when done
deactivate
🤝 Contributing
Contributions are welcome! Here's how you can help:

Fork the repository

Create a feature branch: git checkout -b feature/amazing-feature

Commit changes: git commit -m 'Add some amazing feature'

Push to branch: git push origin feature/amazing-feature

Open a Pull Request

Contribution Ideas:
Add new scripts for different locators

Create more projects

Improve documentation

Fix bugs

Add comments and explanations

💬 Support
Issues: Open an issue

Discussions: Start a discussion

Email: psdhadage18@gmail.com

📜 License
This project is open source and available under the MIT License.

⭐ Show Your Support
If this repository helped you, please give it a ⭐ Star on GitHub!

👩‍💻 Author
Pallavi Dhadage

GitHub: @pallavi-dhadage

LinkedIn: Pallavi Dhadage

📚 Recommended Resources
Official Documentation
Selenium WebDriver Documentation

Python Documentation

Practice Websites
The Internet - Herokuapp

Google

YouTube

Books
"Selenium WebDriver Practical Guide" by Unmesh Gundecha

"Python Testing with Selenium" by Sujay Raghavendra

🎯 Roadmap
Week 1: Foundations ✅
Environment setup

First script

XPath locators

Week 2: Interactions 🚧
Click buttons

Form filling

Dropdowns

Checkboxes

Alerts

Week 3: Professional Waits 🚧
Implicit waits

Explicit waits

Fluent waits

Expected conditions

Week 4: Advanced Topics 🚧
Screenshots

Multiple windows

Frames

JavaScript execution

Week 5: Projects 🚧
Google search automation

Amazon product scraper

YouTube playlist automation

📊 Stats
https://img.shields.io/github/repo-size/pallavi-dhadage/Selenium-Mastery-From-Scratch
https://img.shields.io/github/contributors/pallavi-dhadage/Selenium-Mastery-From-Scratch
https://img.shields.io/github/last-commit/pallavi-dhadage/Selenium-Mastery-From-Scratch

Happy Automating! 🚀

Made with ❤️ and Python

