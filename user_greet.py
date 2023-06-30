def start():
    while True:
       
        print("\n Python Trading Bot \n Licensed by Chaos Algo Trading Firm")
        print("\n 1. Select a stock to analyze/order \n 2. Track previous orders")
        user_input = input("Enter your input as a number:")

        if user_input == "1":
            
            print("Select a stock to analyze/order")
            # from stock_analysis import analyze
            # analyze()
            
                       
            user_input = input()
            if user_input == '0':
                # Go back to start of while loop
                continue 
            else:
                import time
                time.sleep(10)  


        if user_input == "2":
        
            print("Track previous order")
            # from order_history import display
            # display()

start()
