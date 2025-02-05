import pandas as pd

data={
    'Name':['Alice','Bob','Charlie','David'],
    'Age' :[25,30,21,40],
    'City':['NY','HYD','MH','DLE']
}
# df=pd.DataFrame(data)
# print(df)
# print(df.head())
# df=pd.read_csv('industry.csv')
# print(df)
df=pd.read_csv('customers-100.csv')
# df.to_html('customers.html')
print(df['Customer Id'])