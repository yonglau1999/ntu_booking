from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta
from time import sleep
import time
import sys
import pyautogui  # Import pyautogui for screen clicks


def wait_for_midnight():
    print("Waiting for 12:00 AM...")
    while True:
        current_time = datetime.now().time()  # Get the current time
        print(current_time)
        # If it's midnight (00:00:00), break the loop and continue
        if current_time.hour == 0 and current_time.minute == 0:
            print("It's 12:00 AM. Starting automation.")
            break
        # Wait for 10 seconds before checking again
        time.sleep(0.1)

wait_for_midnight()

target_date = datetime.now() + timedelta(days=7)
formatted_date = target_date.strftime("%d-%b-%Y")

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation", 'enable-logging'])

# Path to your Chrome user data directory
options.add_argument("user-data-dir=C:/Users/lauyo/AppData/Local/Google/Chrome/User Data")
# # # Name of the profile directory you want to use
options.add_argument("profile-directory=Default")

options.add_argument("--no-sandbox") #bypass OS security model
options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


key = {}

TIMEOUT = 60

def init():
    with open('config.txt') as f:
        for line in f:
            if line != "\n":
                (k, val) = line.split("=", 1)
                key[k.strip()] = val.strip()

def clicker():
    try:
        driver = webdriver.Chrome(executable_path=key.get('DRIVE'), options=options)
        driver.get('https://ntu.facilitiesbooking.com/login.aspx')

        # Log in with Microsoft using the unique id
        login_button = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.ID, "link_azure")))
        login_button.click()
        sleep(1)
        driver.get("https://ntu.facilitiesbooking.com/quick.aspx")


        # Assuming manual login or additional Selenium steps for login

        # Wait for page to load after login

        # Select filters


        date_input = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txt_startDate")))
        
        driver.execute_script("arguments[0].setAttribute('value', arguments[1]);", date_input, formatted_date)
        driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_input)

        category_dropdown = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_ddl_category")))
        select_category = Select(category_dropdown)
        select_category.select_by_value("224")  # Value for "Sports - Racket Sports"

        location_dropdown = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_ddl_location")))
        select_location = Select(location_dropdown)
        select_location.select_by_value("119")  # Value for "North Hill"

        date_input = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_txt_startDate")))

        # Choose time slot
        x_coord = 923  # Example X coordinate (replace with actual)
        y_coord = 620  # Example Y coordinate (replace with actual)

        pyautogui.moveTo(x_coord, y_coord)  # Move the mouse to the coordinates
        pyautogui.click()  # Click at the specified position

        sleep(10)
        # Input reason to play

        x_coord = 780 # Example X coordinate (replace with actual)
        y_coord = 253  # Example Y coordinate (replace with actual)
        pyautogui.moveTo(x_coord, y_coord)
        sleep(2)
        pyautogui.click()
        pyautogui.write(("Play"), interval=0.05)

        # Check the acknowledge terms and conditions box
        x_coord = 565 # Example X coordinate (replace with actual)
        y_coord = 871  # Example Y coordinate (replace with actual)

        pyautogui.moveTo(x_coord, y_coord)
        sleep(2)
        pyautogui.click()
        
        x_coord = 1352 # Example X coordinate (replace with actual)
        y_coord = 968  # Example Y coordinate (replace with actual)
        pyautogui.moveTo(x_coord, y_coord)
        pyautogui.click()
        
        print('Booking attempt complete!')

    except Exception as e:
        print("ERROR: " + str(e))

    finally:
        driver.quit()

if __name__ == "__main__":
    init()
    if len(sys.argv) >= 2:
        if sys.argv == "-bg":
           options.add_argument("--headless")
    clicker()