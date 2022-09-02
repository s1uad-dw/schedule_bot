import time
import os
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def get_screens():
    op = webdriver.ChromeOptions()
    op.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    op.add_argument("--headless")
    op.add_argument("--no-sandbox")
    op.add_argument("--disable-dev-sh-usage")

    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=op)
    driver.get('https://drive.google.com/drive/folders/1Mq-Yb-NzAPZmzUuonMfK68hbA-NGXJcq?lfhs=2')
    files = driver.find_elements(by=By.CLASS_NAME, value='pmHCK')
    i = 0
    for file in files:
        file.click()
        driver.set_window_size(width=710, height=2500)
        time.sleep(4)
        driver.get_screenshot_as_file(f'./screenshots/day{i}.png')
        time.sleep(1)
        img = Image.open(f'./screenshots/day{i}.png')
        new = img.crop((12, 56, 680, 910))
        new.save(f'./screenshots/day{i}.png')
        driver.find_element(by=By.XPATH, value='/html/body/div[11]/div[4]/div/div[1]/div[1]/div').click()
        i+=1
    driver.quit()
    return i
get_screens()
