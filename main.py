from seleniumhandler import SeleniumHandler
from selenium.webdriver.common.by import By
# From selenium.webdriver.common.keys import Keys #Only needed if I want
# to press enter.
import time

my_selenium = SeleniumHandler()
# Create a driver to get URLs and perform other actions
my_selenium.new_driver()
driver = my_selenium.driver
# Driver.maximize_window() Check if needed.

# Getting the url of the mobile search page in twitch.
my_selenium.get("https://m.twitch.tv")

search_button = driver.find_element(
    By.XPATH, '/html/body/div/div/nav/div[2]/a'
)
search_button.click()

search_bar = driver.find_element(
    By.XPATH, '/html/body/div/div/nav/div/div/div[2]/div/div/input'
)
# Typing our search word.
search_bar.send_keys("starcraft II")
time.sleep(5)

# Finding the element of the first search result.
search_result = driver.find_element(
    By.XPATH, '//*[@id="__next"]/div/main/div/div/ul/li[1]/a/div/p'
)
search_result.click()
# search_bar.send_keys(Keys.RETURN)

# Waits 10 seconds or until all scripts are done running
time.sleep(10)

