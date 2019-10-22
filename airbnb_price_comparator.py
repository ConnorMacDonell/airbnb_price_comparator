from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup


url = "https://www.airbnb.com/s/saigon/homes?source=mc_search_bar&search_type=section_navigation&screen_size=large&checkin=2019-10-31&checkout=2019-11-07&adults=1&refinement_paths%5B%5D=%2Fhomes&place_id=ChIJ0T2NLikpdTERKxE8d61aX_E"
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)
delay = 5

first = True
second = False

first_class = "_1s7voim"
second_class = "_1jlnvra2"
curr_class = ""

try:
    listing_details = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div._1s7voim')))
except TimeoutException:
    try:
        first = False
        second = True
        listing_details = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div._1jlnvra2")))
    except TimeoutException:
        second = False
        print("Loading Timeout")

soup = BeautifulSoup(driver.page_source, "lxml")

if first:
    curr_class = first_class
elif second:
    curr_class = second_class


for listing in soup.find_all('div', class_=curr_class):
    if "1 bedroom" in listing.text:
        print(listing.text)


driver.quit()
