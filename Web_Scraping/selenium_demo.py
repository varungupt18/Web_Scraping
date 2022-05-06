# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 15:07:53 2021

@author: gupta330
material
fit 
upc
"""

# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
# Establish chrome driver and go to report site URL
url = "https://www.target.com/s?searchTerm=mens+hoodies&Nao=0&facetedValue=4apdi"
driver = webdriver.Chrome()
driver.get(url)

time.sleep(8)
driver.execute_script("window.scrollTo(0, 10800)")
time.sleep(3)
title = []
price = []
ratings = []
material = []
fit = []
upc = []
n=1
for item in driver.find_elements_by_xpath('//a[@data-test="product-title"]'):
    title.append(item.text)

for item in driver.find_elements_by_xpath('//div[@data-test="current-price"]'):
    ps = item.text.split(' ')
    price.append(ps[0].replace('$',''))



for item in driver.find_elements_by_xpath('//span[@data-test="ratings"]'):
    rs = item.text.split(' ')
    ratings.append(rs[0])
    
d = {'Title': title, 'Price': price, 'Ratings': ratings}
df = pd.DataFrame(data=d)
df['Price'] = df['Price'].astype(float)
df['Ratings'] = df['Ratings'].astype(float)
for prod in title:
    driver.find_element_by_link_text(prod).click() 
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 420)")
    driver.save_screenshot('test_shot{0}.png'.format(n))
    n += 1
    driver.find_element_by_xpath("//button[@data-test='toggleContentButton']").click()
    item = driver.find_element_by_xpath("//*[@class='styles__StyledCol-sc-ct8kx6-0 jOZqCG h-padding-h-tight']")
    test = item.text.split('\n')
    for thing in test:
        b = thing.split(':')
        if b[0] == 'Material':
            c = b[1][1:]
            material.append(c)
        elif b[0] == 'Fit':
            c = b[1][1:]
            fit.append(c)
        elif b[0] == 'UPC':
            c = b[1][1:]
            upc.append(c)
    driver.get(url) 
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 10800)")
    time.sleep(1)

df['Material'] = material
df['Fit'] = fit
df['UPC'] = upc


