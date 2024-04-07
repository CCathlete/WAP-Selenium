from selenium import webdriver
import time

class SeleniumHandler:
    def new_driver(self):
        # We'll use Google Chrome according to the demand.
        mobile_emulation = {"deviceName": "Galaxy Note 3"}
        # We'd like to set the mobile_emulaiton option in our webDriver.
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(
            "mobileEmulation", mobile_emulation)
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(3)
        self.driver = driver

    def scroll_to_bottom(self):
        self.driver.execute_script(
            'window.scrollBy(0,document.body.scrollHeight);')

    def get_html_source(self, url: str):
        self.driver.get(url)
        time.sleep(3)
        return self.driver.page_source

    def get(self, url: str):
        self.driver.get(url)
        time.sleep(3)

    def close_chrome(driver):
        driver.quit()
