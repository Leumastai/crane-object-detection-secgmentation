#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 23:48:04 2021

@author: samuel
"""

import requests
from bs4 import BeautifulSoup
import lxml
import re
import os
from PIL import Image
import sys
import urllib.request, urllib.parse, urllib.error
import ssl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#MAIN_PATH = os.chdir("/home/samuel/images/crane")

driver = webdriver.Chrome(
        '/home/samuel/Downloads/Compressed/chromedriver')

"""
##FOR GOOGLE SEARCH
driver.get("https://www.google.com/")

box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys('crawler cranes')
box.send_keys(Keys.ENTER)

driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()

#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

for i in range(1, 1000):
    try:
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('/home/samuel/images/crane/crane_'+str(i)+'.png')
    except:
        pass
"""

##FOR BING
driver.get("https://www.bing.com/")

box = driver.find_element_by_xpath('//*[@id="sb_form_q"]')
box.send_keys("cranes")
box.send_keys(Keys.ENTER)

driver.find_element_by_xpath('//*[@id="b-scopeListItem-images"]/a').click()

#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(2)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

for i in range(1, 1000):
    try:
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('/home/samuel/images/crane/crane_'+str(i)+'.png')
    except:
        pass