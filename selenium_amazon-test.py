from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\WebDriver\\geckodriver.exe")
url = "https://www.amazon.com/"
driver.get(url)

id = "email" # replace with valid e-mail address
pw = "password" # replace with valid password
item = "item" # item to search

xpaths = {'id':"//input[@name='email']", 'pw':"//input[@name='password']", 'item':"//input[@name='field-keywords']"}

#Login
driver.find_element_by_id('nav-link-accountList').click()

driver.find_element_by_xpath(xpaths['id']).send_keys(id)
driver.find_element_by_xpath(xpaths['pw']).send_keys(pw)

#Search
driver.find_element_by_css_selector("input[type=\"submit\"]").click()

driver.find_element_by_xpath(xpaths["item"]).send_keys(item)
driver.find_element_by_css_selector("input[type=\"submit\"]").click()

#Select & Check the Cart
driver.find_element_by_css_selector('img.s-access-image.cfMarker').click()
driver.find_element_by_css_selector("input[id=\'add-to-cart-button\']").click()
driver.find_element_by_css_selector('a#hlb-view-cart-announce.a-button-text').click()
