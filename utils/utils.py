pi = 3.141592653589793


def factorial(n):
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# سری تیلور برای محاسبه کردن sin
#  منبع https://en.wikibooks.org/wiki/Trigonometry/Power_Series_for_Cosine_and_Sine
def sin(x):
    """
    :param x: the X given shoulf be multiplied by pi and then given
    :return: The sin of X
    """
    result = 0
    for i in range(30):
        a = (-1) ** i
        b = x ** (2 * i + 1)
        c = factorial(2 * i + 1)
        result += a * (b / c)
    return result


# newton method for calculating sqer root
# source https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf
def sqrt(x):
    """
    :param x: x should be in range natural numbers
    :return: the squere root of X
    """
    N = 0
    while (N + 1) ** 2 <= x:
        N += 1
    N += 1
    d = N ** 2 - x
    result = N - (d / (2 * N))

    return result


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


def insertion_sort(data: list):
    for i in range(len(data)):
        min = data[i]
        min_index = i
        for j in range(i + 1, len(data)):
            if min > data[j]:
                min = data[j]
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]

    return data


def insertion_sort_str(data: list):
    for i in range(len(data)):
        min = data[i]
        min_index = i
        for j in range(i + 1, len(data)):
            if len(min) > len(data[j]):
                min = data[j]
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]

    return data

if __name__ == '__main__':
    import math

    # this for test for every indivdial functions
    print(gcd(34, 50) == math.gcd(34, 50))
    print(factorial(5) == math.factorial(5))
    print(math.sqrt(0.1), sqrt(0.1))
    print(math.sqrt(5), sqrt(5))
    print(math.sin(math.pi / 4), sin(1 / 4 * pi))
    print(sin(1 / 3 * pi), sin(0.33 * pi), math.sin(pi / 3))
