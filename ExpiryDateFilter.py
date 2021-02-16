import csv
import pandas as pd

read = input("Enter File Path: ")
expirydate = input("Enter Expire Date: (mm/dd/yyyy)  ")

filtered = pd.read_csv(read, usecols=["Expiry"])
dateresults = (filtered[filtered["Expiry"] > expirydate])
results = dateresults.value_counts()

print(results)