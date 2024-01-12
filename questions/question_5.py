from utils.utils import sin, pi, sqrt


# TODO : handeling IE for question 3 pop if there is one input
# محاسبه کردن یک چند جمله ای برای یک عدد خاص همان پیدا کردن f(n)
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
            if start_x_interval + h > stop_x_interval:
                break
            # دلیل استفاده از تابع راند نحوه ی کامپایل کردن اعداد اعشاری میباشد
            our_interval.append([round(start_x_interval, 2), round(start_x_interval + h, 2)])
            start_x_interval = start_x_interval + h

        sum_f_i = 0
        for i in range(1, len(our_interval)):
            sum_f_i += sin(our_interval[i][0])
        result = (h / 2) * (sin(our_interval[0][0]) + 2 * sum_f_i + sin(our_interval[-1][1]))
        return result
    else:
        # دلیل نوشته شدن این if بلاک تفاوت در نحوه ی بازه بنده برای انتگرال سینوس و بقیه اعداد هست
        # چون در بازه بندی سینوس یک عدد پی هم اضافه خواهد شد که در اینجابه بازه ها این عدد اضافه نمیشود
        h = (stop - start) / part
        start_x_interval = start
        stop_x_interval = stop
        our_interval = []
        while start_x_interval < stop_x_interval:
            # دلیل استفاده از تابع راند نحوه ی کامپایل کردن اعداد اعشاری میباشد
            if start_x_interval + h > stop_x_interval:
                break
            our_interval.append([round(start_x_interval, 2), round(start_x_interval + h, 2)])
            start_x_interval = start_x_interval + h

        print(our_interval)
        sum_f_i = 0

        if function.lower() == 'sqrt':
            for i in range(1, len(our_interval)):
                sum_f_i += sqrt(our_interval[i][0])
            result = (h / 2) * (sqrt(our_interval[0][0]) + 2 * sum_f_i + sqrt(our_interval[-1][1]))
            return result

        elif function.lower() == 'poly':

            degree = int(input('Please enter your polynomial degree: \n'))
            while True:
                coefficient = list(map(int, input('Please enter your coefficient of your polynomial function \n'
                                                  f'It should be exacly {degree + 1} \n'
                                                  f'plese seperate your numbers by space between each number: \n').split()))
                if len(coefficient) != degree + 1:
                    print('Bad coefficient quantity input try again!\n')
                else:
                    break
            for i in range(1, len(our_interval)):
                sum_f_i += (polynomial_func(degree, our_interval[i][0], *coefficient))
            result = (h / 2) * (polynomial_func(degree, our_interval[0][0], *coefficient) + 2 * sum_f_i
                                + (polynomial_func(degree, our_interval[-1][1], *coefficient)))
            return result


if __name__ == '__main__':
    print(integral(0, 1 / 3, 10, 'sin'))
    # print(polynomial_func(2, 2, *[2, 3, 2]))
    print(integral(4, 16, 20, 'hossein') is None)
    print(integral(4, 32, 30, 'poly'))
