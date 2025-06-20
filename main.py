from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# === CONFIG ===
CHROMEDRIVER_PATH = "./chromedriver.exe"
CRAFTY_URL = "https://[YOURCRAFTYURL]:8443"
USERNAME = "[YOURUSERNAME]"
PASSWORD = "[YOURPASS]"
SERVER_DETAIL_URL = CRAFTY_URL + "/panel/server_detail?id=[YOURSERVERID]&subpage=term"
COMMAND = "gamemode survival testuser"

# === SETUP ===
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

try:
    # 1. Go to login page
    driver.get(CRAFTY_URL)
    time.sleep(2)

    # 2. Fill in login form
    driver.find_element(By.ID, "username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)

    # 3. Submit login form
    driver.find_element(By.CLASS_NAME, "submit-btn").click()
    time.sleep(3)  # wait for login to complete

    # 4. Navigate to the server terminal
    driver.get(SERVER_DETAIL_URL)
    time.sleep(2)

    # 5. Fill in and send command
    driver.find_element(By.ID, "server_command").send_keys(COMMAND)
    driver.find_element(By.ID, "submit").click()

    print("✅ Command sent successfully.")

    time.sleep(3)  # wait to observe output

finally:
    driver.quit()
