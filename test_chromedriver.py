import os
from selenium import webdriver

try:
    chromedriver_path = os.environ.get('CHROMEDRIVER_PATH', None)
    os.environ['webdriver.chrome.driver'] = chromedriver_path
    driver = webdriver.Chrome()
    print("ChromeDriver launched successfully!")
    driver.quit()
except Exception as e:
    print("Failed to launch ChromeDriver:", str(e))
