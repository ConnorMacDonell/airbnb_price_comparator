from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup


def get_prices(attr_class, price_class, soup):
    for listing in soup.find_all('div', class_="_8ssblpx"):
        if "1 bedroom" in listing.find('div', class_=attr_class).text:
            for price in listing.find_all('span', class_=price_class):
                print(price.text)


url = "https://www.airbnb.com/s/saigon/homes?source=mc_search_bar&search_type=section_navigation&screen_size=large&checkin=2019-10-31&checkout=2019-11-07&adults=1&refinement_paths%5B%5D=%2Fhomes&place_id=ChIJ0T2NLikpdTERKxE8d61aX_E"
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)
delay = 1

first = True
second = False

first_attr_class = "_1s7voim"
first_price_class = "_1p7iugi"

second_attr_class = "_1jlnvra2"
second_price_class = "_61b3pa"

try:
    listing_details = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, f"div.{first_attr_class}")))
except TimeoutException:
    try:
        first = False
        second = True
        listing_details = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"div.{second_attr_class}")))
    except TimeoutException:
        second = False
        print("Loading Timeout")

driver.quit()

soup = BeautifulSoup(driver.page_source, "lxml")

if first:
    print("Type 1")
    print()
    get_prices(first_attr_class, first_price_class, soup)
elif second:
    print("Type 2")
    print()
    get_prices(second_attr_class, second_price_class, soup)
