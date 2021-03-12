from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com/")
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//input[@name='q']").send_keys("Murodjon")
listElements=driver.find_elements(By.XPATH, "//li[@role= 'presentation']//div[@class='sbtc']//span")

print("Total suggestions are: ", len(listElements))
for ele in listElements:
    print("Suggestions are ", ele.text)
    if ele.text=='Murodjon':
        print("Record found")
        ele.click()
        break

