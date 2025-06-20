from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# === CONFIG ===
CHROMEDRIVER_PATH = "./chromedriver.exe"
CRAFTY_URL = "https://[YOURCRAFTYURL]:8443"
SERVER_ID = "[YOURSERVERID]"
USERNAME = "[YOURUSERNAME]"
PASSWORD = "[YOURPASS]"
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
    driver.get(CRAFTY_URL + "/panel/server_detail?id=" + SERVER_ID + "&subpage=term")
    time.sleep(2)

    # 5. Fill in and send command
    start_z = 1199
    end_z = 1340
    step = 11

    x1, y1, x2, y2 = 189, 93, 189, 92
    block_type = "polished_deepslate"
    delay_seconds = 0.01

    for z in range(start_z, end_z + 1, step):
        command = f"fill {x1} {y1} {z} {x2} {y2} {z} {block_type}"
        command_input = driver.find_element(By.ID, "server_command")
        command_input.clear()
        command_input.send_keys(command)

         # Close toast if it exists
        try:
            close_btn = driver.find_element(By.CSS_SELECTOR, ".toast.show .fa-xmark")
            close_btn.click()
            time.sleep(0.01)
        except:
            pass

        driver.find_element(By.ID, "submit").click()
        print(f"✅ Sent: {command}")
        time.sleep(delay_seconds)

    print("✅ Command sent successfully.")

    time.sleep(3)

finally:
    driver.quit()
