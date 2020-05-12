from selenium import webdriver

browser=webdriver.Chrome("s:/whats app automation/chromedriver")

browser.get("https://www.selenium.dev/")

download=browser.find_element_by_link_text("Downloads")
download.click()

search=browser.find_element_by_id("gsc-i-id1")
search.send_keys("Downloads")

###whatsapp automation

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser=webdriver.Chrome("s:/whats app automation/chromedriver")
browser.get("https://web.whatsapp.com/")
wait= WebDriverWait(browser,600)

target='"Sandhya"'
file_path=input("Enter the file path")
string = "Hello Sandhya madam"
x_arg='//span[contains(@title,' + target +')]'
target=wait.until(ec.presence_of_element_located((By.XPATH,x_arg)))
target.click()

input_box=browser.find_element_by_class_name('_1Plpp')
for i in range(20):
    input_box.send_keys(string + Keys.ENTER)

attachment_section=browser.find_element_by_xpath('//div[@title="Attach"]')
attachment_section=click()

image_box=browser.find_element_by_xpath('//input[@<input accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(file_path)

sleep(3)

send_button=browser.find_element_by_xpath('//span[@data-icon="send-light"]')
send_button.click()
