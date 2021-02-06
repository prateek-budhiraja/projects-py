from selenium import webdriver
from selenium.webdriver.common.keys import Keys

name=None
msg=None
times=None

def usr_input():
    global name, msg, times
    name=input('Enter the contact name: ')
    msg=input('Enter a file name from which messsages would be send: ')
    # msg=input('Enter the message: ')
    # times=int(input('Enter number of times you want to send that message: '))

chrome=webdriver.Chrome()
chrome.get('https://web.whatsapp.com')

usr_input()     #here you will get time to scan the qr code


# if not working, confirm the class name and xpath
search_box=chrome.find_element_by_class_name('_1awRl')
search_box.send_keys(name)
search_box.send_keys(Keys.ENTER)

with open(msg, 'r') as fi:
    msgs=fi.read().split('\n')
    for msgi in msgs:
        msg_box=chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        msg_box.send_keys(msgi+Keys.ENTER)



# for ti in range(0,times):
#     msg_box=chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
#     msg_box.send_keys(msg+Keys.ENTER)