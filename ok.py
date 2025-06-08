import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



options=Options()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
actions=ActionChains(driver)

driver.get("https://magento.softwaretestingboard.com/customer/account/login/referer/"
           "aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS9jdXN0b21lci9hY2NvdW50L2NyZWF0ZS8%2C/")

WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="email"]'))).send_keys("prachi2200@gmail.com")

passw=(driver.find_element(By.XPATH,'//*[@id="pass"]')
                                    .send_keys('Test&1234'))
driver.find_element(By.XPATH, '//*[@id="send2"]').click()
print("logged in succesfully")

#hover on dropdown
dropdown_hover=driver.find_element(By.XPATH,'//*[@id="ui-id-4"]')
actions.move_to_element(dropdown_hover).perform()
time.sleep(0.5)

tops=driver.find_element(By.XPATH,'//*[@id="ui-id-9"]')
actions.move_to_element(tops).perform()
time.sleep(0.5)

bags=driver.find_element(By.XPATH,'//*[@id="ui-id-11"]')
bags.click()
print("Clicked on jackets")

#choosing and adding jacket to add to cart
product=driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div')
actions.move_to_element(product).perform()

add_cart=driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[3]/div/div[1]/form/button')
add_cart.click()
time.sleep(2)

select_size=driver.find_element(By.XPATH,'//*[@id="option-label-size-143-item-169"]').click()
color=driver.find_element(By.XPATH,'//*[@id="option-label-color-93-item-57"]').click()
submit=driver.find_element(By.XPATH,'//*[@id="product-addtocart-button"]').click()
time.sleep(5)

#check cart
driver.execute_script("window.scrollTo(0, 0);")  # Scroll to the top

cart_button = driver.find_element(By.CLASS_NAME, 'action.showcart')
driver.execute_script("arguments[0].scrollIntoView(true);", cart_button)
cart_button.click()
path='C://Users//LENOVO//PycharmProjects//demo//screenshots//cart.png'
driver.save_screenshot(path)

#proceed to checkout
checkout_button=driver.find_element(By.ID,'top-cart-btn-checkout').click()
#add details for book order
address=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[2]/form[1]/div[1]/fieldset[1]/div[1]/div[1]/div[1]/input[1]')))
address.send_keys("street2")

city=driver.find_element(By.XPATH,'/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[4]/ol[1]/li[1]/div[2]/form[1]/div[1]/div[4]/div[1]/input[1]').send_keys("Ahmedabad")
state=driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[5]/div/select')
select=Select(state)
select.select_by_index(4)
time.sleep(0.5)
zip=driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[7]/div/input').send_keys("33433")

country=driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[8]/div/select')
select = Select(country)
select.select_by_index(3)
phone_no=driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/form/div/div[9]/div/input').send_keys("77423482343")
time.sleep(3)

WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="checkout-shipping-method-load"]/table/tbody/tr[1]/td[1]'))).click()

WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable(
        (By.XPATH,'//*[@id="shipping-method-buttons-container"]/div/button'))).click()

time.sleep(3)

#payment page
order = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="checkout-payment-method-load"]/div/div/div[2]/div[2]/div[4]/div/button')
    )
)
# Click the element
order.click()


driver.quit()