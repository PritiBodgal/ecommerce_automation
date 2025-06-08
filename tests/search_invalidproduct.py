from selenium import webdriver
from pages.login_page import Login
from pages.search_invalidproduct_page import Invalid_product

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.maximize_window()

    login_page = Login(driver)

    login_page.perform_login("prachi2200@gmail.com", "Test&1234")

    invalid_search=Invalid_product(driver)
    invalid_search.perform_invalid_search("Tees43tt")