import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import pandas as pd
  

# creating the webdriver to open the browser
s = Service("D:\chromedriver") 
driver = webdriver.Chrome(service=s)
  
# opening the browser
url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
driver.get(url)


while(True):
    now = datetime.now()
      
    # gets the time of the web scraping
    current_time = now.strftime("%H:%M:%S")
    print(f'At time : {current_time} IST')
    
    # arrays to store collected data
    stocks=['none']*100
    percents=[1]*100
    prices=[1]*100
    volumes=[1]*100
    
    # counter variable
    c=0


    for x in range(1, 101):
          
        # collecting information from the website
        try:
            stock_path = f'/html/body/div[3]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr[{x}]/td[1]/span/sup'
            title = driver.find_element("xpath", stock_path)

            change_path = f'/html/body/div[3]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr[{x}]/td[2]/span'
            percent = driver.find_element("xpath", change_path)

            cost_path = f'/html/body/div[3]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr[{x}]/td[3]/text()'
            #cost = driver.find_element("xpath", cost_path)

            volume_path = f'/html/body/div[3]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr[{x}]/td[6]'
            vol = driver.find_element("xpath", volume_path)




        except:
            continue
        stocks[c]=(title.text)
        percents[c]=(percent.text)
        volumes[c]=(vol.text)
        c += 1
  
    # creating chart and importing into excel
    df = pd.DataFrame()
    df['Biggest Gainers'] = stocks
    df['% Change'] = percents
    df['Volume'] = volumes
    df.to_excel('Stock Info.xlsx', index=False)




    # stops and reruns the code every 10 minutes
    time.sleep(600) 