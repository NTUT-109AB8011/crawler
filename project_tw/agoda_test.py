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
    self.driver.get("https://www.agoda.com/zh-tw/search?znrid=e9f43288-24fa-4834-8f83-5b105b0e9ced&city=8584&recommendedIndex=1&languageId=20&userId=54a55ad8-ae29-4023-a800-8cb128f38f6f&sessionId=hgrba30kpztoclgzwjyowat1&pageTypeId=1&origin=TW&locale=zh-TW&cid=1891473&tag=c6cac438-31ac-9b9f-bc08-0b36bc6fdc3f&gclid=EAIaIQobChMI3dfZoJvG7wIVqcFMAh1bCgR2EAAYASAAEgLyQPD_BwE&aid=82361&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&ckuid=54a55ad8-ae29-4023-a800-8cb128f38f6f&prid=0&checkIn=2021-04-16&checkOut=2021-04-17&rooms=1&adults=2&children=0&priceCur=TWD&los=1&textToSearch=%E8%8A%AD%E9%81%94%E9%9B%85&productType=-1&travellerType=1&familyMode=off")
    self.driver.set_window_size(1936, 1186)
    self.driver.find_element(By.ID, "ModalLoadingSpinner").click()
    self.driver.execute_script("window.scrollTo(0,1)")
    self.driver.execute_script("window.scrollTo(0,647)")
    element = self.driver.find_element(By.CSS_SELECTOR, ".JacketContent:nth-child(1) > .PropertyCard__Link > .sc-gTgzIj > .sc-jgHCyG:nth-child(3) > .sc-bdfBwQ")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".Searchbox__searchButton__text").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".JacketContent:nth-child(1) > .PropertyCard__Link > .sc-gTgzIj > .sc-jgHCyG:nth-child(2) > .sc-bdfBwQ")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
  