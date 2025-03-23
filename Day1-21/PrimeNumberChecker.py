def prime_checker(number):
    isprime = True
    for x in range(2, int(number/2)):
        if number % x == 0 and x != number:
            isprime = False
    if isprime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
