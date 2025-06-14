from selenium import webdriver
from pages.login_page import Login
from pages.buy_product_page import Buy_product
from pages.delete_product_page import Delete

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.maximize_window()

    login_page = Login(driver)

    login_page.perform_login("prachi02200@gmail.com", "Test&1234")

    buy=Buy_product(driver)
    buy.perform_buy_product()
    buy.add_cart()

    product_delete = Delete(driver)
    product_delete.delete_product()

    driver.quit()