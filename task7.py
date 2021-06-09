from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//div//div[@class="first_block"]//input[@class="form-control first"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//div//div[@class="first_block"]//input[@class="form-control second"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//div//div[@class="first_block"]//input[@class="form-control third"]')
    input3.send_keys("Smolensk@ya.ru")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()