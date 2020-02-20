from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup
import time
from docx import Document

####### LINK #########

# pip install selenium
# pip install python-docx
# pip install beautifulsoup4

# Selenium Documentation
# https://selenium-python.readthedocs.io/

# Chrome Driver
# https://sites.google.com/a/chromium.org/chromedriver/downloads

# BeautifulSoup Documentation
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Docx Documentation
# https://python-docx.readthedocs.io/en/latest/


opt = webdriver.ChromeOptions()
opt.add_argument('headless') # Don't open the browser

driver = webdriver.Chrome('C:\\Python37\\chromedriver.exe',options=opt)

pixel = 0

def HashTag(keyword,news=40):

	global pixel

	url = 'https://twitter.com/hashtag/' + keyword

	driver.get(url)

	time.sleep(3)
	totalpage =  news // 20 # per scrolling is 20 news
	for i in range(totalpage):
		driver.execute_script("window.scrollTo(0, {})".format(pixel))
		time.sleep(3)
		pixel = pixel + 10000
		#pixel += 10000

	page_html = driver.page_source

	data = soup(page_html, 'html.parser')

	tweetext = data.findAll('div',{'class':'css-1dbjc4n r-1j3t67a'})

	print(tweetext[0].text)


HashTag('thailand')
