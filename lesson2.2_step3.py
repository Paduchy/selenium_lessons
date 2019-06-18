from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x1 = browser.find_element_by_id("num1").text
x2 = browser.find_element_by_id("num2").text
x_sum = str(int(x1) + int(x2))

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(x_sum)

button = browser.find_element_by_class_name("btn-default").click()