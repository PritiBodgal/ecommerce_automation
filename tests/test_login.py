from pages.login_page import Login

def test_login(setup):
    driver = setup
    login_page = Login(driver)

    login_page.perform_login("prachi2200@gmail.com", "Test&1234")
    assert "My Account" in driver.title

