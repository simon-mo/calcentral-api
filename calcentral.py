from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pprint
import datetime
import json

USER_INFO = {}
COURSE_LINK = 'https://calcentral.berkeley.edu/academics/semester/fall-2017/class/compsci-170-2017-D'



def find_element_and_filter(css_selector, lambdas, retry = 1):
	try:
		buttons = driver.find_elements_by_css_selector(css_selector)
		found_button = list(filter(lambdas, buttons))[0]
		return found_button
	except IndexError:
		if retry > 0:
			time.sleep(0.5)
			return find_element_and_filter(css_selector, lambdas, retry = 0)
		else:
			return None

def parse_date(text):
	if text == '':
		return ''
	return datetime.datetime.strptime(text, '%Y-%m-%d').strftime('%A')

driver = webdriver.Chrome()
# driver = webdriver.PhantomJS('phantomjs')

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(chrome_options=chrome_options)

driver.implicitly_wait(1)

try:
	with open('user_info.json','r') as f:
		USER_INFO = json.load(f)
except FileNotFoundError:
	USER_INFO['USERNAME'] = input('Enter Your Username: ')
	USER_INFO['PASSWORD'] = input('Enter Your Password: ')

	save = input('Remember the username and password?(y/[n]) ')
	if save.lower() == 'y':
		with open('user_info.json','w') as f:
			json.dump(USER_INFO, f)


print('Web Driver Initiated...')

driver.get('https://calcentral.berkeley.edu/')


sign_in_button = find_element_and_filter('button',lambda x:x.text == 'Sign In')
sign_in_button.click()

print('Begin Sign In Process...')

username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
username.send_keys(USER_INFO['USERNAME'])
password.send_keys(USER_INFO['PASSWORD'])

submit = find_element_and_filter('input', lambda x:x.get_attribute('value') == 'Sign In')
submit.click()

##TODO: Detect if auth success

print('Enter Course Page...')
driver.get(COURSE_LINK)

# ten_more = find_element_and_filter('button', lambda x:x.text == 'Show 10 More')
# while ten_more:
# 	ten_more.click()
# 	ten_more = find_element_and_filter('button', lambda x:x.text == 'Show 10 More')

videos = driver.find_elements_by_css_selector('td.cc-table-top-border')
videos = list(map(lambda x: x.find_element_by_css_selector('a'), videos))
videos = list(map(lambda x: (x.get_attribute('href'), x.text.split('\n')[0]), videos))
videos_with_week = list(map(lambda x: (x[0], x[1], parse_date(x[1])), videos))
print(videos)
print('Here are the links, ordered by newest to oldest...')
pp = pprint.PrettyPrinter()
pp.pprint(videos_with_week)

driver.close()

