from seleniumhandler import SeleniumHandler
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

my_selenium = SeleniumHandler()
# create a driver to get URLs and perform other actions
my_selenium.new_driver()
driver = my_selenium.driver
# driver.maximize_window() Check if needed.

# getting the url of the mobile search page in twitch.
my_selenium.get("https://m.twitch.tv")

search_button = driver.find_element(
    By.XPATH, '/html/body/div/div/nav/div[2]/a'
)
search_button.click()

search_bar = driver.find_element(
    By.XPATH, '/html/body/div/div/nav/div/div/div[2]/div/div/input'
)
# typing our search word.
search_bar.send_keys("starcraft II")
search_bar.send_keys(Keys.RETURN)

# finding the element of the first search result.
search_result = driver.find_element(
    By.XPATH, '//*[@id="__next"]/div/main/div/div/ul/li[1]/a/div/p'
)
search_result.click()

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
