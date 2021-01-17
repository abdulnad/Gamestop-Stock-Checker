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

class the_bot:

    def __init__(self):
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
            'cookie': 'akaas_ChatThrottling=2147483647~rv=51~id=45a319d995e22751069818b76a4b100e~rn=; RES_TRACKINGID=57167115800665150; ResonanceSegment=1; _caid=cdfa3f0a-ae4c-423d-ac81-ac6ab0a4a4ff; _gcl_au=1.1.802771872.1605156601; _ga=GA1.2.237014674.1605156602; _mibhv=anon-1605156601743-1164461950_6874; __cq_uuid=bcme9lvRXuRrxdWEnLa5RV5Q7P; sto__vuid=fe61cda711289e483d90cd36a0f50bdf; QuantumMetricUserID=8bbe1492ff9ba8d58f3b9e495fe12fd1; _aeaid=26d17ca4-0fb8-476b-98bf-a929ae90713d; aeatstartmessage=true; __cq_dnt=0; dw_dnt=0; BVBRANDID=0fd84d9c-6342-47d9-91f7-e14b547eb604; BVImplsfcc=9014_3_0; salsify_session_id=09ee6c96-ec81-4466-b617-8087635086dd; fp=enableSEZZLE; manualDSCall=true; dwanonymous_420142ceefb9f0c103b3815e84e9fcef=abKbGjWw5jZpzpapuuoMeYCgJC; cqcid=abKbGjWw5jZpzpapuuoMeYCgJC; QSI_SI_3wI8Q9U6pfO1aAZ_intercept=true; akavpau_Prioritization=1607551246~id=e88d9ab11ed59974de4c89efb51b610f; linkshareAffiliateID=77777; linkshareSiteID=yFHdtQfGcHA-D0T1xAbiCYajgGKiF8H08A; __cfduid=defeec7cc72f8975425e1ee027a47d08e1607883626; QuantumMetricSessionID=9e1a99c2be73f4be450058ff9545cf93; __cq_seg=0~0.00u00211~0.00u00212~0.00u00213~0.00u00214~0.00u00215~0.00u00216~0.00u00217~0.00u00218~0.00u00219~0.00; _gcl_aw=GCL.1609090721.Cj0KCQiAh4j-BRCsARIsAGeV12BuoMT3ljYebxzTuVuiAtsh-ZKSnhlGZ44G39RfD-OKol35xveevb4aAvYVEALw_wcB; _gcl_dc=GCL.1609090721.Cj0KCQiAh4j-BRCsARIsAGeV12BuoMT3ljYebxzTuVuiAtsh-ZKSnhlGZ44G39RfD-OKol35xveevb4aAvYVEALw_wcB; _gac_UA-10897913-30=1.1609090723.Cj0KCQiAh4j-BRCsARIsAGeV12BuoMT3ljYebxzTuVuiAtsh-ZKSnhlGZ44G39RfD-OKol35xveevb4aAvYVEALw_wcB; AnonymousSaveForLaterCookie=2970fa0dc82dcb3addd5ad481f; _gaexp=GAX1.2.mYB1pHUnSEqFhyd7qQABsQ.18701.1u0021N7GoCGDvTuqZT8JcTJnoKQ.18702.1; _k_lia_e=M9/ipZNCkh1DxtslxM6t8zs4PruOKNmOhJRgXpFvwDTy8JK9ojFkfIM/D1dpzd0KO8mg98S8q72424QM1AWZD7nh2vOt7CzQr9ULATcn0qt+WMmOx6CX3HtooISXQ9if/dsBiBrZW1Z1pfDiTUk6BfMvpfRyoa28C059vI0rFTO3QdWLdkMiuZZd6NPD/YuMQljFmuaa4iugpS/XnhDcFK3dAxjCskYQ1VPPVM1rc6De1DDXGmaVRGtm2wiVjvg1sNCJ4bDHByDqoKHXQxBtEpORwd/FOQL81sLGgX3aqjVfhOIYRMlqIae2tWE/mPYkevozIUpmRA40aNWjdK8ngdT1r+VhvEbCQcwfzcBFaojbsmfFH9pfCGBKKA3dlwyh66Bhn773zypbT13AumOyzaBe/7j8jhNMicjmKg+SnUi7/B5+5TaOfd9LVkN3AOpQSQ1IVXd9eICqouNTvx3gmsxUA116hCYMgOmGqZDbP/q6yVrXwIurJWCp1EI2KwYw0KtddVFMugp5PBSshFm6rDyPiL07kygQr5N8WhFAmtXGy1FVH8GEbUjxIsMkW+enm0gUt/tRkBX/QLB4lnf2uVXDwLcT13unuPz5wxcOtQ9w0pmEhiEJfgh5yoVCtqGRuLPz8YFRS0fqi8hbGcNPITuV73u2+cOMiyoNspq0Fns=; cquid=||; customergroups=Everyone; userInfo=S=N|R=N|C=0; QSI_HistorySession=https%3A%2F%2Fwww.gamestop.com%2Fsearch%2F%3Fq%3Dpokemon%2Bchampions%2Bpath%26lang%3Ddefault~1609183360872%7Chttps%3A%2F%2Fwww.gamestop.com%2Ftoys-collectibles%2Fgames-puzzles%2Ftrading-card-games%2Fproducts%2Fpokemon-trading-card-game-sword-and-shield-vivid-voltage-elite-trainer-box%2F11107433.html%3Fcondition%3DNew~1609212942385%7Chttps%3A%2F%2Fwww.gamestop.com%2Ftoys-collectibles%2Fgames-puzzles%2Ftrading-card-games%2Fproducts%2Fpokemon-trading-card-game-champions-path-wave-1-pin-collection-assortment%2F11104959.html%3Fcondition%3DNew~1609353148063%7Chttps%3A%2F%2Fwww.gamestop.com%2Fsearch%2F%3Fq%3Dpokemon%2Bhidden%2Bfates%26lang%3Ddefault~1609366852906%7Chttps%3A%2F%2Fwww.gamestop.com%2Forder%2Fview%2F~1609434574516%7Chttps%3A%2F%2Fwww.gamestop.com%2Ftoys-collectibles%2Fgames-puzzles%2Ftrading-card-games%2Fproducts%2Fpokemon-trading-card-game-hidden-fates-tin-assortment%2F11095083.html%3Fcondition%3DNew~1609790083286; _gid=GA1.2.4647603.1609978026; bm_sz=AC4EF838FE39BF665396289AAB376644~YAAQRwEkF3j0V912AQAAryV73gp2mS840bR3AxS2bij6CTwpjDuZU4UMBiI8XIWUkzVsCwBlMy3yyfJjH1LqefQJCjaNuY0EIuJzLzKKo3H8CLDhlKEQI+Y+BuPh31a1h/DhhR96KB0SpXuP855wW+PssO5/K0NNkebXaJ1O55WHCTAfyGyL1nHEJrODokq1xXE=; dwac_a78eb5a11975e4c9cbc84f55ad=Y3KLMdFjS71zbs80wWeS7ll6rlfndujBuP0%3D|dw-only|||USD|false|US%2FCentral|true; sid=Y3KLMdFjS71zbs80wWeS7ll6rlfndujBuP0; dwsid=Ojlm2kAThwtFB6PmLOoJLQAxQ7x2BiR3jpSHs-PGGWjJT1XsTEtA56lg6jYt9I3UxOtjxyNMMutQzpn2X8Yo8w==; bm_mi=8DF5C8371E2E9399B4188FBFF61E03D5~i8d6Swl3oblIns2UZWwYneazWb3ckVHOdk0SGy+3pblmf+1J5COlzbdgqzMWmmwRQe18inoPNYDxUBcYlazCxthHvX1MZ6ai3F2OTAoGABSqBPB9kPDDm4CXngb31RCTOHmmMOONppfAXxjz7jaE0KArsqNuBQqlTlRizaxmM0mzkftYFJk6Z7FQvSy5P0Kzy/L4xrbxLuiYWBn225svt0fd1niUDAW6Cw1dXz+YNrQE2sXCWTdxRt5PvCm36+8+qcIefZNjn2qxkd0enfSjc3fI1pxhuxYTn7T7jGPc8gY=; RES_SESSIONID=68707090928305001; _cavisit=176de7b2c4e|; ak_bmsc=FF187DE6AB4FB5B4A871AFB8AE78C0C217240147693C00004D6BF75F4021CD39~plcVyGy8VO8pVdiNzMFkaXOjyeW2kuylTYrkm4aHFo3dX62VT+YP9C6mO3FvpIyzAFE12RGELVKGTgLPaWjszb7sSXOnvIq3hlJ2UAeF8sMaSd2UFm9EPXQ/HECetDPNKUbnzmNUlzJYnzsUAvfZ15uoscI9Bx9wQcyLvtl/qDCYNRos0gAAnyjAjee6QSCuPOsp6Gy4pWu2+xQJyhYWbS0Po1oTq05EB2x0bRnEKSkzZ5Yrp8my5mZ/PaWMTe572k; BVBRANDSID=202d316d-eac7-4cd2-b09f-fd81ea3db54a; sto__session=1610050790454; __cq_bc=%7B%22bcpk-gamestop-us%22%3A%5B%7B%22id%22%3A%2211095083%22%7D%2C%7B%22id%22%3A%2211108140%22%7D%2C%7B%22id%22%3A%2211096131%22%7D%2C%7B%22id%22%3A%2211094826%22%7D%2C%7B%22id%22%3A%2210112167%22%7D%2C%7B%22id%22%3A%2211104959%22%7D%2C%7B%22id%22%3A%2211104961%22%7D%2C%7B%22id%22%3A%2211107433%22%7D%2C%7B%22id%22%3A%2211096133%22%7D%2C%7B%22id%22%3A%2210167287%22%7D%5D%7D; _uetsid=471397a0507c11eb913c0dbc0d34d0c4; _uetvid=860b2c4024a211eb9885d35414730258; stc118903=env:1610050383%7C20210207201303%7C20210107210437%7C5%7C1084110:20220107203437|uid:1605156601899.1008609373.8614445.118903.1886455122:20220107203437|srchist:1084103%3A1607549188%3A20210109212628%7C1084111%3A1607621892%3A20210110173812%7C1084103%3A1607621912%3A20210110173832%7C1084111%3A1608777041%3A20210124023041%7C1084103%3A1608824135%3A20210124153535%7C1084111%3A1608929541%3A20210125205221%7C1084110%3A1609027618%3A20210127000658%7C1084103%3A1609090722%3A20210127173842%7C1084111%3A1609978026%3A20210207000706%7C1084110%3A1610050383%3A20210207201303:20220107203437|tsa:0:20210107210437; sto__count=3; QSI_S_SI_3wI8Q9U6pfO1aAZ=r:25:426; bm_sv=918898C84FC0200C8C6BA0CEFBECA037~rRWMR9a9rtrXwhMCyKCMNHRHOzgny/xXEg5JmU0izaZXv8jwJRieUv/cPCk0uHo1WB6V7y247hvcTfHL2QxJuJQ547dDLCsXEzUhXyNvWYtd7QUYa3zClz3Fy0i7qWEnUaqGVHhFRrJ+MjA6WULvQyHaUZ2ipCCqZOe7giNkSQA=; RT="z=1&dm=gamestop.com&si=8scw7kazq0j&ss=kiuw8u86&sl=0&tt=0"; _abck=4D423E81648FB269CF6AF999BE79841D~-1~YAAQTPs7F1EFCM52AQAAe2eW3gUqGAih/UIKkdK7/mFE3vb/VQoBqMYpdGeOduqbWas+6UaRXV7Lgaj4iDdPkQrhL1wOoa7yHTbnCIZa/Raszul8qg/KnRe3Q2dRcOtH++Gtjt1OJ0+dkpZ4m6Upw53DrJ0QLUFXdmdLMU9VHdwgi4kmVVd/mZN4EcSsYP9U1otjCMZHAikQEYB4B8HluJ3u/1JabO4LWDmHG4peMG1z04lkQT37QnFLApQQ790xqsdlnT3ebdyR0N1slKVTnhApm6Hbg2ILxSjtN3JoBKvcNIYA1bvBCLGQi1Ti37kFWr1l8CxzS+vLfYpln9c/2ramPYfzU1HeL62Apu71/gt6Rrv1ZQ==~-1~-1~-1; ak_bmsc=70F54DC84E43C2CED8B261EB9CE655FD173097BD1D2C00004A6FF75F169E6E09~pl2Ra4PaNLSAKWip/ImOa9ZTGS56W4ZGnCD2g1sUEmUnPYiIQjfcBg0CScPwb5PG6Ovi2BjB03Ig1+i/XHarjKjREbIK7kElk3wz0wUvIxC/1daQgoJlhdDykd7TjKD3PPQLSpRV40fME1mb6igPZCFL53xEyqf0HKsMZCqZnFF8b7Z5zsc0LJE/7n5TpsgN25zrCN2vShioWrngwZklkJ2HQQyqE5wU7AmJE4Jk5KM/Q=; akaas_ChatThrottling=2147483647~rv=41~id=0c53f572ef6c175ff081ff75231f3f06~rn=; bm_sz=9D5A3859A31F7550F6CB68EFBEC6C5F3~YAAQvZcwFy9OEN52AQAAj7mK3go4JIRcnnu/pTRgabfXies85d69ZJW/9ohC/vmD/aOTQViLC6OHx2lg3aiGaeu91vVCu3fyLG8HkMArc+MsdnINh6AJnikZVaSGL2u1s9FrX/C/XJVC5j6LNWyeAx3c4ky8ZvwN7XufcKQ9nnAowhAGAN+n0YkrlzQhemq+qpw=; bm_mi=9F61CEDA9DE8E1DC157ECE03DD7AC076~TJpOD/VfLBwED5eP/ImXEbWNoNw+nW2bNchP8exqrdYEwqUm0DL/CnamFgzLCAWcYYoJaQS5+9YCn7p72sKmBBaqBPixLpjuuYzcvjK5wxjf6c9P9cEmJ2kEiSrqbY5kGSIB3YLsEpQ+9VKPa3Bdq9ELECkWmxaN3PbO6Qdhb8LBi9/dL9VPRNXkag0cdASksmv1xqWzXgx2Z3mQqpWRS6lyF0y1k3fduT4FSw6myOTTFOtTgUQomFm5JCr6SIz8WsseTp8HgUYoMeJHKBgaZ7koFdSaSBY8oKwp3cu4gaxDk4HwF3unSY4sk8kDMnsTInrBFdfaEOx5JCaZdjBjdcP0OdC7mZKupaHVR6ePVaPnHOfGe5e6uUASvo6n4OiKES18Aga+NrtMD10Velu6Ew==; __cq_dnt=0; dw_dnt=0; bm_sv=918898C84FC0200C8C6BA0CEFBECA037~rRWMR9a9rtrXwhMCyKCMNHRHOzgny/xXEg5JmU0izaZXv8jwJRieUv/cPCk0uHo1WB6V7y247hvcTfHL2QxJuJQ547dDLCsXEzUhXyNvWYsN4V5e2NM4hxjmNiY+rgi/TdqiCuq/ybL96zui+TemmWTJHFFScLP28ZN5qCG7C+8=; _abck=4D423E81648FB269CF6AF999BE79841D~-1~YAAQjpcwF+X+ptB2AQAAjoWd3gXyIySs0A8U5iE1he7kK9WaQkfius9jvdwwgFiT5f+aCwD7duGvZxoaMUSjJyKx8UR3Q9t2Isf95mMe89B6ljm6ApuRrC3xj9lKwEHhzWpNkl71/nMkfpEOMOqTu6swbQeN39fuhvIcw9K1vxJmYFF2owzWlu9+pufCoMocWTgQL+t0kW27Ss3sNNCOKsK3s+ixEZgmmp2m1M/mAiNOBpsyB7ID91aznQ1KwuXyTS67gO/kjGYjB52tY4MZsWer5qgHXR+tDgbDp00822qXxg79hkHglZCBzmAVHMPcRHo4OY11NjY+LZ+xjC3JJoq2rEOTVxftKb40fPxN63iU754gJg==~0~-1~-1'
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
        driver = webdriver.Chrome(executable_path="/Users/abdullahnaderi/Downloads/chromedriver", options=option)
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
            driver.find_element_by_id('login-form-email').send_keys('abdullah7998@gmail.com')
            time.sleep(3)
            driver.find_element_by_id('login-form-password').send_keys('Spiderwimin555!')
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
            if inStock == False:
                time.sleep(2)
                driver.refresh()
            if new_ua == 5:
                userAgent = ua.random()
                option.add_argument('user-agent={}'.format(userAgent))







