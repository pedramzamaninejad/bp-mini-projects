from utils.utils import sin

# here i calculate the intervals of our integrals
def interval(end, start, delta, intervals: list):
    if start == end:
        return intervals
    else:
        interval_part = (start, start + delta)
        intervals.append(interval_part)
        return interval(end, interval_part[1], delta, intervals)


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

    if function.lower() == 'sin':
        f_n = sin(stop)
        sum_f_i = 0
        for itmes in our_interval:
            sum_f_i += sin(itmes[0])
        result = (h / 2) * (((part - 1) * f_n) + sum_f_i)
        return result
    else:
        f_n = stop ** 0.5
        sum_f_i = 0
        for itmes in our_interval:
            sum_f_i += itmes[0] ** 0.5
        result = (h / 2) * (((part - 1) * f_n) + sum_f_i)
        return result


if __name__ == '__main__':
    print(integral(0, 4, 4, 'sin'))
