#всего 3 теста на каждый тип локатора:
#Откройте страницу: https://ultimateqa.com/complicated-page/
#Нажмите на 2-ю сверху кнопку во втором столбце используя:
#XPATH
#CSS selector
#class name

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()

def test_locators_xpath():
    chrome = webdriver.Chrome('/.chromedriver')
    chrome.implicitly_wait(10)
    chrome.maximize_window()
    url = 'https://ultimateqa.com/complicated-page/'
    chrome.get(url=url)
    button = chrome.find_element(By.XPATH, '//div[@class="et_pb_row et_pb_row_2 et_pb_row_4col"]//div[2]//div[2]')
    button.click()
    time.sleep(10)

def test_locators_name():
    chrome = webdriver.Chrome('/.chromedriver')
    chrome.implicitly_wait(10)
    chrome.maximize_window()
    url = 'https://ultimateqa.com/complicated-page/'
    chrome.get(url=url)
    button = chrome.find_element(By.CLASS_NAME, 'et_pb_button et_pb_button_4 et_pb_bg_layout_light')
    button.click()
    time.sleep(10)

def test_locators_CSS():
    chrome = webdriver.Chrome('/.chromedriver')
    chrome.implicitly_wait(10)
    chrome.maximize_window()
    url = 'https://ultimateqa.com/complicated-page/'
    chrome.get(url=url)
    button = chrome.find_element(By.CSS_SELECTOR, '[class="et_pb_button et_pb_button_4 et_pb_bg_layout_light"]')
    button.click()
    time.sleep(10)
