import data_collecting as dc 
import pandas as pd

# SAVES YEAR DATA TO FILE
def year_to_file():
    mydata = dc.get_stock_data("BTC/USD", "2022-01-01", "2022-12-31")
    file = open("saved_data/BTC_USD", "a")
    i = 1
    for x in mydata.df.get("open").values:
        file.write(str(x) + "," + str(i) + "\n")
        i+=1

year_to_file()

