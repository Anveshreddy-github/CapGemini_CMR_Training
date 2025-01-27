# def smallest_biggest(list):
#     list.sort()
#     print("the smallest number in the list is :",list[0])
#     print("the biggest the number in the list is:",list[len(list)-1])

# def main():
#     list=[100,4,3,99,300,1,400]
#     smallest_biggest(list)
# main()

def smallest_biggest(list):
    smallest = list[0]
    biggest = list[0]
    
    for num in list:
        if num < smallest:  
            smallest = num
        if num > biggest:
            biggest = num
    
    print("the smallest number in the list is :", smallest)
    print("the biggest number in the list is:", biggest)

def main():
    list = [100, 4, 3, 99, 300, 1, 400]
    smallest_biggest(list)

main()