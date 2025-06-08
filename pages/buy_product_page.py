import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Buy_product():
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.locator = {
            'dropdown': '//*[@id="ui-id-4"]',
            'tops': '//*[@id="ui-id-9"]',
            'jacket': '//*[@id="ui-id-11"]',
            'product': '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div',
            'add_cart': '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[3]/div/div[1]/form/button',
            'select_size': '//*[@id="option-label-size-143-item-169"]',
            'color': '//*[@id="option-label-color-93-item-57"]',
            'submit': '//*[@id="product-addtocart-button"]',
            'checkout_button': '//*[@id="top-cart-btn-checkout"]',
            'address': '//input[@name="street[0]"]',
            'city': '//input[@name="city"]',
            'state': '//select[@name="region_id"]',
            'zip': '//input[@name="postcode"]',
            'country': '//select[@name="country_id"]',
            'phone_no': '//input[@name="telephone"]',
            'shipping_method': '//*[@id="checkout-shipping-method-load"]/table/tbody/tr[1]/td[1]',
            'button': '//*[@id="shipping-method-buttons-container"]/div/button',
            'order': '//*[@id="checkout-payment-method-load"]/div/div/div[2]/div[2]/div[4]/div/button'
        }

    def perform_buy_product(self):
        dropdown_hover = self.driver.find_element(By.XPATH, self.locator['dropdown'])
        self.actions.move_to_element(dropdown_hover).perform()
        time.sleep(0.5)
        tops = self.driver.find_element(By.XPATH, self.locator['tops'])
        self.actions.move_to_element(tops).perform()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.locator['jacket']).click()

    def add_cart(self):
        self.driver.find_element(By.XPATH, self.locator['product']).click()

        # Wait for size option and click
        size = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.locator['select_size']))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", size)
        size.click()

        # Wait for color option and click
        color = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.locator['color']))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", color)
        color.click()

        # Click Add to Cart button
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator['submit']))
        ).click()

        # Open cart
        self.driver.execute_script("window.scrollTo(0, 0);")
        cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".action.showcart"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cart_button)
        cart_button.click()

    def checkout(self, address, city, zip, phone_no):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator['checkout_button']))
        ).click()

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.locator['address']))
        )

        self.driver.find_element(By.XPATH, self.locator['address']).send_keys(address)
        self.driver.find_element(By.XPATH, self.locator['city']).send_keys(city)

        #state = self.driver.find_element(By.XPATH, self.locator['state'])
       # Select(state).select_by_index(4)

        self.driver.find_element(By.XPATH, self.locator['zip']).send_keys(zip)

        country = self.driver.find_element(By.XPATH, self.locator['country'])
        Select(country).select_by_index(3)

        self.driver.find_element(By.XPATH, self.locator['phone_no']).send_keys(phone_no)

        time.sleep(5)
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator['shipping_method']))
        ).click()

        time.sleep(0.5)

        button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator['button']))
        )
        self.driver.execute_script("arguments[0].click();", button)

        order_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.locator['order']))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_button)
        time.sleep(1)  # Optional wait for stability
        order_button.click()


