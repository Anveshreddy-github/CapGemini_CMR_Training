# def display(data):
#     print(f"The area is {data}")

# def area(l,b):
#     area=l*b
#     display(area)

# l=int(input("enter length:"))
# b=int(input("enter breath:"))
# area(l,b)


def display(area):
    print(f"The area of rectangle is {area}")

def input_s():
    l=int(input("enter length:"))
    b=int(input("enter breath:"))
    return (l,b)

def cal(l,b):
    area=l*b
    return area

def main():
    (l,b)=input_s()
    area=cal(l,b)
    display(area)

main()