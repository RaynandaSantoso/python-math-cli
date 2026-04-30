import random

#returns nth fibonacci sequence
def fibonacci(n):
    num_list =[0]
    for num in range(n):
        current_num = 1
        if len(num_list) < 2:
            num_list.append(1)
            continue
        current_num = num_list[-1] + num_list[-2]
        num_list.append(current_num)
        
    return num_list[-1]

# Collatz Conjecture
def collatz(n):
    num = n
    step = 0
    while num > 1:
        if num % 2 == 0:
            num //= 2
            step += 1
        else:
            num = 3*num + 1
            step += 1
        print(num, f"step: {step}")
    return f"\nEnd Result: {num}, \nSteps: {step}"

# miller rabin probabilistic primality test
# n is number, k is the # of rounds
def miller_rabin(n, k):
    temp = n - 1
    r = 0
    d = temp
    while d % 2 == 0:        
        d = d // 2
        r += 1
    
    for _ in range(k):
        a = random.randint(2, n-2)
        x = a**d % n

        if x == 1 or x == (n-1):
            continue

        for _ in range(r - 1):
            x = x**2 % n
            if x == n - 1:
                break
        else:
            return False

    return True