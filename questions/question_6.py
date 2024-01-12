# پدرام زمانی نژاد


def find_prependicular(point_one: tuple, point_two: tuple):
    """
    :param point_one: first point ; (x1, y1)
    :param point_two: second point ; (x2, y2)
    :return: (m, h) : slop and Width from the origin ; mX + h
    """
    mid_x = (point_one[0] + point_two[0]) / 2
    mid_y = (point_one[1] + point_two[1]) / 2
    try:
        prependicular_slop = (-1) / ((point_one[1] - point_two[1]) / (point_one[0] - point_two[0]))
    except ZeroDivisionError:
        # checking for infinity slop
        if point_one[1] - point_two[1] == 0:
            return ((point_two[0] + point_two[0]) / 2, )
        prependicular_slop = 0
    # عرض از مبدا
    h = mid_y - (prependicular_slop * mid_x)
    print(prependicular_slop, h)
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

    for i in impacted:
        if i[0] > rectangle[0] or i[1] > rectangle[1] or i[0] < 0 or i[1] < 0:
            impacted.remove(i)

    return impacted


def impact_prependucular(prependicular1: tuple, prependicular2: tuple):
    """
    :param prependicular1: (m, h) : slop and Width from the origin ; mX + h
    :param prependicular2: (m, h) : slop and Width from the origin ; mX + h
    :return: The impact point of these two lines
    """
    impact_x = ((prependicular2[1] - prependicular1[1]) / (prependicular1[0] - prependicular2[0]))
    impact_y = (prependicular1[0] * impact_x) + prependicular1[1]

    return impact_x, impact_y


def main_idea(points: list, rectangle: tuple):
    """
    :param points: the points cordinents
    :param rectangle: the rectangle top left cordinent
    :return: چند ضلعی
    """
    prependicular = []
    for i in range(len(points)):
        try:
            prependicular.append(find_prependicular(points[i], points[i + 1]))
        except IndexError:
            prependicular.append(find_prependicular(points[i], points[0]))
    importans_point = impact_prependucular(prependicular[0], prependicular[1])
    impacts = [impact_prependicular_rectangle(rectangle, prependicular[x]) for x in range(len(prependicular))]
    for i in range(len(impacts)):
        thrid_point = (i + 2) % len(impacts)  # نقطه مورد نیازه سوم برای مقایسه فاصله برخورد عمود منصف
        for j in range(len(impacts[i])):
            # مقایسه فاصله نقطه ای که از ان عمود منصف بدست اومده و نقطه ی سوم
            distance1_1 = ((impacts[i][j][0] - points[thrid_point][0]) ** 2 + (impacts[i][j][1] - points[thrid_point][1]) ** 2) ** 0.5
            distance1_2 = ((impacts[i][j][0] - points[i][0]) ** 2 + (impacts[i][j][1] - points[i][1]) ** 2) ** 0.5
            if distance1_1 < distance1_2:
                impacts[i].pop(j)
                break
    all_points = [importans_point, (0, 0), (0, rectangle[1]), (rectangle[0], 0), rectangle]
    for i in impacts:
        for j in i:
            all_points.append(j)

    print(f'Points --> {all_points}')
    print(f'میدانستم چگونه نقطه ها رو جدا کنم')


if __name__ == '__main__':
    points = [(2, 3), (2, 6), (4, 7)]
    Rectangle = (6, 10)
    main_idea(rectangle=Rectangle, points=points)
    # print(find_prependicular(points[0], points[1]))
    # print(find_prependicular((2, 3), (4, 3)))
