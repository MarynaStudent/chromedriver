#1. test_checkbox: http://the-internet.herokuapp.com/dynamic_controls
#Найти чекбокс
#Нажать на кнопку
#Дождаться надписи “It’s gone”
#Проверить, что чекбокса нет
#Найти инпут
#Проверить, что он disabled
#Нажать на кнопку
#Дождаться надписи “It's enabled!”
#Проверить, что инпут enabled

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

def test_checkbox():
    chrome = webdriver.Chrome('/.chromedriver')
    url = 'http://the-internet.herokuapp.com/dynamic_controls'
    chrome.get(url=url)
    chrome.maximize_window()
    checkbox_locator = chrome.find_element(By.XPATH, '//*[@id="checkbox"]/input')
    button_check = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable(checkbox_locator))
    button_check.click()
    button = chrome.find_element(By.XPATH, '//*[@id="checkbox-example"]/button')
    button_click = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable(button))
    button_click.click()
    checkbox_locator = selenium.webdriver.support.expected_conditions.invisibility_of_element_located\
        ('//*[@id="checkbox"]/input')
    input1 = chrome.find_element(By.XPATH, '//*[@id="input-example"]/input')
    input1 = selenium.webdriver.support.expected_conditions.element_located_selection_state_to_be\
        ('//*[@id="input-example"]/input', 'disabled')
    button_enable = chrome.find_element(By.XPATH, '//*[@id="input-example"]/button')
    button_enable.click()
    input1 = selenium.webdriver.support.expected_conditions.element_located_selection_state_to_be \
        ('//*[@id="input-example"]/input', 'enabled')
    time.sleep(5)