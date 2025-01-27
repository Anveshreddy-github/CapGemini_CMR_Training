#empty dictionary
d={}
print("the empty dictionary",d)

#two item dic
d1={"car":4,"auto":3}
print("dict :",d1)

#nested dictionary
d2={"food":{"rice":4,"water":2}}
print("the nested dictionary:",d2)
print(d2["food"]["water"])

#zip keyword 
keys=['abc','xyz','pqr']
values=[1,2,3]
d4=dict(zip(keys,values))
print(d4)

#update
d.update(d1)
print(d)

#length
p=len(d)
print(f"the length of d is {p}")

#pop function
d8={"ram":7,"arun":9,"ruthvik":99}
print(d8)
d8.pop("ruthvik")
print("after pop :",d8)

#keys,values and items
q=d8.keys()
print(q)
r=d8.values()
print(r)
x=d8.items()
print(x)