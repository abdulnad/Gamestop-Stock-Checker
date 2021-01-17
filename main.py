from selenium import webdriver
import requests
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from the_bot import the_bot

bot = the_bot()
bot.sign_in()
bot.print_status()
#bot.check_for_stock()