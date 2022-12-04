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
    
    # counter variable
    c=0


    for x in range(1, 101):
        curr_path = ''
          
        # collecting information from the website
        try:
            curr_path = f'/html/body/div[3]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr[{x}]/td[1]/span/sup'
            title = driver.find_element("xpath", curr_path)

            other_path = f'/html/body/div[3]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr[{x}]/td[2]/span'
            percent = driver.find_element("xpath", other_path)

        except:
            continue
        stocks[c]=(title.text)
        percents[c]=(percent.text)
        c += 1
  
    # creating chart and importing into excel
    df = pd.DataFrame()
    df['Biggest Gainers'] = stocks
    df['% Change'] = percents
    df.to_excel('df.xlsx', index=False)




    # stops and reruns the code every 10 minutes
    time.sleep(20) 

