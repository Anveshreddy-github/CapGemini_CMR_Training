import pandas as pd
def customer():
    n=int(input("enter no of records:"))
    data={'Name':[],'Age':[]}
    while n > 0:
        name=input("enter name :")
        age=input("enter age:")
        data['Name'].append(name)
        data['Age'].append(age)
        n-=1
    return data

def main():
    df=pd.DataFrame(customer())
    df.to_csv('data.csv',index=False)
    print(df)
main()