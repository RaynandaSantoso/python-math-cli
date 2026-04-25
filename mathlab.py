from functions.primes import *

while True:
    print("\n")
    print("=== MATH LAB ===")
    print("Welcome to Math Lab. CLI tool for math functions")
    print("""
    Please select the available functions:
    0 - exit
    1 - is_prime : Check if a number is prime.
    2 - sieve_of_erastothenes : List down prime numbers from 2 - number.
    """)
    selection = input("select the function to use: ")

    if selection == '0':
        break
    if selection == '1':
        number = input("Input a number to check for pimality: ")
        is_prime(int(number))
    if selection == '2':
        limit = input("Input a number, and I will return a list of primes before it: ")
        sieve_of_erastothenes(int(limit))
    else:
        print("Please select a number from 0-10")