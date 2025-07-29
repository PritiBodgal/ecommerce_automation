from pages.login_page import Login

def test_login(setup):
    driver = setup
    login_page = Login(driver)

    login_page.perform_login("prachi2200@gmail.com", "Test&1234")
    assert "My Account" in driver.title

def test_invalid_login(setup):
    driver=setup
    login=Login(driver)
    login.perform_login("test111@gmai.com","Test&1234")
    message=login.invalid_message()
    expected="The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
    assert expected in message , "Invalid login message not displayed correctly"
