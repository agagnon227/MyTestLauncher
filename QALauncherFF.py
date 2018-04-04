from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time, getpass


myAccount = input('Account: ')
myPass = getpass.getpass('Password: ')
browser = webdriver.Firefox()
sites = ['https://outlook.office.com/', 'https://hipchat.com/sign_in/',
        'https://jira.transparent.com/', 'https://confluence.transparent.com',
        'https://screencast-o-matic.com/screen_recorder/']

def delay():
    return time.sleep(2)
def newTab(x):
    new = browser.execute_script("window.open('')")
    new = browser.switch_to.window(browser.window_handles[x])
    return new
def windowSwitch(x):
    return browser.switch_to.window(browser.window_handles[x])
def idIt(element):
    return browser.find_element_by_id(element)

for tabs in range(len(sites)-1):
    newTab(tabs)

windowSwitch(0)
browser.get(sites[0])
officeEmail = idIt('i0116')
officeEmail.send_keys(myAccount + '@transparent.com')
idIt('idSIButton9').click()
delay()
officePass = idIt('i0118')
officePass.send_keys(myPass)
idIt('idSIButton9').click()
delay()
idIt('idBtn_Back').click()

windowSwitch(1)
browser.get(sites[1])
hipEmail = idIt('email')
hipEmail.send_keys(myAccount + '@transparent.com')
hipEmail.submit()
delay()
hipPass = idIt('password')
hipPass.send_keys(myPass)
hipPass.submit()
delay()
chat = browser.find_element_by_link_text('Launch the web app')
chat.click()

windowSwitch(2)
browser.get(sites[2])
jiraEmail = idIt('login-form-username')
jiraEmail.send_keys(myAccount)
jiraPass = idIt('login-form-password')
jiraPass.send_keys(myPass)
jiraPass.submit()

windowSwitch(4)
browser.get(sites[4])

windowSwitch(0)
