from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# 1. Open Swiggy
driver.get("https://www.swiggy.com/")

# 2. Click Login (wait for button to be clickable)
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Sign In') or contains(text(),'Login') or contains(text(),'Account')]"))
    )
    login_button.click()
except Exception as e:
    print("Login button not found or clickable:", e)
    driver.quit()
    exit()
time.sleep(2)


# 3. Enter phone number (wait for input)
try:
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='tel' or @id='mobile']"))
    )
    phone_input.send_keys("9381725008")  # 9030366809  8688426259  9032208078 8125476289
    login_after_phone = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='overlay-sidebar-root']/div/div/div[2]/div/div/div/form/div[2]/a"))
    )
    login_after_phone.click()
    print("Clicked login after entering phone number. Please enter OTP manually within 30 seconds...")
    time.sleep(60)
    verify_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='overlay-sidebar-root']/div/div/div[2]/div/div/div/div[2]/form/div[2]/div[2]/a"))
    )
    verify_button.click()
    print("Clicked login/continue after OTP.")
except Exception as e:
    print("Phone input or login button after phone not found or not clickable:", e)
    driver.quit()
    exit()


# 6. Validate Page Title and URL
print("Page Title after login:", driver.title)
print("Current URL after login:", driver.current_url)


# 7. Wait for restaurants page and handle location/address prompt if present
try:
    for _ in range(30): 
        try:
            search_icon = driver.find_element(By.XPATH, "//*[@id='root']/div[1]/header/div/div/ul/li[5]/div/a/span[2]")
            search_icon.click()
            time.sleep(1)
            
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search for restaurants and food']"))
            )
            search_box.clear()
            search_box.send_keys("Dominos")
            time.sleep(2)
            search_box.send_keys(Keys.RETURN)
            time.sleep(3)
            break  
        except Exception:
            pass
        time.sleep(1)
    else:
        print("Search box or restaurant page not found after waiting. Please check if you are logged in and have entered your address.")
        
        driver.save_screenshot("swiggy_debug.png")
        driver.quit()
        exit()
except Exception as e:
    print("Unexpected error after login:", e)
    driver.save_screenshot("swiggy_debug.png")
    driver.quit()
    exit()

# 8. Click on the restaurant (update if needed)
try:
    restaurant = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Domino')]"))
    )
    restaurant.click()
    time.sleep(3)
except Exception as e:
    print("Restaurant not found or not clickable:", e)
    driver.quit()
    exit()

try:
    # 9. Add first item to cart
    add_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[1]/div/div/div/div[2]/div[9]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/button[2]/div"))
    )
    
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_button)
    time.sleep(1)
    try:
        add_button.click()
    except Exception:
        driver.execute_script("arguments[0].click();", add_button)
    time.sleep(5)

    # view cart
    view_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='view-cart-btn']/span/span[2]/span"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", view_cart_button)
    time.sleep(1)
    try:
        view_cart_button.click()
    except Exception:
        driver.execute_script("arguments[0].click();", view_cart_button)
    time.sleep(7)

    # add new address
    address_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div/div/div[2]/div[2]"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", address_button)
    time.sleep(1)
    try:
        address_button.click()
    except Exception:
        driver.execute_script("arguments[0].click();", address_button)
    time.sleep(60) # Wait for manual address entry

    save_address_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='overlay-sidebar-root']/div/div/div[2]/div/div[4]/div/div/a"))
    )
    save_address_button.click()
    time.sleep(2)

    proceed_to_payment_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div[1]/div/div/div[1]/div/div[2]/div/button"))
    )
    proceed_to_payment_button.click()

except Exception as e:
    print("Error adding item to cart or going to checkout:", e)
    driver.save_screenshot("swiggy_debug_add_cart.png")
    driver.quit()
    exit()

print("Automation complete. Review the cart and payment page manually.")

# driver.quit()
