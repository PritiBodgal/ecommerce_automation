from selenium import webdriver
from pages.signup_page import Signup

if __name__ == "__main__":
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    signup_page=Signup(driver)
    signup_page.perform_signup("prachi","bodgal","prachi02200@gmail.com","Test&1234","Test&1234")

    driver.quit()