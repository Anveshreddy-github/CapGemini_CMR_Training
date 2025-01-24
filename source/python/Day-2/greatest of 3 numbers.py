def display(n):
    print(f"The greatest of  numbers is {n}")

def input_c():
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    c=int(input("enter thid number"))
    return(a,b,c)

def greatest(a,b,c):
    if a>b & a>c:
        return a
    elif b>a & b>c:
        return b
    else :
        return c
    
def main():
    (a,b,c)=input_c()
    n=greatest(a,b,c)
    display(n)

main()