#empty Tuples are immutable 
t=()
print("Its empty tuple",t)

#A one item tuple
t1=(0,1)
print(t1)

#A tuple
t2=(0,'a','m',7)
print(t2)

t3=0,'n',1,'f'
print(t3)

#nested tuple
t4=('abc',('pqr','xyz',9,8))
print(t4)

t5=tuple('spam')
print(t5)

print(t4[0])
print(t4[1][2])
print(t2[1:3])
l=len(t2)
print(l)