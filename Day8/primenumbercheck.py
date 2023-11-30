n = int(input("Enter a number 1-100  "))


def prime_checker(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    if is_prime == True:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")


prime_checker(n)
