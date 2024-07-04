from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#headless window
options = Options()
options.headless = True

#gets chrome driver
service = Service(executable_path="/Users/rohitnikam/chromedriver-mac-x64/chromedriver")

#sets browser and page to view
browser = webdriver.Chrome(options=options, service=service)
browser.get('https://utd.bioraft.com/')

def signin():
    login = browser.find_element(By.LINK_TEXT, "Log in with your NetID and Password")
    login.click()

    netid = browser.find_element(By.ID, "netid")
    netid.click()
    netid.send_keys("username")

    password = browser.find_element(By.ID, "password")
    password.click()
    password.send_keys("password")

    loginButton = browser.find_element(By.ID, "submit")
    loginButton.click()

def ppe():
    ppeLaunch = browser.find_element(By.LINK_TEXT, "Launch Course")
    ppeLaunch.click()

    ppemodule = browser.find_element(By.XPATH, '//a[contains(@href, "raftTrainingModule/player.html?course_url=/UTD/Personal_Protective_Equipment_2021_Feb_8/imsmanifest.xml")]')
    time.sleep(5)
    ppemodule.click()
    time.sleep(5)
    amount = 30
    for i in range(amount):
        ppenext = browser.find_element(By.XPATH, '//a[contains(@href, "raftTrainingModule/player.html?course_url=/UTD/Bloodborne_Pathogens_2021_Jan_6/imsmanifest.xml")]')
        time.sleep(5)
        ppenext.click()



#main function
signin()
ppe()

time.sleep(10)

browser.quit()