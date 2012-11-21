#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common import keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time

driver = webdriver.Ie()
driver.get("http://ts-test.validio.com.ua/ctpm")
alert = driver.switch_to_alert()
print alert.text
alert.send_keys(keys.Keys.TAB)
alert.send_keys(keys.Keys.TAB)
alert.send_keys(keys.Keys.TAB)
alert.send_keys(keys.Keys.ESCAPE)
driver.get("http://ts-test.validio.com.ua/ctpm")
Field = driver.find_element_by_xpath("\\input[@id=.*UserName]")
Field.SendKeys("Viktor.klymenko")
#comment

#it is test ts test