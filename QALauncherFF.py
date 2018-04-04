from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time, getpass


myAccount = input('Account: ')
myPass = getpass.getpass('Password: ')
browser = webdriver.Firefox()
sites = ['site1', 'site2', 'site3', 'site4']

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
Email0 = idIt('email')
Email0.send_keys(myAccount + '@test.com')
idIt('test').click()
delay()
Pass0 = idIt('password')
Pass0.send_keys(myPass)
idIt('idSIButton9').click()
delay()
idIt('idBtn_Back').click()

windowSwitch(1)
browser.get(sites[1])
Email1 = idIt('email')
Email1.send_keys(myAccount + '@test.com')
Email1.submit()
delay()
Pass1 = idIt('password')
Pass1.send_keys(myPass)
Pass1.submit()
delay()
chat = browser.find_element_by_link_text('Launch this link')
chat.click()

windowSwitch(2)
browser.get(sites[2])
Email2 = idIt('email')
Email2.send_keys(myAccount)
Pass2 = idIt('password')
Pass2.send_keys(myPass)
Pass2.submit()

windowSwitch(3)
browser.get(sites[3])

windowSwitch(4)
browser.get(sites[4])

windowSwitch(0)
