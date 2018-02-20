# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:54:58 2018

@author: Akshit
"""
from selenium import webdriver

def main():
    driver = webdriver.Chrome()
    driver.get('https://www.udemy.com/join/login-popup/?ref=&display_type=popup&locale=en_US&response_type=json&next=https%3A%2F%2Fwww.udemy.com%2F&xref=')
    userid = driver.find_element_by_id("id_email")
    userid.send_keys('Here Enter Your Email')
    password = driver.find_element_by_xpath('//*[@id="id_password"]')
    password.send_keys('Here Enter Your Password')
    submit = driver.find_element_by_xpath('//*[@id="submit-id-submit"]')
    submit.click()
    driver.get('https://www.udemy.com')
    time.sleep(1000)
	
if __name__ == '__main__':
    main()
