from selenium.webdriver.common.by import By

class Login:
    def __init__(self,driver):
        self.driver=driver
        self.locator={
            "email":'//*[@id="email"]',
            "password":'//*[@id="pass"]',
            "submit":'//*[@id="send2"]'
        }

    def perform_login(self,email,password):
        self.driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer/"
           "aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9jdXN0b21lci9hY2NvdW50L2NyZWF0ZS8%2C/")
        self.driver.find_element(By.XPATH,self.locator['email']).send_keys(email)
        self.driver.find_element(By.XPATH,self.locator['password']).send_keys(password)
        self.driver.find_element(By.XPATH,self.locator['submit']).click()