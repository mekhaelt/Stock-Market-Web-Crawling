import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import pandas as pd
  


s = Service("D:\chromedriver")
  
driver = webdriver.Chrome(service=s)
  
url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
  
driver.get(url)
  
while(True):
    now = datetime.now()
      
    # this is just to get the time at the time of 
    # web scraping
    current_time = now.strftime("%H:%M:%S")
    print(f'At time : {current_time} IST')
    stocks=['none']*100
    columns=[1]*100
    c=0

    for x in range(1, 101):
        curr_path = ''
          
        # Exception handling to handle unexpected changes
        # in the structure of the website
        try:
            curr_path = f'/html/body/div[3]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr[{x}]/td[1]/span/sup'
            title = driver.find_element("xpath", curr_path)
        except:
            continue
        stocks[c]=(title.text)
       
        c += 1
        columns[c-1]=c
    # print(stocks)
    # chart1 = pd.Series(stocks)

    df = pd.DataFrame(stocks, index=columns)
    #df.to_excel('df.xlsx')

    #print(chart1)

    # to stop the running of code for 10 mins
    time.sleep(600) 
  

    
