import threading

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    threads = []

    for number in numbers:
        thread = threading.Thread(target=check_even_odd, args=(number,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()