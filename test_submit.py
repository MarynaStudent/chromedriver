#3 теста:
#тест1:
#Заполните форму обратной связи
#Нажмите на кнопку "Submit"
#Проверьте наличие сообщения "Form filled out successfully"
#тест2:
#Заполните поле "Name"
#Нажмите на кнопку "Submit"
#Проверьте наличие сообщения об ошибке
#тест3:
#Заполните поле "Message"
#Нажмите на кнопку "Submit"
#Проверьте наличие сообщения об ошибке

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()
def test_web_form():
    chrome = webdriver.Chrome('/.chromedriver')
    chrome.implicitly_wait(10)
    chrome.maximize_window()
    url = 'https://ultimateqa.com/complicated-page/'
    chrome.get(url=url)
    input_box = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_name_0"]')
    input_box.send_keys('Marina')
    input_box = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_email_0"]')
    input_box.send_keys('marina@gmail.com')
    input_box = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_message_0"]')
    input_box.send_keys('Hello, how are you?')
    input_box = chrome.find_element(By.XPATH, '// *[ @ id = "et_pb_contact_form_0"] / div[2] / form / div / div / p / input')
    input_box.send_keys('20')
    button = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div[2]/form/div/button')
    button.click()
    time.sleep(10)

def test_web_name():
    chrome = webdriver.Chrome('/.chromedriver')
    chrome.implicitly_wait(10)
    chrome.maximize_window()
    url = 'https://ultimateqa.com/complicated-page/'
    chrome.get(url=url)
    input_box = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_name_1"]')
    input_box.send_keys('Dusya')
    button = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_form_1"]/div[2]/form/div/button')
    button.click()
    time.sleep(10)

def test_web_message():
    chrome = webdriver.Chrome('/.chromedriver')
    chrome.implicitly_wait(10)
    chrome.maximize_window()
    url = 'https://ultimateqa.com/complicated-page/'
    chrome.get(url=url)
    input_box = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_message_1"]')
    input_box.send_keys('I am crazy')
    button = chrome.find_element(By.XPATH, '//*[@id="et_pb_contact_form_1"]/div[2]/form/div/button')
    button.click()
    time.sleep(10)