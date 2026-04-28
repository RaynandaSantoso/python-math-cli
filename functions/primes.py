# Checks if num is prime
def is_prime(num):
    if num < 2:
        return False 
    #checks if num divides any number until sqrt(num).
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Returns primes up until the limit
def sieve_of_erastothenes(limit):
    #Makes an array with the value of True, up until the limit.
    number_list = [True] * limit
    number_list[0] = False
    number_list[1] = False

    for num in range(2, int(limit ** 0.5) + 1):
        if number_list[num]:
            for multiple in range(num*num, limit, num):
                number_list[multiple] = False

    list_of_primes = [i for i in range(limit) if number_list[i]]
    return list_of_primes


# Returns list of prime factors for 'num'
def prime_factors(num):
    factors = []
    while num > 1:
         for nums in range(2, num + 1):
            for divisor in range(2, int(nums ** 0.5) + 1):
                if nums % divisor == 0:
                    break
            else: 
                if num % nums == 0:
                    num //= nums 
                    factors.append(nums)  
                    break   