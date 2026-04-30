# python-math-cli

A Python CLI tool implementing math functions from scratch, without using built-in math libraries.
This project serves as practice for writing mathematical concepts in code.

## Functions

### 🔢 Primes (`primes.py`)
| Function | Description |
|----------|-------------|
| `is_prime(n)` | Checks if a number is prime |
| `sieve_of_eratosthenes(n)` | Returns all primes up to n |
| `prime_factors(n)` | Returns list of prime factors |

### ➗ Modular Arithmetic (`modular.py`)
| Function | Description |
|----------|-------------|
| `gcd(a, b)` | Greatest common divisor |
| `extended_gcd(a, b)` | Returns gcd with Bézout coefficients |
| `modular_inverse(a, m)` | Modular multiplicative inverse |
| `modular_exp(base, exp, mod)` | Fast modular exponentiation |

### 🔭 Number Theory (`number_theory.py`)
| Function | Description |
|----------|-------------|
| `fibonacci(n)` | Returns nth Fibonacci number |
| `collatz(n)` | Returns Collatz sequence from n |
| `miller_rabin(n)` | Probabilistic primality test |

## Usage

```bash
python mathlab.py
```
