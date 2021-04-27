import os
import asyncio 
from arsenic import get_session, keys, browsers, services
import pandas as pd 
import itertools
from requests_html import HTML 
import re, time, pathlib

import logging, structlog

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
	html_r = HTML(html=body_content)
	fabric_links = [x for x in list(html_r.links) if x.startswith("/en/fabric")]
	datas = []
	for path in fabric_links:
		id_, slug_ =await extract_id_slug(path)
		print(id_, slug_) 
		data = {
			"id":id_,
			"slug":slug_,
			"path":path,
			"scraped:": 0 # True / False -> 1 / 0
		}
		datas.append(data)
	return datas


async def scraper(url):
	service = services.Chromedriver()
	browser = browsers.Chrome(chromeOptions={
	    'args': ['--headless', '--disable-gpu']
	})
	async with get_session(service, browser) as session:
		await session.get(url)
		body = await session.get_page_source()
		#print(body)
		return body

def store_links_as_df_pickle(datas=[], name='links.pkl'):
	df = pd.DataFrame(datas)
	df.set_index('id', drop=True, inplace=True)
	df.to_pickle(name)
	return df

async def run(url):
	body_content = await scraper(url)
	links = await get_links(body_content)
	return links

if __name__ == "__main__":
	set_arsenic_log_level()
	url = 'https://www.spoonflower.com/en/shop?on=fabric'
	results = asyncio.run(run(url))
	df = store_links_as_df_pickle(results)
	print(df.head())
