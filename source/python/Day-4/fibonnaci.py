def fibonnaci(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)
def main():
    n=int(input("enter the positive number"))
    if n>=0:
        for i in  range(n):
            print(fibonnaci(i))
main()