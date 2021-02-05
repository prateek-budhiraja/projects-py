# importing webdriver which is neccessary to load the browser
from selenium import webdriver
import time

url="https://www.youtube.com"
searchstring="punjabi music"
driver=webdriver.Chrome() 
driver.get(url)  


search_box=driver.find_element_by_xpath('//*[@id="search"]')
search_box.send_keys(searchstring)

search_btn=driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
search_btn.click()

time.sleep(10)
video=driver.find_element_by_xpath('//*[@id="video-title"]')
video.click()
