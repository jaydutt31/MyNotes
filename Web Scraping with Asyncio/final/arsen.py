import os, asyncio, itertools, re, time, pathlib
from arsenic import keys, get_session, browsers, services
from requests_html import HTML 
import pandas as pd 

import logging
import structlog

def set_arsenic_log_level(level = logging.WARNING):
	logger = logging.getLogger('arsenic')

	def logger_factory():
		return logger

	structlog.configure(logger_factory=logger_factory)
	logger.setLevel(level)



async def extract_id_slug(url_path):
	regex = r"^[^\s]+(?P<id>\d+)-(?P<slug>[\w-]+)$"
	group = re.match(regex, url_path)
	if not group:
		return None, None
	return group['id'], group['slug']

async def get_links(body_content):
	html_r = HTML(html=content)
	print(html_r)

	fabric_links = [x for x in list(html_r.links) if x.startswith("/en/fabric")]
	datas = []
	import pandas as pd

	for path in fabric_links:
		id_, slug_ = extract_id_slug(path)
		print(id_, slug_)
		data = {
			"id":id_,
			"slug":slug_,
			"path":path,
			"scraped:": 0 # True / False -> 1 / 0
		}
		datas.append(data)

	df = pd.DataFrame(datas)
	df.head()

	df.to_csv("local.csv")

async def scraper(url):
	service = services.Chromedriver()
	browser = browsers.Chrome(chromeOptions={
	    'args': ['--headless', '--disable-gpu']
	})
	async with get_session(service, browser) as session:
		await session.get(url)
		body = await session.get_page_source()
		print(body)
		return body

if __name__=="__main__":
	url = 'https://www.spoonflower.com/en/shop?on=fabric'
	#loop = asyncio.get_event_loop()
	#results = loop.run_until_complete(scraper(url))
	results = asyncio.run(scraper(url))