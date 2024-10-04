def harmonic_serius(n, it1=0):
    it1 += 1
    if it1 == n:
        return 1 / it1
    else:
        return (1 / it1) + harmonic_serius(n, it1)


def power_recursion(a, x):
    if x == 0:
        return 1
    else:
        return a * power_recursion(a, x - 1)


def factorial_recursion(n):
    if n <= 0:
        return 1
    else:
        return n * factorial_recursion(n - 1)


def fibonacci_recursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


print(harmonic_serius(5))
print(power_recursion(3, 4))
print(factorial_recursion(5))
print(fibonacci_recursion(7))
