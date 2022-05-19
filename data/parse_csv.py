import pandas as pd

df = pd.read_csv('daily_sales_data_0.csv')
df1 = pd.read_csv('daily_sales_data_1.csv')
df2 = pd.read_csv('daily_sales_data_2.csv')

# Adds all the .csv files to become 1 file
newfile = pd.concat([df, df1, df2])

# We are only interested in Pink Morsels,so I removed other rows which contain another type of product.
newfile = newfile[newfile['product'] == 'pink morsel']

# Combined quantity and price columns into sales column
# Since there are floats with .0 values, I converted to integer
newfile['price'] = newfile['price'].str.replace('$', '').astype(float)
newfile['sales'] = newfile['price'] * newfile['quantity']

newfile = newfile.drop(columns=['price', 'quantity'])

print(newfile.head())
newfile.to_csv('mynewfile.csv')
