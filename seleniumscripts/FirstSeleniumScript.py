from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\murod\\Desktop\\JAVA\\ChromeDriver\\chromedriver.exe")
print(type(driver))
driver.get("http://www.google.com")
myPageTitle=driver.title
print(myPageTitle)
assert "Google" in myPageTitle

#print(driver.quit())
driver.quit()