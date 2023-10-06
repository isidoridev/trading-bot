import matplotlib as mpl
import mpl.pyplot as plt
import numpy as np

def display_chart():
    file = open("BTC_USD", "r")
    
    for x in file:
