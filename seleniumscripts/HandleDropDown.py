from selenium import webdriver
#from selenium.webdriver.chrome import ChromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

#Using the dropdown box and Select Tag

driver=webdriver.Chrome(executable_path="C:\\Users\\murod\\Desktop\\JAVA\\ChromeDriver\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH, "//a[text()='Create New Account']").click()
time.sleep(3)

monthFinder=driver.find_element(By.ID, "month")
dayFinder=driver.find_element(By.ID, "day")
monthDD=Select(monthFinder)
dayDD=Select(dayFinder)
yearFinder=driver.find_element(By.ID, "year")
yearDD=Select(yearFinder)

time.sleep(3)
#January
monthDD.select_by_index(1)
time.sleep(3)

#19
dayDD.select_by_value('19')
time.sleep(3)

#1999
yearDD.select_by_visible_text("1999")

