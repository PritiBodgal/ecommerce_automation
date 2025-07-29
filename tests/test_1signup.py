from pages.signup_page import Signup

def test_signup(setup):
    driver = setup
    signup_page = Signup(driver)
    signup_page.perform_signup("prachi", "bodgal", "prachi6606299900@gmail.com", "Test&1234", "Test&1234")
    assert "My Account" in driver.title

def test_duplicate_signup(setup):
    driver = setup
    signup_page = Signup(driver)
    signup_page.perform_signup("prachi", "bodgal", "prachi660620033@gmail.com", "Test&1234", "Test&1234")
    message=signup_page.same_email_signup()
    expected='There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account.'
    assert expected in message , "Duplicate email error"