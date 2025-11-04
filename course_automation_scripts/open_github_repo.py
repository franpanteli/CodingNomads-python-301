from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # optional: start maximized

# Initialize Chrome session (Selenium will handle ChromeDriver automatically)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the GitHub repository
url = "https://github.com/franpanteli/CodingNomads-python-301"
driver.get(url)

# Wait for a few seconds to see the page
time.sleep(10)

# Close the browser
driver.quit()