from selenium import webdriver
from selenium.webdriver.common.by import By
import time,math

link='http://suninjuly.github.io/redirect_accept.html'
def calc(x : int):
    return math.log(abs(12*math.sin(int(x))))
try:
    browser=webdriver.Firefox()
    browser.get(link)

    button=browser.find_element(By.TAG_NAME,'button')
    button.click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)
    x=browser.find_element(By.ID,'input_value')
    x=x.text
    input1=browser.find_element(By.ID,'answer')
    input1.send_keys(calc(int(x)))
    button=browser.find_element(By.TAG_NAME,'button')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
