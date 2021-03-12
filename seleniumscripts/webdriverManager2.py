from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://www.facebook.com/")
#driver.find_element(By.NAME, "q").send_keys("Murodjoni Sharifzoda")
#driver.quit()

