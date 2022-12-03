import time
from selenium import webdriver
from datetime import datetime

# path of the chromedriver we have just downloaded
PATH = r"D:\chromedriver"
driver = webdriver.Chrome(PATH)  # to open the browser
  
# url of google news website
url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
  
# to open the url in the browser
driver.get(url)  

stocks = [100]



while(True):
    now = datetime.now()
      
    # this is just to get the time at the time of 
    # web scraping
    current_time = now.strftime("%H:%M:%S")
    print(f'At time : {current_time} IST')
    c = 1
  
    for x in range(1, 101):
        curr_path = ''
          
        # Exception handling to handle unexpected changes
        # in the structure of the website
        try:
            curr_path = f'//html/body/div[3]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr[{x}]/td[1]/span/sup'
            title = driver.find_element_by_xpath(curr_path)
        except:
            continue
        print(f"Heading {c}: ")
        c += 1
        print(title.text)
          
    # to stop the running of code for 10 mins
    time.sleep(600) 



