from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace these with your Instagram credentials
USERNAME = ''
PASSWORD = ''

# List of Instagram profiles to follow
profiles_to_follow = [
    "https://www.instagram.com/kunsharora912/"
]

def login_instagram(driver, username, password):
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(3)  # Wait for the login page to load

    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for the login to complete

def follow_profiles(driver, profiles):
    for profile in profiles:
        driver.get(profile)
        time.sleep(3)  # Wait for the profile page to load

        try:
            # Locate the follow button using a more specific class name from the provided HTML
            follow_button = driver.find_element(By.XPATH, '//button[contains(@class, "_acan") and .//div[contains(text(), "Follow")]]')
            follow_button.click()
            time.sleep(2)  # Wait for the action to complete
        except Exception as e:
            print(f"Could not follow {profile}: {e}")

def main():
    driver_path = ''  # Adjust the path to your chromedriver
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--disable-gpu')  # Applicable to windows os only
    options.add_argument('--window-size=1920x1080')
    # Ensure the Chrome binary path is set correctly
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Adjust to your actual Chrome path

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        login_instagram(driver, USERNAME, PASSWORD)
        follow_profiles(driver, profiles_to_follow)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
