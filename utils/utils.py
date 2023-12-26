pi = 3.141592653589793


def factorial(n):
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# finding this algorthm is blong to taylor's series of sin X source
# https://www.symbolab.com/solver/taylor-maclaurin-series-calculator/taylor%20%5Csin%28x%29?or=ex
def sin(x):
    """
    :param x:
    :return: the X will be multiplaied by pi number
    """
    result = 0
    for i in range(30):
        a = (-1) ** i
        b = (pi * x) ** (2 * i + 1)
        c = factorial(2 * i + 1)
        result += a * (b / c)
    return result


# def sqrt(x):
#     """
#     :param x:
#     :return: the squere root of X
#     """
#
#     return a


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
    # print(math.sqrt(10), sqrt(10))
    print(math.sin(math.pi / 4), sin(1/4))