import csv
import pandas as pd

read = input("Enter File Path: ")
policy = input("Enter Coverage Type: ")

filtered = pd.read_csv(read, usecols=[policy])
result = filtered.value_counts()

print(result)