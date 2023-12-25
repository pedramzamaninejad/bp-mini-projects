def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def sin(x):
    ...


def gcd(n, m):
    if n == 0 and m == 0:
        return None
    elif n == m:
        return n
    elif n == 0:
        return m
    else:
        n, m = (m % n), n
        return gcd(n, m)


if __name__ == '__main__':
    import math
    print(gcd(34, 50) == math.gcd(34, 50))
    print(factorial(5) == math.factorial(5))
