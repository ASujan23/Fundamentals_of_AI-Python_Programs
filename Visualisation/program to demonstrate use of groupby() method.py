# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name':['A', 'B', 'C', 'D','E', 'F', 'G', 'H'],
'Age':[27, 24, 22, 32,33, 36, 27, 32],
'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Hyderabad','Chennai', 'Kanpur', 'Allahabad', 'Jaipur'],
'Qualification':['Msc', 'MA', 'MCA', 'Phd','B.Tech', 'B.com', 'Msc', 'MA']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1)
print(df)

# using groupby function with one key
df.groupby('Name')
print(df.groupby('Name').groups)

# Using multiple keys in groupby() function
df.groupby(['Name', 'Qualification'])
print(df.groupby(['Name', 'Qualification']).groups)