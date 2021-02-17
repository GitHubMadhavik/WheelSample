import csv
import pandas as pd

date = input("Enter Date: Format(yyyy-mm-dd)        ")

filtered = pd.read_csv("C:\Script\PolicyData.csv", parse_dates=['Expiry'])
filteredresults = filtered[(filtered['Expiry'] > date) & (filtered['Expiry'] <= '2099-01-01')]
results = len(filteredresults)

print(results)
