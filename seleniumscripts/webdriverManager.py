from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/")
driver.find_element(By.NAME, "q").send_keys("Murodjoni Sharifzoda")
#driver.quit()

