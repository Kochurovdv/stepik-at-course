from selenium import webdriver
import time 

link = "https://www.degreesymbol.net"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_link_text("» Degree symbol examples")
    input2 = browser.find_element_by_partial_link_text("examples")

finally:
    time.sleep(30)
    browser.quit()