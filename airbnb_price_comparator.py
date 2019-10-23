from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup


def get_prices(attr_class, price_class, soup):
	for listing in soup.find_all('div', class_='_8ssblpx'):
		attributes = listing.find('div', class_=attr_class).text
		if '4 guests' in attributes:
			price = listing.find('span', class_=price_class)
			print(price.text)
			print()


def get_driver(url):
	driver = webdriver.Firefox()
	driver.implicitly_wait(30)
	driver.get(url)
	return driver


def main():
	driver = get_driver('https://www.airbnb.com/s/saigon/homes?refinement_paths%5B%5D=%2Fhomes&current_tab_id=home_tab&selected_tab_id=home_tab&source=mc_search_bar&search_type=filter_change&screen_size=large&hide_dates_and_guests_filters=false&checkin=2019-11-07&checkout=2019-11-14&place_id=ChIJ0T2NLikpdTERKxE8d61aX_E&adults=1')
	
	i = 1
	first = True
	second = False
	delay = 1

	first_attr_class = '_1s7voim'
	first_price_class = '_1p7iugi'

	second_attr_class = '_1jlnvra2'
	second_price_class = '_1p3joamp'


	while True:
		try:
			WebDriverWait(driver, delay).until(
				EC.presence_of_element_located((By.CSS_SELECTOR, f'div.{first_attr_class}')))
		except TimeoutException:
			try:
				first = False
				second = True
				WebDriverWait(driver, delay).until(
					EC.presence_of_element_located((By.CSS_SELECTOR, f'div.{second_attr_class}')))
			except TimeoutException:
				second = False
				print('Loading Timeout')

		soup = BeautifulSoup(driver.page_source, 'lxml')

		if first:
			print(f'Page: {i}')
			print('Type 1')
			print()
			get_prices(first_attr_class, first_price_class, soup)
		elif second:
			print(f'Page: {i}')
			print('Type 2')
			print()
			get_prices(second_attr_class, second_price_class, soup)

		i += 1
		if soup.find('li', '_r4n1gzb').find('a', class_='_1ip5u88') is None:
			driver.quit()
			break

		next_ = driver.find_element_by_css_selector('li._r4n1gzb')
		python_button = next_.find_element_by_css_selector('a._1ip5u88')
		python_button.click()
			


if(__name__ == '__main__'):
	main()
