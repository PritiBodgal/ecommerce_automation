import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Review():
    def __init__(self,driver):
        self.driver=driver
        self.actions = ActionChains(driver)

        self.locator={
            "dropdown_hover":'//*[@id="ui-id-4"]',
            "product":'//*[@id="ui-id-9"]',
            "product_page":'//*[@id="ui-id-11"]',
            "product_click":'//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/strong/a',
            "add_review":'//*[@id="maincontent"]/div[2]/div/div[1]/div[2]/div/a',
            "rating":'Rating_4',
            "summary":'summary_field',
            "review_field":'review_field',
            "submit":'//*[@id="review-form"]/div/div/button',
            "message":'//*[@id="maincontent"]/div[1]/div[2]/div/div/div'

        }

    def perform_add_review(self,summary,review):
      dropdown_hover=self.driver.find_element(By.XPATH,self.locator['dropdown_hover'])
      self.actions.move_to_element(dropdown_hover).perform()

      product=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.locator['product'])))
      self.actions.move_to_element(product).perform()

      WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.locator['product_page']))).click()

      self.driver.find_element(By.XPATH,self.locator['product_click']).click()

      self.driver.find_element(By.XPATH,self.locator['add_review']).click()
      star_input=WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.ID,self.locator['rating'])))
      self.driver.execute_script("arguments[0].click();", star_input)

      self.driver.find_element(By.ID,self.locator['summary']).send_keys(summary)
      self.driver.find_element(By.ID,self.locator['review_field']).send_keys(review)
      self.driver.find_element(By.XPATH,self.locator['submit']).click()

      msg=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.locator['message'])))
      print(msg.text)





