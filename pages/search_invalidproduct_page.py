from selenium.webdriver.common.by import By

class Invalid_product():
    def __init__(self,driver):
        self.driver=driver
        self.locator={
            "search":'//*[@id="search"]',
            "submit":'//*[@id="search_mini_form"]/div[2]/button',
            "error":'//*[@id="maincontent"]/div[3]/div[1]/div[2]/div'
        }

    def perform_invalid_search(self,search):
        self.driver.find_element(By.XPATH,self.locator['search']).send_keys(search)
        self.driver.find_element(By.XPATH,self.locator['submit']).click()
        error_message=self.driver.find_element(By.XPATH,self.locator['error'])
        print(error_message.text)