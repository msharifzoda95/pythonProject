from selenium import webdriver
#from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(executable_path="C:\\Users\\murod\\Desktop\\JAVA\\ChromeDriver\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.ziprecruiter.com/login?realm=candidates")

username=driver.find_element_by_name("email")

enableStatus=username.is_enabled()

displayStatus=username.is_displayed()

print(enableStatus)
print(displayStatus)

username.clear()

attrType=username.get_attribute("type")

paddingData=username.value_of_css_property("padding")

print(attrType)
print(paddingData)

username.send_keys("murodjoni@aol.com")

password=driver.find_element_by_name("password")
password.send_keys("NGg7GDJbT6CC")

loginButton=driver.find_element_by_class_name("btn")
loginButton.click()

driver.quit()