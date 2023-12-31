def find_prependicular(two_point: list):
    """
    :param two_point: [(x1, y1), (x2, y2)]
    :return: (m, h) : slop and Width from the origin ; mX + h
    """
    mid_x = (two_point[0][0] + two_point[1][0]) / 2
    mid_y = (two_point[0][1] + two_point[1][1]) / 2
    try:
        prependicular_slop = (-1) / ((two_point[0][1] - two_point[1][1]) / (two_point[0][0] - two_point[1][0]))
    except ZeroDivisionError:
        prependicular_slop = 0
    # عرض از مبدا
    h = mid_y - (prependicular_slop * mid_x)
    return prependicular_slop, h


def impact_prependicular_rectangle(rectangle: tuple, prependicular: tuple):
    """
    :param rectangle: (x, y) from the top rightest
    :param prependicular: (m, h) : slop and Width from the origin ; mX + h
    :return: the possible impact points
    """
    impacted = []
    if (rectangle[0] * prependicular[0] + prependicular[1]) <= rectangle[1]:
        impacted.append((rectangle[0], rectangle[0] * prependicular[0] + prependicular[1]))

    try:
        if ((rectangle[1] - prependicular[1]) / prependicular[0]) <= rectangle[0]:
            impacted.append(((rectangle[1] - prependicular[1]) / prependicular[0], rectangle[1]))
    except ZeroDivisionError:
        pass

    try:
        if ((-prependicular[1]) / prependicular[0]) <= rectangle[0]:
            impacted.append(((-prependicular[1]) / prependicular[0], 0))
    except ZeroDivisionError:
        pass

    if prependicular[1] <= rectangle[1]:
        impacted.append((0, prependicular[1]))

    return impacted


def impact_point_two_prependucular(prependicular1: tuple, prependicular2: tuple):
    """
    :param prependicular1: (m, h) : slop and Width from the origin ; mX + h
    :param prependicular2: (m, h) : slop and Width from the origin ; mX + h
    :return: The imnpact point of these two lines
    """
    impact_x = ((prependicular2[1] - prependicular1[1]) / (prependicular1[0] - prependicular2[0]))
    impact_y = (prependicular1[0] * impact_x) + prependicular1[1]

    return impact_x, impact_y


if __name__ == '__main__':
    points = [(2, 3), (2, 6)]
    Rectangle = (6, 10)
    print(impact_prependicular_rectangle(Rectangle, find_prependicular(points)))
