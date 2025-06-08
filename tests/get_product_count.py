from selenium import webdriver
from pages.login_page import Login
from pages.get_product_count_page import Get_count

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.maximize_window()

    login_page = Login(driver)

    login_page.perform_login("prachi2200@gmail.com", "Test&1234")

    count=Get_count(driver)
    search_results=count.perform_search("shirt")

    for search_product in search_results:
        print(search_product.text)

    driver.quit()


