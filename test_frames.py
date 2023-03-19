#2. test_frames: http://the-internet.herokuapp.com
#Frames
#Открыть iFrame
#Проверить, что текст внутри параграфа равен “Your content goes here.”

import time
import selenium as selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()

def test_frames():
    chrome = webdriver.Chrome('/.chromedriver')
    url = 'https://the-internet.herokuapp.com/'
    chrome.get(url=url)
    chrome.maximize_window()
    frames = chrome.find_element(By.XPATH, '//*[@id="content"]/ul/li[22]/a')
    frames.click()
    iframe = chrome.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/a')
    iframe.click()
    text = selenium.webdriver.support.expected_conditions.text_to_be_present_in_element\
        ('//*[@id="tinymce"]/p', 'Your content goes here.')
    time.sleep(5)