from pages.signup_page import Signup

def test_signup(setup):
    driver = setup
    signup_page = Signup(driver)
    signup_page.perform_signup("prachi", "bodgal", "prachi6200@gmail.com", "Test&1234", "Test&1234")
    assert "My Account" in driver.title
