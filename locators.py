#Для сайта https://baraholka.onliner.by/ написать локаторы (xpath или css - посмотрите, какой получится опимальным и решите):

#1) Поиска кнопки "Разместить объявление"
#2) Найти сколько объявлений в разделе "Ноутбуки. Компьютеры. Apple. Оргтехника", категория "Видеокарты"
#3) Найти сколько объявлений в разделе "Женская одежда", категория "Платья

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()

def test_locators_1():
    chrome = webdriver.Chrome('/.chromedriver')
    chrome.implicitly_wait(10)
    chrome.maximize_window()
    url = 'https://baraholka.onliner.by/'
    chrome.get(url=url)
    button = chrome.find_element(By.XPATH, '//*[@class="b-btn-fleamarket__1"]')
    video_cards = chrome.find_element(By.XPATH, '//html/body/div[1]/div[1]/div/div[2]/div[2]/div/div[5]/div[1]/div[2]/ul/li[9]/sup')
    dresses = chrome.find_element(By.CSS_SELECTOR, '#minWidth > div > div.l-gradient-wrapper > div.b-whbd > div > div.b-columntopic.columntopic-bah > div:nth-child(2) > div:nth-child(2) > ul > li:nth-child(5) > sup')
    time.sleep(10)



