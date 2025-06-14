from pages.login_page import Login
from pages.reviews_page import Review

def test_review(setup):
    driver = setup
    login_page = Login(driver)

    login_page.perform_login("prachi02200@gmail.com", "Test&1234")

    review = Review(driver)
    review.perform_add_review("jacket is good", "Must Buy")
