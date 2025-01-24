def display(n): #display function
    print(f"the Average of 4 numbers: {n}")

def input_v(): #taking input
    a=int(input("enter 1st number:"))
    b=int(input("enter 2nd number:"))
    c=int(input("enter 3rd number:"))
    d=int(input("enter 4th number:"))
    return(a,b,c,d)

def cal(a,b,c,d): #calculation
    avg=a+b+c+d
    n=avg/4
    return n

def main(): 
    (a,b,c,d)=input_v() 
    n=cal(a,b,c,d)
    display(n)

main()