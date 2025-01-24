import dis
def display(n):
    print(f"multiplication of two numbers : {n}")

def input_v():
    a=int(input("enter a number"))
    b=int(input("enter b number"))
    return (a,b)

def mul(a,b):
    ans=a*b
    return ans

def main():
    (a,b)=input_v()
    n=mul(a,b)
    display(n)
main()
dis.dis(mul)