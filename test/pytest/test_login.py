# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    self.driver.get("https://dazhadazha.pythonanywhere.com/")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.CSS_SELECTOR, ".bx-x").click()
    self.driver.find_element(By.LINK_TEXT, "Register").click()
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("758343984@qq.com")
    self.driver.find_element(By.ID, "password").send_keys("fengyunjia")
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(4)").click()
  
