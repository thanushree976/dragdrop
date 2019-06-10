import time

from selenium import webdriver

driver = webdriver.Chrome("C:/Users/dell/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://phptravels.com/")
time.sleep(10)
driver.find_element_by_xpath("//span[text()='Login']").click()

print("current window",driver.current_window_handle)
c_w = driver.current_window_handle
w_n = driver.window_handles

for i in  w_n:
    if i!=c_w:
        driver.switch_to.window(i)
        driver.find_element_by_id("inputEmail").send_keys("testmail")
        driver.quit()


webdriver