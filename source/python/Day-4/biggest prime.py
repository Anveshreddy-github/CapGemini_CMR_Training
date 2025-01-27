import math 
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def prime_numbers_between(start, end,l1):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def display(primes):
    l=len(primes)
    print("the smallest prime number in the range is :",primes[0])
    print("the largest prime number in the given range is :",primes[l-1])

def main():
    print("enter only Positive numbers which are > 0")
    start = int(input("Enter the start number : "))
    end = int(input("Enter the end number: "))
    l1=[]
    l1=prime_numbers_between(start,end,l1)
    display(l1)
main()
