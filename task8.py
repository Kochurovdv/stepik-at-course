from selenium import webdriver
import time 
import math

link = " http://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option2 = browser.find_element_by_id("robotCheckbox")
    option2.click()
    option3 = browser.find_element_by_css_selector("[for='robotsRule']")
    option3.click()
   
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    
finally:
    time.sleep(30)
    browser.quit()
    
    
