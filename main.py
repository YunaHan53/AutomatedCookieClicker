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
end_time = datetime.now() + timedelta(minutes=5)

# Find the big cookie
big_cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")

# Functions
def click_big_cookie():
    big_cookie.click()
    time.sleep(0.05)

def check_upgrades():
    print("Checking upgrades...")
    available_upgrades = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

    if not available_upgrades:
        print("No upgrade available")
        return

    most_expensive = available_upgrades[-1]
    item_id = most_expensive.get_attribute("id")

    try:
        most_expensive.click()
        print(f"{item_id} upgraded")
    except Exception as e:
        print(f"Could not find {item_id}. {e}")


# Schedule a check every 5 seconds
schedule.every(5).seconds.do(check_upgrades)

# Keep it running until end
while datetime.now() < end_time:
    schedule.run_pending()
    click_big_cookie()

# Find the number of cookies/second
cookies_data = driver.find_element(By.ID, "cookies").text.split(" ")
cookies_per_sec = cookies_data[-1]
print(f"Done - 5 minutes passed. Cookies/second: {cookies_per_sec}")
# driver.quit()