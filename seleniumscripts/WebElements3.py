from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Working with TAG_NAME

driver=webdriver.Chrome(executable_path="C:\\Users\\murod\\Desktop\\JAVA\\ChromeDriver\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.ziprecruiter.com/login?realm=candidates")

driver.find_element(By.TAG_NAME, "img").click() #This function will click the first image on the page


#forgotLink=driver.find_element(By.LINK_TEXT, "Forgot Password?")
#forgotLink=driver.find_element(By.PARTIAL_LINK_TEXT, "Forgot Password")
#forgotLink.click()

