from functions.primes import is_prime, sieve_of_erastothenes, prime_factors
from functions.modular import gcd, extended_gcd, modular_exp, modular_inverse
from functions.number_theory import fibonacci, collatz, miller_rabin

while True:
    print("""
╔══════════════════════════════════════════╗
║              MATH LAB CLI                ║
║   A CLI tool for mathematical functions  ║
╚══════════════════════════════════════════╝

  ── Primes ────────────────────────────────
  1  is_prime            Check if a number is prime
  2  sieve_of_eratosthenes  List primes from 2 up to N
  3  prime_factors       List the prime factors of N

  ── Modular Arithmetic ────────────────────
  4  gcd                 Greatest Common Divisor (Euclidean)
  5  extended_gcd        Extended Euclidean Algorithm (gcd, x, y)
  6  modular_exp         Modular Exponentiation  (base^exp mod m)
  7  modular_inverse     Modular Multiplicative Inverse of N mod M

  ── Number Theory ─────────────────────────
  8  fibonacci           Nth Fibonacci number
  9  collatz             Collatz sequence for N
  10 miller_rabin        Probabilistic primality test (n, k rounds)

  0  exit
─────────────────────────────────────────────""")

    selection = input("Select a function (0–10): ").strip()

    # ── Exit ────────────────────────────────────────────────────────────
    if selection == '0':
        print("Goodbye!")
        break

    # ── Primes ──────────────────────────────────────────────────────────
    elif selection == '1':
        number = input("Enter a number to check for primality: ")
        result = is_prime(int(number))
        print(f"\n  {number} is {'prime ✓' if result else 'not prime ✗'}\n")

    elif selection == '2':
        limit = input("Enter N — I'll list all primes up to N: ")
        result = sieve_of_erastothenes(int(limit))
        print(f"\n  Primes up to {limit}:\n  {result}\n")

    elif selection == '3':
        number = input("Enter a number to find its prime factors: ")
        result = prime_factors(int(number))
        print(f"\n  Prime factors of {number}: {result}\n")

    # ── Modular Arithmetic ───────────────────────────────────────────────
    elif selection == '4':
        print("\n  Greatest Common Divisor (Euclidean Algorithm)")
        num1 = int(input("  First number:  "))
        num2 = int(input("  Second number: "))
        result = gcd(num1, num2)
        print(f"\n  gcd({num1}, {num2}) = {result}\n")

    elif selection == '5':
        print("\n  Extended Euclidean Algorithm")
        print("  Finds gcd and coefficients x, y such that: num1·x + num2·y = gcd")
        num1 = int(input("  First number:  "))
        num2 = int(input("  Second number: "))
        g, x, y = extended_gcd(num1, num2)
        print(f"\n  gcd({num1}, {num2}) = {g}")
        print(f"  Coefficients: x = {x}, y = {y}")
        print(f"  Verification: {num1}·{x} + {num2}·{y} = {num1*x + num2*y}\n")

    elif selection == '6':
        print("\n  Modular Exponentiation — computes (base ^ exp) mod m")
        base = int(input("  Base:     "))
        exp  = int(input("  Exponent: "))
        mod  = int(input("  Modulus:  "))
        result = modular_exp(base, exp, mod)
        print(f"\n  {base}^{exp} mod {mod} = {result}\n")

    elif selection == '7':
        print("\n  Modular Inverse — finds x such that (num · x) ≡ 1 (mod m)")
        num = int(input("  Number:  "))
        mod = int(input("  Modulus: "))
        result = modular_inverse(num, mod)
        if result == 0:
            print(f"\n  No modular inverse exists for {num} mod {mod}\n")
        else:
            print(f"\n  Inverse of {num} mod {mod} = {result}")
            print(f"  Verification: {num} · {result} mod {mod} = {(num * result) % mod}\n")

    # ── Number Theory ────────────────────────────────────────────────────
    elif selection == '8':
        n = int(input("  Enter N to get the Nth Fibonacci number: "))
        result = fibonacci(n)
        print(f"\n  Fibonacci({n}) = {result}\n")

    elif selection == '9':
        n = int(input("  Enter a number to run the Collatz sequence: "))
        print()
        result = collatz(n)
        print(result)

    elif selection == '10':
        print("\n  Miller-Rabin Probabilistic Primality Test")
        n = int(input("  Number to test: "))
        k = int(input("  Number of rounds (higher = more accurate, e.g. 10): "))
        result = miller_rabin(n, k)
        print(f"\n  {n} is {'probably prime ✓' if result else 'composite ✗'} ({k} rounds)\n")

    else:
        print("\n  Invalid selection. Please enter a number from 0 to 10.\n")