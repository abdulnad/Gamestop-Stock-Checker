from selenium import webdriver
import requests
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from stock_checker import stock_checker

checker = stock_checker()
#stock_checker.sign_in()
sc = bot.print_status()
if sc == 200:
  bot.check_for_stock()
else:
  print('Could not reach page: status code {}'.format(sc))
