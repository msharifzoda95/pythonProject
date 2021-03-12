from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Calendar Handler with GoiBibo


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.goibibo.com/")
driver.implicitly_wait(10)

fromWhere=driver.find_element(By.XPATH, "//input[@class='inputSrch']").send_keys("tashkent")
toWhere=driver.find_element(By.XPATH, "//input[@placeholder='Destination']").send_keys("new york")
driver.find_element(By.XPATH, "//input[contains(@id,'departure')]").click()

departure=driver.find_element(By.XPATH, "//div[text()='25']").click()
returning=driver.find_element(By.XPATH, "//input[contains(@id, 'return')]").click()
driver.find_element(By.XPATH, "//div[text()='31']").click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()

#allDates=driver.find_elements(By.XPATH, "//div[@class='calDate']")

#for dateElement in allDates:
 #  date=dateElement.text
  #  print(date)
  #  if date=='31':
   #    dateElement.click()
    #   break







