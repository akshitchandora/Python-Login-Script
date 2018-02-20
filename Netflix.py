# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:05:58 2018

@author: Akshit
"""
from selenium import webdriver

def main():
    driver = webdriver.Chrome()
    driver.get('https://www.netflix.com/in/login')
    email = driver.find_element_by_xpath('//*[@id="email"]')
    email.send_keys('Here Is Your Email')
    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys('Here Is Your Password')
    submit = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[2]/div/div/form[1]/button')
    submit.click()
    time.sleep(1000)
	
if __name__ == '__main__':
    main()
