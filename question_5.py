from utils.utils import sin, pi


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
            result += args[-1]
        else:
            result += (init ** i) * args[(-1) + (-i)]

    return result


def integral(start: float, stop: float, part: int, function: str):
    """
    :param start: The start point of interval
    :param stop: The stop point of interval
    :param part: how meny part of intervals you want with it start and stop points
    :param function: there is only two option of sin or sqrt of x
    :return:
    """
    if function.lower() == 'sin':
        start *= pi
        stop *= pi
        h = (stop - start) / part
        start_x_interval = start
        stop_x_interval = stop
        our_interval = []
        while start_x_interval < stop_x_interval:
            # دلیل استفاده از تابع راند نحوه ی کامپایل کردن اعداد اعشاری میباشد
            our_interval.append([start_x_interval, start_x_interval + h])
            start_x_interval = start_x_interval + h

        sum_f_i = 0
        for i in range(len(our_interval)):
            sum_f_i += sin(our_interval[i][0]) + sin(our_interval[i][1])
        result = (h / 2) * sum_f_i
        return result
    else:
        h = (stop - start) / part
        start_x_interval = start
        stop_x_interval = stop
        our_interval = []
        while start_x_interval < stop_x_interval:
            # دلیل استفاده از تابع راند نحوه ی کامپایل کردن اعداد اعشاری میباشد
            our_interval.append([start_x_interval, start_x_interval + h])
            start_x_interval = start_x_interval + h

        sum_f_i = 0

        if function.lower() == 'sqrt':
            f_n = stop ** 0.5
            for i in range(len(our_interval)):
                sum_f_i += our_interval[i][0] ** 0.5 + our_interval[i][1] ** 0.5
            result = (h / 2) * sum_f_i
            return result

        elif function.lower() == 'poly':

            degree = int(input('Please enter your polynomial degree: \n'))
            coeffient = list(map(int, input('Please enter your coeffient of your polynomial function \n'
                                            f'It should be exacly {degree + 1} \n'
                                            f'plese seperate your numbers by space between each number: \n').split()))

            for i in range(len(our_interval)):
                sum_f_i += (polynomial_func(degree, our_interval[i][0], *coeffient) + (
                    polynomial_func(degree, our_interval[i][1], *coeffient)))
            result = (h / 2) * sum_f_i
            return result


if __name__ == '__main__':
    print(integral(0, 1/3, 1000, 'sin'))
    # print(polynomial_func(2, 2, *[2, 3, 2]))
    print(integral(4, 16, 20, 'sqrt'))
    print(integral(4, 32, 30, 'poly'))
