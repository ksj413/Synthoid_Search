from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
import time
import random
import selenium.webdriver.support.ui as ui
def search(parameter):
	browser=webdriver.Firefox()
	browser.get("http://www.google.com/")
	for p in range(0,6):
		#text_box=browser.find_element_by_id('gbqfq')
		#text_box.send_keys("cats")
		#button=browser.find_element_by_id('gbqfb');
		#button.click()
		browser.get("https://www.google.com/#q="+parameter[p])
		time.sleep(6)
	browser.close()

if __name__=="__main__":
	parameter=['dogs','cats','cars','trains','ships','Chicago', 'Paris]
	search(parameter)
