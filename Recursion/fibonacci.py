def fib(n):
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c


num = int(input("Enter a number : "))
res = fib(num)
print(f"The fibonacci of {num} is : {res}")
