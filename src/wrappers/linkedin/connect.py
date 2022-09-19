import logging
import time
import http.cookiejar as cookielib
import os
import urllib
import re
import string
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from time import sleep

from bs4 import BeautifulSoup


from src.config.linkedin import \
    LINKEDIN_USER, \
    LINKEDIN_PASSWORD, \
    LINKEDIN_USER_II, \
    LINKEDIN_PASSWORD_II
from src.config.scraperapi import API_KEY

logger = logging.getLogger(__name__)


class LinkedinConnection:

    def __init__(self):
        self.driver = None
        self.__initialize_driver()
        self.__login()

    def __initialize_driver(self):
        # proxy = "scraperapi:645302528ec3278e0a16594eec1dd39d@proxy-server.scraperapi.com:8001"
        # firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        # firefox_capabilities['marionette'] = True
        #
        # firefox_capabilities['proxy'] = {
        #     "proxyType": "MANUAL",
        #     "httpProxy": proxy,
        #     "ftpProxy": proxy,
        #     "sslProxy": proxy
        # }
        self.driver = webdriver.Firefox()

    def __login(self):
        self.driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
        username = self.driver.find_element('id', 'username')
        username.send_keys(LINKEDIN_USER_II)
        sleep(0.5)
        password = self.driver.find_element('id', 'password')
        password.send_keys(LINKEDIN_PASSWORD_II)
        sleep(0.5)
        sign_in_button = self.driver.find_element('xpath', '//*[@type="submit"]')
        sign_in_button.click()


linkedin_connection = LinkedinConnection()
