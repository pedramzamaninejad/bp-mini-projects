from utils.utils import sin


# here i calculate the intervals of our integrals
def interval(end, start, delta, intervals: list):
    while start < end:
        # دلیل استفاده از تابع راند نحوه ی کامپایل کردن اعداد اعشاری میباشد
        intervals.append([start, round(start + delta, 2)])
        start = round(start + delta, 2)
    return intervals


def polynomial_func(n: int, init: float, *args):
    """

    :param n: The degree of our polynomial
    :param init: This is the initial of the polynomial function
    :param args: The coefficient of Xes needs to be n + 1
    :return: The answer of the X
    """
    result = 0
    for i in range(n, -1, -1):
        if i == 0:
            result += args[i]
        else:
            result += (init ** i) * args[i]

    return result


def integral(start: float, stop: float, part: int, function: str):
    """
    :param start: The start point of interval
    :param stop: The stop point of interval
    :param part: how meny part of intervals you want with it start and stop points
    :param function: there is only two option of sin or sqrt of x
    :return:
    """
    h = (stop - start) / part
    our_interval = interval(stop, start, h, [])
    sum_f_i = 0

    if function.lower() == 'sin':
        f_n = sin(stop)
        for i in range(len(our_interval) - 1):
            sum_f_i += sin(our_interval[i][0]) + f_n
        result = (h / 2) * (sum_f_i + sin(start))
        return result

    elif function.lower() == 'sqrt':
        f_n = stop ** 0.5
        for i in range(len(our_interval)):
            sum_f_i += our_interval[i][0] ** 0.5 + f_n
        result = (h / 2) * (start ** 0.5 + sum_f_i)
        return result

    elif function.lower() == 'polynomial':
        degree = int(input('Please enter your polynomial degree'))
        coeffient = list(map(int, input('Please enter your coeffient of your polynomial function \n'
                                        f'It should be exacly {degree + 1} \n'
                                        f'plese seperate your numbers by space between each number').split()))

        f_n = polynomial_func(degree, stop, *coeffient)
        for i in range(len(our_interval)):
            sum_f_i += our_interval[i][0] ** 0.5 + f_n
        result = (h / 2) * (polynomial_func(degree, start, *coeffient) + sum_f_i)
        return result


if __name__ == '__main__':
    import sympy

    x = sympy.symbols('x')
    print(integral(0, 0.33, 20, 'sin'))
    print(sympy.integrate(sympy.sin(x), (x, 0, 0.33)))
    # print(sympy.integrate(x, (x, 0, sympy.pi*0.3333)))
#     print(polynomial_func(2, 2, *[2, 3, 2]))
