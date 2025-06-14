import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Delete:
    def __init__(self,driver):
        self.driver= driver
        self.locator={
            'delete':'//*[@id="mini-cart"]/li/div/div/div[3]/div[2]/a',
            'button':'/html/body/div[4]/aside[2]/div[2]/footer/button[2]',
            'message':'//*[@id="ui-id-1"]'

        }
    def delete_product(self):
        self.driver.find_element(By.XPATH,self.locator['delete']).click()
        yes_button=WebDriverWait(self.driver,50).until(EC.element_to_be_clickable((By.XPATH,self.locator['button'])))
        yes_button.click()

        message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.locator['message'])))
        print(message.text)
        