from selenium import webdriver
import requests
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from fake_useragent import UserAgent
import os

class stock_checker:
      
    def __init__(self):
        user = os.environ.get('user')
        password = os.environ.get('passwordgame')
        ua = UserAgent()
        nua = ua.random
        #Headers setup
        global headers
        headers = {
            'authority': 'www.gamestop.com',
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-hidden-fates-tin-assortment/11095083.html?condition=New',
            'accept-language': 'en-US,en;q=0.9',
        }
        #Options setup
        global option
        option = webdriver.ChromeOptions()
        option.add_argument('--disable-blink-features=AutomationControlled')
        option.add_experimental_option("excludeSwitches", ['enable-automation']);
        option.add_argument('--incognito')
        #option.add_argument('user-agent={}'.format(headers['user-agent']))
        option.add_argument('user-agent={}'.format(nua))
        #Chromedriver setup
        global driver
        driver = webdriver.Chrome(executable_path=PATH, options=option)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        global website
        website = "https://gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-hidden-fates-tin-assortment/11095083.html?condition=New"
        driver.get(website)
        count = 5


    def print_status(self):
        url = "https://www.gamestop.com/on/demandware.store/Sites-gamestop-us-Site/default/Stores-ProductDetailStoreAvailability?pid=11095083&redesignFlag=true&storeId=2605"
        r = requests.request("GET", url, headers=headers)
        data = json.loads(r.text)
        print(r.status_code)
        print(requests.get(website,headers=headers).status_code)

    def sign_in(self):
        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, "MY ACCOUNT"))
            )
            element.click()
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, "SIGN IN"))
            )
            element.click()
            time.sleep(2)
            driver.find_element_by_id('login-form-email').send_keys(user)
            time.sleep(3)
            driver.find_element_by_id('login-form-password').send_keys(password)
            time.sleep(1)
            driver.find_element_by_id('login-form-password').send_keys(Keys.RETURN)
            time.sleep(2)



            #btn btn-block btn-primary

        except:
            driver.quit()
    def checkout(self):
        pass




    def check_for_stock(self):
        driver.get(website)
        url = "https://www.gamestop.com/on/demandware.store/Sites-gamestop-us-Site/default/Stores-ProductDetailStoreAvailability?pid=11095083&redesignFlag=true&storeId=2605"
        r = requests.request("GET", url, headers=headers)
        data = json.loads(r.text)
        global inStock
        gotem = False
        new_ua = 0
        ua = UserAgent()
        while gotem==False:
            for s in data['products']:
                inStock=s['inStock']
            if new_ua == 5:
                userAgent = ua.random()
                option.add_argument('user-agent={}'.format(userAgent))
            if inStock == False:
                time.sleep(2)
                driver.refresh()
            elif inStock == True:
                    with smtplib.SMTP('smtp.gmail.com', 587) as smtp: #SEND ME AN EMAIL
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.ehlo()
                        smtp.login(user,password)
                        subject = 'Hidden Fates in STOCK!'
                        body = 'https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-burning-shadows-sleeved-booster-pack/10149279.html'
                        msg = 'Subject: {}\n\n'.format(subject) + '{}'.format(body)
                        smtp.sendmail(user,user,msg)
            







