# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("nba.csv")
df.nsmallest(5, ['Age'])
df.nsmallest(10, ['Weight'])
df.nsmallest(5, ['Salary'])