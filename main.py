from seleniumhandler import SeleniumHandler
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

my_selenium = SeleniumHandler()
# create a driver to get URLs and perform other actions
driver = my_selenium.new_driver()
# driver.maximize_window() Check if needed.

# get a URL
my_selenium.get("https://www.twitch.tv")

# find an element
# link: https://selenium-python.readthedocs.io/locating-elements.html
search_bar = driver.find_element(By.XPATH, "//input[@class='gLFyf']")
search_bar.send_keys("This search was done by a Selenium Script")
# also if it is a button you can do
# element.click()
search_bar.send_keys(Keys.RETURN)

# allow time for dynamic elements to load
# this just waits a max of 10 seconds or until all scripts are done running
driver.implicitly_wait(10)
# I've also found that a time.sleep() works well here
# uncomment if results are not what is expected
time.sleep(2)

# function packaged into get_html() in seleniumhandler
# takes in a URL and returns the page's source (HTML)
# usage: html = get_html("https://google.com", driver)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

first_result = soup.find("h3", {"class": "LC20lb MBeuO DKV0Md"})
print("First result: '" + first_result.get_text() + "'")

# text = soup.get_text()
# print("All text:")
# print(text)
