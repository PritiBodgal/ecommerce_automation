from selenium.webdriver.common.by import By


class Product_details():
    def __init__(self, driver):
        self.driver = driver
        self.locator = {
            "search": '//*[@id="search"]',
            "submit": '//*[@id="search_mini_form"]/div[2]/button',
            "count": '//*[@id="toolbar-amount"]',
            "product_detail": '//*[@id="maincontent"]/div[3]/div[1]/div[2]/div[2]/ol/li/div'
        }

    def perform_get_details(self, search):
        self.driver.find_element(By.XPATH, self.locator['search']).send_keys(search)
        self.driver.find_element(By.XPATH, self.locator['submit']).click()
        count = self.driver.find_element(By.XPATH, self.locator['count'])
        print(count.text)
        product_details = self.driver.find_elements(By.XPATH, self.locator['product_detail'])
        return product_details
