from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import validators

def take_screenshot(url, output_path="screenshot.png", resolution=(1920, 1080)):
    """Takes a screenshot of the webpage at a specific resolution."""
    
    # Configure Selenium Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless mode (no visible browser window)
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-features=NetworkService,NetworkServiceInProcess")
    chrome_options.add_argument(f"--window-size={resolution[0]},{resolution[1]}")  # Set window size

    # Specify the ChromeDriver path explicitly
    service = Service("chromedriver")  # Adjust if stored elsewhere
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        print(f"Loading webpage: {url}")
        driver.get(url)
        time.sleep(3)  # Wait for the page to fully load

        # Remove cookie banners
        driver.execute_script("document.querySelectorAll('[id*=cookie], [class*=cookie]').forEach(el => el.remove());")

        # Take a screenshot
        driver.save_screenshot(output_path)
        print(f"Screenshot saved: {output_path} ({resolution[0]}x{resolution[1]})")

    finally:
        driver.quit()

# User input with validation
url = input("Enter the URL: ") or "https://www.google.com"
while not validators.url(url):
    print("❌ Invalid URL! Please enter a valid URL.")
    url = input("Enter the URL: ")

width = input("Enter width (e.g., 1920): ") or "1920"
height = input("Enter height (e.g., 1080): ") or "1080"

# Convert to integer
try:
    width = int(width)
    height = int(height)
except ValueError:
    print("❌ Invalid input for width or height! Default values (1920x1080) will be used.")
    width, height = 1920, 1080

# Capture screenshot
take_screenshot(url, "screenshot.png", (width, height))
