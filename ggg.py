from selenium import webdriver
from selenium.webdriver.common.by import By

# create a new Chrome browser
driver = webdriver.Chrome()

# navigate to the TradingView page for top gainers
driver.get("https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/")

# wait for the page to load
driver.implicitly_wait(10)

# find the table containing the stock information
table = driver.find_element(By.ID, "js-screener-container")

# find all rows in the table
rows = table.find_elements(By.TAG_NAME, "tr")

# print the stock symbol and price for each row
for row in rows:
    symbol = row.find_element(By.CLASS_NAME, "symbol").text
    price = row.find_element(By.CLASS_NAME, "price").text
    print(f"{symbol}: {price}")

# close the browser
driver.quit()


/html/body/div[3]/div[4]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/table/tbody/tr[{x}]/td[3]