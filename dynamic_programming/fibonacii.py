# 1, 1, 2, 3, 5, 8
#


def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
