import math
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def prime_numbers_between(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

print("enter only Positive numbers which are > 0")
start = int(input("Enter the start number : "))
end = int(input("Enter the end number: "))
print(f" {prime_numbers_between(start, end)}")

