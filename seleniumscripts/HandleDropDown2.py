from selenium import webdriver
#from selenium.webdriver.chrome import ChromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

#FACEBOOK Using the dropdown box and Select Tag

driver=webdriver.Chrome(executable_path="C:\\Users\\murod\\Desktop\\JAVA\\ChromeDriver\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH, "//a[text()='Create New Account']").click()
time.sleep(3)

monthFinder=driver.find_element(By.ID, "month")

monthDD=Select(monthFinder)

myList=monthDD.options

firstItem=monthDD.first_selected_option
print("First Option is ", firstItem.text)

assert "Mar"==firstItem.text

print(len(myList))

assert len(myList) == 13

for ele in myList:
    print("Value is ", ele.text)
    if ele.text=="Feb":
        ele.click()
    break
