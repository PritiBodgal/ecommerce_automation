import pytest

from pages.get_product_count_page import Get_count
from pages.login_page import Login
from pages.search_invalidproduct_page import Invalid_product

#search product and get their count
@pytest.mark.positive
def test_get_count(setup):
    driver=setup
    login_page = Login(driver)

    login_page.perform_login("prachi2200@gmail.com", "Test&1234")

    count = Get_count(driver)
    search_results = count.perform_search("shirt")

    for search_product in search_results:
        print(search_product.text)
        assert "shirt" in search_product.text.lower()

#search invalid product
@pytest.mark.negative
def test_invalid_search(setup):
    driver = setup
    login_page = Login(driver)

    login_page.perform_login("prachi2200@gmail.com", "Test&1234")

    invalid_search = Invalid_product(driver)
    message=invalid_search.perform_invalid_search("Tees43tt")
    assert "your search returned no results" in message.lower()