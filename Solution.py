from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def buildDriver():
    options = ChromeOptions()
    options.add_argument('--profile-directory=Default')
    options.add_argument('--user-data-dir="C:/Temp/ChromeProfile"')
    browser = webdriver.Chrome(chrome_options=options)


driver = buildDriver()

driver.get('https://web.whatsapp.com') 

name = input("Enter name of contact : ")
message = input("Enter message to send : ")

user = driver.find_elements_by_xpath('//span[@title = "{}"]'.format(name))
choice = 1
if len(user) > 1:
    for i in range(len(user)):
        print(i+1+". "+user[i]+'\n')
    choice = input("Which one? Type the serial number.")
user[choice-1].click()

box = driver.find_element_by_class_name('_2S1VP')
box.send_keys(message)
send_button = driver.find_element_by_class_name('_35EW6')
send_button.click()

