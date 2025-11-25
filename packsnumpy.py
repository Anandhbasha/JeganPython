import numpy as np

# # 1d Array 
# arr1D = np.array([10,20,30,40])
# print(arr1D)

# arr2d = np.array([[20,40,60,80],[50,10,150,200]])

# arr3d = np.array([[20,40,60,80],[50,10,150,200],[30,60,90,120]])
# print(arr3d)

# zeros = np.zeros((3,4))
# print(zeros)

# ones = np.ones((2,3))
# print(ones)

# eye = np.eye(3)

# print(eye)

# rangeArr = np.arange(0,10,2)

# print(rangeArr)


# linSpace = np.linspace(0,1,5)

# print(linSpace)

# # random = np.random.rand(2,2)
# # print(random)

# # arr2d = np.array([[20,40,60,80],[50,10,150,200]])

# # print(arr2d[0,0])

# # # col
# # arr3d = np.array([[20,40,60,80],[50,10,150,200],[30,60,90,120]])
# # print(arr3d[:,2])
# # print(arr3d[0:2,1:3])

# arr = np.array([1,2,3,4,5])

# # print(arr[arr>3])

# arr1 = np.array([5,10,20,40,50])

# print(arr+10)


# # transpose
# # arr1 = np.array([[10,20],[50,100]])

# # print(arr1.T)

# print(np.sum(arr1))
# print(np.mean(arr1))
# print(np.max(arr1))
# print(np.min(arr1))
# print(np.std(arr1))


# arr = np.arange(12)

# print(arr)

# res = arr.reshape(3,4)
# print(res)

# flat = res.flatten()
# print(flat)


# pandas

import pandas as pd
# s1 = pd.Series([1,2,3,4,5],index=["a","b","c","d","e"])
# print(s1)

# data = {"apple":3,"banana":5}
# s3 = pd.Series(data)
# print(s3)

# print(s1*2)
# print(s1[s1>3])

# print(s1['a'])
# print(s1[1])

# Data frame
# data = {
#     "Name":["arun","Ajay","Bala","Chandru"],
#     "age":[20,22,23,25],
#     "City":["CBE","Erode","Salem","Namakkal"]
# }

# df = pd.DataFrame(data,index=[1,2,3,4])
# print(df)

dataNew = [
    {"Name":"arun","age":24,"City":"Erode"},
    {"Name":"ajay","age":20,"City":"Erode"},
    {"Name":"bala","age":22,"City":"Erode"},
]

dfList = pd.DataFrame(dataNew)
# print(dfList)

# print(dfList.head(2))
# print(dfList.tail(1))
# print(dfList.shape)
# print(dfList.columns)
# print(dfList['Name'])
# print(dfList[['Name','age']])

dfList["Course"] = ["Python","Java","Frontend"]
# print(dfList)


# print(dfList.loc[0])
# print(dfList.iloc[0:2,0:2])

# print(dfList[dfList["Course"]=="Python"])
# print(dfList[(dfList["Course"]=="Python") & (dfList["age"]>21)])

# add to excelsheet
dfList.to_csv("output.csv")

print("File created")



import pandas as pd

# From a list
s1 = pd.Series([1, 3, 5, 7, 9])
print(s1)

# With custom index
s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s2)

# From a dictionary
data = {'apple': 3, 'banana': 5, 'cherry': 7}
s3 = pd.Series(data)
print(s3)


# Basic operations
print(s2 * 2) 
print(s2 + s2) 

# Boolean indexing
print(s2[s2 > 25])

# Accessing elements
print(s2['b'])  
print(s2[1])  


# Pandas DataFrame
# A DataFrame is a 2-dimensional labeled data structure with columns that can be of different types.

# # Creating a DataFrame
# # From a dictionary of lists
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['NY', 'LA', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
# print(df)

# With custom index
df_indexed = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
print(df_indexed)

# From a list of dictionaries
data_list = [
    {'Name': 'Alice', 'Age': 25, 'City': 'NY'},
    {'Name': 'Bob', 'Age': 30, 'City': 'LA'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]
df_from_list = pd.DataFrame(data_list)
print(df_from_list)

# Viewing data
print(df.head(2))  # First 2 rows
print(df.tail(1))   # Last row
print(df.shape)     # Dimensions (rows, columns)
print(df.columns)   # Column names
print(df.dtypes)    # Data types of columns

# Accessing columns
print(df['Name'])   # As Series
print(df[['Name', 'Age']])  # Multiple columns as DataFrame

# Adding new column
df['Salary'] = [70000, 80000, 90000, 100000]
print(df)

#  Indexing and Filtering
# Basic Indexing

# loc - label-based indexing
print(df.loc[0])           # First row
print(df.loc[0:2, 'Name']) # Rows 0-2, 'Name' column

# iloc - position-based indexing
print(df.iloc[0])          # First row
print(df.iloc[0:2, 0:2])   # Rows 0-1, columns 0-1

# at - fast scalar access by label
print(df.at[0, 'Name'])

# iat - fast scalar access by position
print(df.iat[0, 0])


# Boolean Indexing (Filtering)
# Simple conditions
print(df[df['Age'] > 30])

# Multiple conditions
print(df[(df['Age'] > 25) & (df['City'] == 'LA')])

# isin()
print(df[df['City'].isin(['NY', 'Chicago'])])

# query()
print(df.query('Age > 30 and Salary < 95000'))

# String operations
print(df[df['Name'].str.startswith('A')])

# Reading and Writing Excel & CSV Files
csv_data = pd.read_csv('D:\shopping.shopping.csv')
print(csv_data.head())

# Read Excel
# pip install openpyxl
excel_data = pd.read_excel(r"C:\Users\Admin\Downloads\Students.xlsx", sheet_name='Sheet2')
print(excel_data.head())

#create and write a file
# Write to CSV
df.to_csv('output.csv', index=False)

# Write to Excel
df.to_excel('output.xlsx', sheet_name='Employees', index=False)

# With options
df.to_csv('output_advanced.csv', 
          index=True, 
          columns=['Name', 'Salary'],  # Only these columns
          encoding='utf-8')

# # Create a sample DataFrame
data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Accessories'],
    'Price': [1200, 800, 400, 300, 50],
    'Quantity': [15, 30, 25, 10, 50],
    'Date': pd.date_range('20230101', periods=5)
}
sales = pd.DataFrame(data)
sales['Revenue'] = sales['Price'] * sales['Quantity']

# Basic analysis
print("Summary Statistics:")
print(sales.describe())

print("\nCategory-wise Summary:")
print(sales.groupby('Category').agg({'Price': 'mean', 'Quantity': 'sum', 'Revenue': 'sum'}))

# Filtering
high_value = sales[sales['Price'] > 500]
print("\nHigh Value Products:")
print(high_value)

# Sorting
print("\nTop 3 Products by Revenue:")
print(sales.sort_values('Revenue', ascending=False).head(3))

# Pivot table
print("\nPivot Table (Category vs Price):")
print(pd.pivot_table(sales, values='Price', index='Category', aggfunc=['mean', 'count']))

# Save analysis results
sales.to_excel('sales_analysis.xlsx', sheet_name='Sales Data', index=False)
