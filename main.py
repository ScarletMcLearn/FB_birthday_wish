from selenium import webdriver
from bs4 import BeautifulSoup
import os
import getpass 
  
if os.name == 'nt':
    chrome_path = r"./chromedriver_win32/chromedriver.exe"
else:
    chrome_path = r"./chromedriver_linux64/chromedriver"

print("While entering password nothing may appear on the screen, but be sure to type it right as this option is just for security. ")

user = input("Enter Your Facebook Login Username, Phone Number or Email:  ")
password = getpass.getpass(prompt='Enter Your Facebook Login Password:  ') 
wish="Wish You Many Many Happy Returns of The Day :D"


driver=webdriver.Chrome(chrome_path)

driver.get("https://www.facebook.com/login")
driver.find_element_by_id('email').send_keys(user)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()

driver.get("https://www.facebook.com/events/birthdays/")
areas = driver.find_elements_by_tag_name('textarea')

for area in areas:
    area.send_keys(wish)
    area.submit()

driver.quit()

