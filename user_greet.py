import data_collecting
import os, platform

SYSTEMNAME=platform.system()

def clear_menu():
    #clear screen
    if SYSTEMNAME=="Windows":
        os.system('cls')
    elif SYSTEMNAME=="Linux":
        os.system('clear')


def menu():
    while True:
    
        print("\n Python Trading Bot \n Licensed by Chaos Algo Trading Firm")
        print("\n 1. Track previous orders \n 2. Select stock to get data")
        
        try:
            user_input = int(input("Enter your input as a number:"))
        except ValueError:
            import time
            clear_menu()
            print("Please enter a number")
            time.sleep(3)
            clear_menu()
            continue

        if user_input == 1:        
            print("Track previous order")
            # from order_history import display
            # display()

        if user_input == 2:
            print("Weekly interval only")
            stock_name = input("Stock Ticker:")
            start_date = input("From Date: (YYYY-MM-DD or Start: )")
            end_date = input("To Date: (YYYY-MM-DD or Today): ")
            print(data_collecting.get_stock_data(stock_name, start_date, end_date))
            input()
        
        #clear screen
        clear_menu()

menu()
