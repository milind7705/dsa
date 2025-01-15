from math import sqrt, floor

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

print(is_prime(1)) # -> False

print(is_prime(2))

print(is_prime(2017)) # -> True
