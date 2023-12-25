from utils.utils import gcd


def lcm(a, b):
    result = abs(a * b) / gcd(a, b)
    return result

if __name__ == '__main__':
    import math

    print(math.lcm(2, 5) == lcm(5, 2))
