# def main():
#     arr=[]
#     for i in range(5):
#         n=int(input("enter the numbers in to array:"))
#         arr.append(n)
#     print(arr)
# main()

l1=[]
print("1.The empty list",l1)

l2=[1,2,3,4]
print("2. the list contains 4 elements :",l2)

l3=['abc',['xyz','pqr']]
print("3. The nested list",l3)

l4=list("spam")
print("4. List created from string spam:",l4)

l5=list(range(-4,4))
print("5. list created from the range [-4,4]:",l5)

l6=[10,20,30,40]
print("6.Element of index 2 :",l6[2])

#Accesing an element from a nested list by index
l7=['X',[1,2,3],'C','n']
print("7.the element in the index l7[1][2] is :",l7[1][2])

#slicing the list
l8=[1,2,3,4,5,6]
print("8. Slicing list from l8[1:4]",l8[1:4])

#length of the list
print("9.The length of l8:",len(l8))

#demonstrating nested indexing and slicing together
l9=[10,[100,200,300],20]
print("10a. Element at l9[1]:",l9[1])
print("10b. Element at l9[1,2]: ",l9[1][2])
print("10c. silicing sublist l9[1][1:3]:",l9[1][1:3])

