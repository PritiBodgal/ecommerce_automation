from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Get_count():
    def __init__(self,driver):
        self.driver=driver
        self.locator={
            "search":'//*[@id="search"]',
            "search_result":'/html[1]/body[1]/div[2]/header[1]/div[2]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/ul[1]/li',
        }

    def perform_search(self,search):
        WebDriverWait(self.driver,30).until(EC.presence_of_element_located((
                            By.XPATH,self.locator['search']))).send_keys(search)

        results= WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.locator['search_result']))
        )
        return results

