# %%
from selenium import webdriver as wd # selenium to webscrape the websites and input neccessary information
import chromedriver_binary # I used the chrome browser driver however their is multiple drivers available 
# Newest version of chromedriver did not work you must rollback the driver for it to work
import random # randomly generate time intervals to try and fool bot prevention
import time # Need to use the time module in order to have a implicit wait timer or you will get banned from the websites due to bot prevention.


# %%
wd = wd.Chrome() # If using a different browser you must change this to wd = wd.browser where browser is the name of the driver
wd.implicitly_wait(10) # wait time to open browser 

# %%
wd.get("https://www.bestbuy.com/site/microsoft-xbox-series-s-512-gb-all-digital-console-disc-free-gaming-white/6430277.p?skuId=6430277") # website for the product you want to try and buy

# %%

random_wait_time = random.randrange(5.0, 15.0) # wait time range
print(random_wait_time)
time.sleep(random_wait_time) 

add_to_cart_button = wd.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[14]/div[2]/div/div/div/button') # must use the full Xpath on the site of the product you want to add to cart
add_to_cart_button.click() # selenium to add to cart

# %%
random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

go_to_cart = wd.find_element_by_xpath('/html/body/div[8]/div/div[1]/div/div/div/div/div[1]/div[3]/a') # Full xpath for go to cart 
go_to_cart.click() # After product is added to my cart this is to go to cart 

# %%
random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

view_cart_button = wd.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[2]') # Full Xpath for the view cart button 
view_cart_button.click()

# %%
random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

not_interested_button = wd.find_element_by_xpath('//*[@id="Popup_Masks"]/div/div/div[3]/div[2]/button[1]') # This may or may not be needed for the product this was to deny a upsell promotion
not_interested_button.click()

# %%
random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

secure_checkout_button = wd.find_element_by_xpath('//*[@id="app"]/div[1]/section/div/div/form/div[2]/div[3]/div/div/div[3]/div/button') # begin the checkout process 
secure_checkout_button.click()

# %%
random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

guest_checkout_button = wd.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[1]/form[2]/div[2]/div/button') # check out process as a guest this may or may not be needed depending on the site
guest_checkout_button.click()

# %%
random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

add_address = wd.find_element_by_xpath('//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/i') # Adds the address for product shipment
add_address.click()

# %%
# This is the checkout section for the product page
# Before running script manually go through a checkout section on website to make sure these line up with the full XPATH 
# Go through the check out process on an item in stock to make sure the steps line up and their is not any pop ups that happen along the way that you need to bypass

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

first_name = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[1]/input') # First Name
first_name.send_keys("First")

random_wait_time = random.randrange(5.0, 10.0)
print(random_wait_time)
time.sleep(random_wait_time)

last_name = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[2]/input') # Last Name
last_name.send_keys("Last")

random_wait_time = random.randrange(5.0, 10.0)
print(random_wait_time)
time.sleep(random_wait_time)

address_first_line = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[6]/input')
address_first_line.send_keys("First Line")

random_wait_time = random.randrange(5.0, 10.0)
print(random_wait_time)
time.sleep(random_wait_time)

city = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[8]/input')
city.send_keys("City")

random_wait_time = random.randrange(5.0, 10.0)
print(random_wait_time)
time.sleep(random_wait_time)

from selenium.webdriver.support.select import Select
state = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[9]/label[2]/select') # The state selection was a drop down button 
Select(state).select_by_value('State')

random_wait_time = random.randrange(5.0, 10.0)
print(random_wait_time)
time.sleep(random_wait_time)


zip_code = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[10]/input')
zip_code.clear()
zip_code.send_keys("Zip Code")

random_wait_time = random.randrange(5.0, 10.0)
print(random_wait_time)
time.sleep(random_wait_time)

phone_number = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[12]/input')
phone_number.send_keys("phone number") 

random_wait_time = random.randrange(5.0, 10.0)
print(random_wait_time)
time.sleep(random_wait_time)

email = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[15]/input')
email.send_keys("email address")

random_wait_time = random.randrange(5.0, 10.0)
print(random_wait_time)
time.sleep(random_wait_time)

save_button = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[3]/button[2]')
save_button.click()

# %%
# This is the shipping address and billing address section 
# If any of the steps do not work replace the XPath with the Full XPath 
random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

use_address_as_entered = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[3]/button[1]')
use_address_as_entered.click()

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

go_to_delivery_button = wd.find_element_by_xpath('//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[1]/div/div[3]/button')
go_to_delivery_button.click()

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

go_to_payment_page_button = wd.find_element_by_xpath('//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[2]/div/div[3]/button') # 
go_to_payment_page_button.click()

# %%
# This is the part that you put your financial information in so you can  place the order and have it shipped 
# If any of the steps dont work replace the XPath with the Full XPath
random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

cred_or_debit = wd.find_element_by_xpath('//*[@id="optimized-cc-card-number"]') # Repllace the CC Number string with a integer of your CC or Debit card 
cred_or_debit.send_keys("CC NUMBER")

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

from selenium.webdriver.support.select import Select
MM = wd.find_element_by_xpath('//*[@id="credit-card-expiration-month"]/div/div/select') # The Expiration Date selection was a drop down button 
Select(MM).select_by_value(integervalue)

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

from selenium.webdriver.support.select import Select
YYYY = wd.find_element_by_xpath('//*[@id="credit-card-expiration-year"]/div/div/select') # The Year selection was a drop down button 
Select(YYYY).select_by_value(integervalue)

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

seccode = wd.find_element_by_xpath('//*[@id="credit-card-cvv"]') # take out the string and put int a 3 digit integer on the next line for security cody
seccode.send_keys("3 digit integer")

random_wait_time = random.randrange(5.0, 15.0)
print(random_wait_time)
time.sleep(random_wait_time)

Place_Order = wd.find_element_by_xpath('//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[3]/div/section/div[2]/div/div[2]/button')
Place_Order.click()



