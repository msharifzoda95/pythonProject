from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Working with XPATH and the ASSERT function

driver=webdriver.Chrome(executable_path="C:\\Users\\murod\\Desktop\\JAVA\\ChromeDriver\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.ziprecruiter.com/login?realm=candidates")

#username=driver.find_element_by_name("email")
#username.send_keys("murodjoni@aol.com")

#driver.find_element(By.XPATH, "//input[@name='email']").send_keys(("murodjoni@aol.com"))

#driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("NGg7GDJbT6CC")

#password=driver.find_element_by_name("password")
#password.send_keys("NGg7GDJbT6CC")

driver.find_element(By.XPATH, "//input[@value='Sign In']").click()

privacyBtn = driver.find_element(By.XPATH, "//a[contains(text(), 'Privacy')]")
time.sleep(3)
privacyBtn.click()
print("URL after click is ", driver.current_url)
assert "privacy" in driver.current_url

termsBtn=driver.find_element(By.XPATH, "//a[contains(text(), 'Terms of Use')]")
termsBtn.click()

time.sleep(3)


#loginButton=driver.find_element_by_class_name("btn")
#loginButton.click()
driver.quit()
