from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Simple Calendar Handler with Blogspot example



driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.implicitly_wait(10)
driver.find_element(By.ID, "datepicker").click()
#driver.find_element(By.XPATH, "//a[text()='23']").click()

allDates=driver.find_elements(By.XPATH, "//table[@class ='ui-datepicker-calendar']//a")

for dateElement in allDates:
    date=dateElement.text
    print(date)
    if date=='23':
        dateElement.click()
        break







