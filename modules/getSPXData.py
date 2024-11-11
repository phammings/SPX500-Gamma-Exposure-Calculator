from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
import time

# Set the path to your ChromeDriver executable
chromedriver_path = 'C:/Program Files/chromedriver-win64/chromedriver.exe'

# Create a Chrome service
chrome_service = ChromeService(executable_path=chromedriver_path)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=chrome_service)

# Open the website
driver.get('https://www.cboe.com/delayed_quotes/spx/quote_table')

try:
    # Wait for the page to be fully loaded
    timeout = 100
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section[1]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[2]')))
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section[1]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[2]')))

    cookies_reject_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/button[2]')
    cookies_reject_btn.click()
    time.sleep(2)

    # Select "All" for expiration
    expiration_select = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[2]')
    expiration_select.click()
    time.sleep(2)
    all_button = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[2]/div/div/div[2]/div/div[1]')
    all_button.click()
    time.sleep(2)

    # Select "All" for options range
    options_range_select = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[2]')
    options_range_select.click()
    time.sleep(2)
    all_button = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div/div[2]/div/div[1]')
    all_button.click()
    time.sleep(2)

    viewAllChain_button = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div[5]/div/button')
    viewAllChain_button.click()
    time.sleep(2)

    # Scroll down to trigger loading of data
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the download button to be clickable
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section[1]/div/div/div/div/div[2]/div[2]/div[3]/div[60]/a')))

    # Click the download button
    download_button = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/div/div/div[2]/div[2]/div[3]/div[60]/a')
    driver.execute_script("arguments[0].click();", download_button)
    time.sleep(2)

except TimeoutException:
    print("Timed out waiting for the page to be fully loaded")

finally:
    # Close the browser window
    driver.quit()
