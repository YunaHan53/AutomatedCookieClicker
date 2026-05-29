from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
import schedule

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the Cookie Clicker page & maximize window
driver.get("https://ozh.github.io/cookieclicker/")
driver.set_window_position(2568, 722)
driver.maximize_window()
time.sleep(1)

# Find and select English language prompted
language_selection = driver.find_element(By.CSS_SELECTOR, "#langSelect-EN")
language_selection.click()
time.sleep(1)

# Set the end time
end = datetime.now() + timedelta(minutes=5)
end_time = end.strftime("%Y-%m-%d %H:%M:%S")

# Find the big cookie
big_cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")

# Find the number of cookies
cookies_per_sec = driver.find_element(By.ID, "cookiesPerSecond")

# Functions
def click_big_cookie():
    big_cookie.click()
    time.sleep(0.05)

def check_upgrades():
    print("Checking upgrades...")
    available_upgrades = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    item_ids = [item.get_attribute("id") for item in available_upgrades]
    print(item_ids)

    for item_id in item_ids:
        try:
            driver.find_element(By.ID, item_id).click()
            print(f"{item_id} upgraded")
            time.sleep(1)
        except Exception as e:
            print(f"Could not find {item_id}. {e}")


# Schedule a check every 30 seconds
schedule.every(30).seconds.do(check_upgrades)

# Keep it running until end
while datetime.now() < end:
    schedule.run_pending()
    click_big_cookie()

print(f"Done - 5 minutes passed. Cookies/second: {cookies_per_sec.text}")
# driver.quit()