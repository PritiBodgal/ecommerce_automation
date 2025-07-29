from pages.login_page import Login
from pages.get_product_details_page import Product_details

def test_product_details(setup):
    driver=setup
    login_page = Login(driver)

    login_page.perform_login("prachi2200@gmail.com", "Test&1234")

    product_details = Product_details(driver)
    verify_product = product_details.perform_get_details("Tees")

    for i in verify_product:
        print("Product is below\n", i.text)