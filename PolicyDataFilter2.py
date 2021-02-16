import csv
import pandas as pd

read = input("Enter File Path: ")
policy = input("Enter Coverage Type: ")

filtered = pd.read_csv(read, usecols=[policy])
yresults = (filtered[filtered[policy] == "Y"])
result = yresults.value_counts()

print(result)
