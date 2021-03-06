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

class TestUntitled():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_untitled(self):
    # Test name: Untitled
    # Step # | name | target | value
    # 1 | open | /tool/compound_interest?stkCode=5904 | 
    self.driver.get("https://www.moneycome.in/tool/compound_interest?stkCode=5904")
    # 2 | setWindowSize | 1020x835 | 
    self.driver.set_window_size(1020, 835)
    # 3 | click | css=.btn:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    # 4 | runScript | window.scrollTo(0,669) | 
    self.driver.execute_script("window.scrollTo(0,669)")
  
