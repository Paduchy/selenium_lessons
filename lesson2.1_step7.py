import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("treasure")
treasure = x_element.get_attribute("valuex")
y = calc(treasure)

input = browser.find_element_by_id("answer")
input.send_keys(y)

option_checked = browser.find_element_by_id("robotCheckbox")
option_checked.click()
option_radio_button = browser.find_element_by_css_selector("[value='robots']")
option_radio_button.click()
button = browser.find_element_by_class_name("btn-default")
button.click()