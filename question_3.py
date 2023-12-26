from utils.utils import gcd


def lcm(*args):
    args = list(args)
    # exit condition
    if len(args) == 2:
        result = abs(args[0] * args[1]) / gcd(args[0], args[1])
        return result

    else:
        a = args.pop(0)
        b = args.pop(0)
        args.append(lcm(a, b))
        return lcm(*args)


if __name__ == '__main__':
    import math

    print(math.lcm(2, 5, 3) == lcm(5, 2, 3))
    # print(lcm(2, 5, 3))
