from selenium.webdriver.common.by import By

class Signup:
    def __init__(self,driver):
        self.driver=driver
        self.locator={
            "first_name":'firstname',
            "last_name":'lastname',
            "email":'email_address',
            "password":'password',
            "confirm_pass":'password-confirmation',
            "submit":'/html[1]/body[1]/div[2]/main[1]/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]/span[1]'
        }

    def perform_signup(self,first_name,last_name,email,password,confirm_pass):
        self.driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
        self.driver.find_element(By.ID,self.locator['first_name']).send_keys(first_name)
        self.driver.find_element(By.ID,self.locator['last_name']).send_keys(last_name)
        self.driver.find_element(By.ID,self.locator['email']).send_keys(email)
        self.driver.find_element(By.ID,self.locator['password']).send_keys(password)
        self.driver.find_element(By.ID,self.locator['confirm_pass']).send_keys(confirm_pass)
        self.driver.find_element(By.XPATH,self.locator['submit']).click()