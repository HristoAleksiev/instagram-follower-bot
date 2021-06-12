from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition
import os
import time as t

user = os.getenv("USERNAME")
password = os.getenv("PASS")

chrome_driver_path = "C:\Python Stuff\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

site = "https://www.instagram.com/accounts/login/"

driver.get(url=site)

target_account = "instagram"

driver.find_element_by_xpath('/html/body/div[3]/div/div/button[1]').click()

# Login
WebDriverWait(driver, 10). \
    until(condition.presence_of_element_located((By.XPATH,
                                                 '//*[@id="loginForm"]/div/div[1]/div/label/input'))) \
    .send_keys(user)
WebDriverWait(driver, 10). \
    until(condition.presence_of_element_located((By.XPATH,
                                                 '//*[@id="loginForm"]/div/div[2]/div/label/input'))) \
    .send_keys(password)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

# find the target account
WebDriverWait(driver, 10). \
    until(condition.presence_of_element_located((By.XPATH,
                                                 '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))) \
    .send_keys(target_account)
WebDriverWait(driver, 10). \
    until(condition.presence_of_element_located((By.XPATH,
                                                 '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/'
                                                 'div/div[2]/div/div[1]/a'))) \
    .click()

# get to followers popup
WebDriverWait(driver, 10). \
    until(condition.presence_of_element_located((By.XPATH,
                                                 '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'))) \
    .click()

popup_body = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
WebDriverWait(driver, 10). \
    until(condition.presence_of_element_located((By.XPATH,
                                                 '/html/body/div[5]/div/div/div[2]/ul/div')))
follow_list = driver.find_elements_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li')

position = 0
while True:
    for itr in range(7):
        follow_button = follow_list[position].find_element_by_tag_name("button")
        print(follow_button.text)
        if follow_button.text == "Follow":
            follow_button.click()
        position += 1
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;", popup_body)
    t.sleep(2)
    follow_list = driver.find_elements_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li')
