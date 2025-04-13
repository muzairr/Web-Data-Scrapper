import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

# Configuration
USERNAME = "your_username"
PASSWORD = "your_password"
LOGIN_URL = "https://example.com/login"
FILES_URL = "https://example.com/files"
DOWNLOAD_DIR = os.path.join(os.path.expanduser("~"), "Downloads", "client files")

# Ensure download folder exists
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Initialize browser
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def login():
    driver.get(LOGIN_URL)
    time.sleep(2)
    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

def get_session_cookies():
    cookies = driver.get_cookies()
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    return session

def download_files(session):
    driver.get(FILES_URL)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    # Adjust this to match actual link elements
    links = soup.find_all("a", href=True)
    for link in links:
        file_url = link['href']
        file_name = os.path.basename(file_url)

        if not file_name.endswith(('.pdf', '.docx', '.xlsx')):  # adjust types
            continue

        file_path = os.path.join(DOWNLOAD_DIR, file_name)

        if os.path.exists(file_path):
            print(f"Already downloaded: {file_name}")
            continue

        print(f"Downloading: {file_name}")
        response = session.get(file_url)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download: {file_name}")

# Run the job
login()
session = get_session_cookies()
download_files(session)
driver.quit()
