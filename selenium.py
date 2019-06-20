from selenium import webdriver

browser = webdriver.firefox()
browser.get('https://automatetheboringstuff.com')
elem = browser.find_element_by_css_selector(".someClass")
elem.click()
elems = browser.find_element_by_css_selector(".someClass")
searchElem = browser.find_element_by_css_selector(".someClass")
searchElem.send_keys('kitty')
searchElem.submit()
browser.back()
browser.forward()
browser.refresh()
browser.quit()
