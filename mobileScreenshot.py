from seleniumhandler import SeleniumHandler
from selenium.webdriver.common.by import By
import time

def main() -> None:
    my_selenium = SeleniumHandler()
    # Create a driver to get URLs and perform other actions.
    my_selenium.new_driver()
    driver = my_selenium.driver
    # Driver.maximize_window() Check if needed.
    
    # Getting the url of the mobile search page in twitch.
    url = "https://m.twitch.tv"
    my_selenium.get(url)
    
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
    time.sleep(1)
    
    #Scroll down 2 times.
    driver.execute_script("window.scrollBy(0, 300)", "")
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, 300)", "")
    time.sleep(1)
    
    third_streamer = driver.find_element(
        By.XPATH, 
        "/html/body/div/div/main/div[2]/div/div/div[3]/" +
        "div/article/a/div/div[1]/img"
    )
    third_streamer.click()
    time.sleep(10)
    driver.get_screenshot_as_file("Screenshot_with_selenium.png")
    print("Screenshot taken.")


if __name__ == "__main__":
    main()