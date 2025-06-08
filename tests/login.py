from selenium import webdriver
from pages.login_page import Login

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.maximize_window()

    login_page=Login(driver)

    login_page.perform_login("prachi2200@gmail.com","Test&1234")

    driver.quit()