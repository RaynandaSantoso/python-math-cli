def gcd(num1, num2):
    # euclidean Algorithm
    while num1 % num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    return num2

def extended_gcd(num1, num2):
    if num2 == 0:
        return num1, 1, 0
    gcd, x, y = extended_gcd(num2, num1 % num2)
    return gcd, y, x - (num1 // num2) * y


# modular_exp
def modular_exp(base, exp, mod):
    result = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2

    return result

# modular_inverse
def modular_inverse(num, mod):
    increment = 1
    raw_answer = 0
    for _ in range(1, mod):
        if increment % num == 0:
            raw_answer = increment
            break
        increment += mod
    answer = raw_answer // num
    return answer