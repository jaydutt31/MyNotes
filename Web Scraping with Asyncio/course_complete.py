import threading
from selenium import webdriver
import selenium.common.exceptions
import time, pickle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import sys


options = Options()
options.headless = False
options.add_argument("--mute-audio")
options.add_argument(r"user-data-dir=D:\\project\\AutoCourser\\config")
#options.add_experimental_option("detach", True)

print("starting")

def login():
	driver = webdriver.Chrome(options=options)
	web = driver.get("https://olympus.greatlearning.in/login")
	do = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/form[1]/div[1]/input")
	time.sleep(1)
	do.send_keys("duttjay255@gmail.com")
	do = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/form[1]/div[2]/input")
	do.send_keys("jaydutt@123")
	do = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/form[1]/div[3]/div[2]/button").click()
	time.sleep(5)
	driver.quit()

def test():
	try:
		driver = webdriver.Chrome(options=options)
	except:
		try:
			driver.quit()
		except:
			sys.exit()
	driver.get("https://olympus.greatlearning.in/dashboard")
	try:
		do = driver.find_element_by_class_name("MuiTypography-root").text()
		print(do)
	except:
		pass
	try:
		do = driver.find_element_by_class_name("CourseCards_enrolledCardCourseName__nZlMq").text()
		print(do)
	except:
		pass
	try:
		do = driver.find_element_by_class_name("MuiTypography-body1").text()
		print(do)
	except:
		pass
	driver.quit()


def main():
	first_time = 1
	while first_time != 1:
		login()
		first_time = 1 # just run for first time
	test()

main()

'''
try:
	
	do = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/form[1]/div[3]/div[2]/button").click()
	time.sleep(5)
	web = driver.get(x)
	time.sleep(15)
	try:
		do = driver.find_elements_by_xpath("/html/body/div[1]/main/div/div[2]/div[1]/main/div[2]/div[1]/div[2]/div[1]/div[2]/button")[0]
		do.click()
		print("opened a new tab")
	except Exception as e:
		time.sleep(1)
		print("Error Found, using other method")
		driver.get(x)
		time.sleep(20)
		do = driver.find_elements_by_xpath("/html/body/div[1]/main/div/div[2]/div[1]/main/div[2]/div[1]/div[2]/div[1]/div[2]/button")[0]
		do.click()
except:
	pass
'''
 































