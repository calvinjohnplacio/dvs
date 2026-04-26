from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  # Automatically install chromedriver

import time

# Set up Chrome options
options = Options()
options.add_argument("--headless")  # Run the browser in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-gpu")
options.add_argument("--disable-software-rasterizer")

# Use webdriver-manager to handle ChromeDriver installation
driver_path = ChromeDriverManager().install()  # Install and get the path of the chromedriver

# Use the Service class to pass the driver path
service = Service(executable_path=driver_path)

# Create the WebDriver instance with the Service and options
driver = webdriver.Chrome(service=service, options=options)  # Use the Service to pass the executable path

try:
    # Open the local file
    driver.get("file://" + "/var/www/html/index.html")

    # Wait for the element to be visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "title"))
    )

    # Fetch the title text
    title = driver.find_element(By.ID, "title").text

    # Assert the title is as expected
    assert title == "Hello CI/CD", f"Expected 'Hello CI/CD' but got '{title}'"

    print(f"Test Passed: Title is '{title}'")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    driver.quit()
