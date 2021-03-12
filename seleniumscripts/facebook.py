from selenium import webdriver
#from selenium.webdriver.chrome import ChromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome(executable_path="C:\\Users\\murod\\Desktop\\JAVA\\ChromeDriver\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//a[text()='Create New Account']").click()
#time.sleep(3)
driver.find_element(By.NAME, "firstname").send_keys("Murodjoni")
driver.find_element(By.NAME, "lastname").send_keys("Sharifzoda")
driver.find_element(By.NAME, "reg_email__").send_keys("myEmail@gmail.com")
driver.find_element(By.NAME, "reg_email_confirmation__").send_keys("myEmail@gmail.com")
driver.find_element(By.ID, "password_step_input").send_keys("555555555")
selMonth=Select(driver.find_element(By.XPATH, "//select[@title='Month']"))
selMonth.select_by_visible_text("Nov")
selDay=Select(driver.find_element(By.XPATH, "//select[@title='Day']"))
selDay.select_by_visible_text("10")
selYear=Select(driver.find_element(By.NAME, "birthday_year"))
selYear.select_by_visible_text("1995")
driver.find_element(By.XPATH, "//label[text()='Male']").click()
driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()


