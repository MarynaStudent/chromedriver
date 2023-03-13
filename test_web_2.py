from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()


def test_web_2():
    chrome = webdriver.Chrome('/.chromedriver')
    url = 'http://thedemosite.co.uk/savedata.php'
    chrome.get(url=url)
    input_box = chrome.find_element(By.NAME, "username")
    input_box.send_keys('Marina')
    input_box = chrome.find_element(By.NAME, "password")
    input_box.send_keys('1234')
    button = chrome.find_element(By.NAME, "FormsButton2")
    button.click()



def test_web_3():
    chrome = webdriver.Chrome('/.chromedriver')
    url = 'https://demoqa.com/text-box'
    chrome.get(url=url)
    input_box = chrome.find_element(By.ID, "userName")
    input_box.send_keys('Marina')
    input_box = chrome.find_element(By.ID, "userEmail")
    input_box.send_keys('marina@gmail.com')
    input_box = chrome.find_element(By.ID, "currentAddress")
    input_box.send_keys('Saint Petersburg')
    input_box = chrome.find_element(By.ID, "permanentAddress")
    input_box.send_keys('Orsha')
    button = chrome.find_element(By.ID, "submit")
    button.click()
