"""
def fib(n):
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c
"""

"""
def fib(n):
    if (n <= 1):
        return n
    else:
        return fib(n-1) + fib(n-2)
"""

# Recursion using memoization


def fib(n):
    if (n <= 1):
        return n
    if (memo[n] != -1):
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]


memo = [-1] * 200
num = int(input("Enter a number : "))
res = fib(num)
print(f"The fibonacci of {num} is : {res}")
