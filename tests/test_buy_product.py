from pages.login_page import Login
from pages.buy_product_page import Buy_product

def test_buy_product(setup):
    driver=setup
    login_page = Login(driver)

    login_page.perform_login("prachi6200@gmail.com", "Test&1234")

    buy = Buy_product(driver)
    buy.perform_buy_product()
    buy.add_cart()
    buy.checkout("street2", "ahmedabad", "33433", "77423482343")
