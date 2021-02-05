from selenium import webdriver

# opens a play-list link on browser
url="https://www.youtube.com/playlist?list=PLx65qkgCWNJIs3FPaj8JZhduXSpQ_ZfvL"
browser = webdriver.Chrome()
browser.get(url)

# playing the play-list
play=browser.find_element_by_class_name('style-scope ytd-playlist-thumbnail')
play.click()