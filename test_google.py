from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_title():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # Run without opening browser window
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")

    assert "Google" in driver.title  # Assertion = actual "test"

    driver.quit()