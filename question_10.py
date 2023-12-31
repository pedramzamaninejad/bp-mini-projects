def det(data: list):
    if len(data) == 2:
        return (data[0][0] * data[1][1]) - (data[0][1] * data[1][0])

    result = 0
    for j in range(len(data)):
        temp_data = [x[:] for x in data]
        a0j = temp_data[0][j]
        temp_data.pop(0)
        for i in range(len(temp_data)):
            temp_data[i].pop(j)
        result += ((-1) ** j) * a0j * det(temp_data)

    return result

def calc_x(coeffient, answer):
    det_of_coeffient = det(coeffient)
    detan = []
    for i in range(len(answer)):
        temp_co = [x[:] for x in coeffient]
        for j in temp_co:
            j[i] = answer[i]
        try:
            detan.append(f'x{i} = {det(temp_co) / det_of_coeffient}')
        except ZeroDivisionError as e:
            return f'The is no possible answer for this problem\nError: {e}'
    return detan


if __name__ == '__main__':
    zaraieb = [
        [2, 3, 4],
        [3, 4, 2],
        [3, 4, 5]
    ]
    javab = [5, 12, 7]
    print(calc_x(zaraieb, javab))
