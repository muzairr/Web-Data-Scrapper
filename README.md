# Web-Data-Scrapper
# 🔁 Daily Client File Downloader

This Python automation script logs into a web-based client portal, checks for new files, and downloads them to a local folder (`Downloads/client files`) on a Windows machine. It ensures no duplicate downloads by checking previously saved files.

## 📌 Features

- 🔐 Logs in using your username and password
- 📁 Scrapes and downloads new files from a client portal
- ✅ Skips already downloaded files
- 🧭 Saves files in a dedicated folder: `Downloads/client files`
- 🕒 Designed for daily scheduled execution via Windows Task Scheduler
- 🧪 Headless browser automation using Selenium

---

## ⚙️ Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (version must match your Chrome browser)

### 🧪 Python Dependencies

Install via pip:

```bash
pip install selenium requests beautifulsoup4
