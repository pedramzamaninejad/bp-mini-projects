def prefix_arithmetic_expression(a):
    index = 2
    first_index = 0
    while len(a) != 1:
        b = a[index]
        try:
            b = int(b)
            index += 1
            first_index += 1
        except ValueError:
            first = int(a.pop(first_index))
            second = int(a.pop(first_index))
            if b == '-':
                a.remove('-')
                temp = second - first
                a.insert(first_index, temp)
            elif b == '+':
                a.remove('+')
                temp = second + first
                a.insert(first_index, temp)
            elif b == '*':
                a.remove('*')
                temp = second * first
                a.insert(first_index, temp)
            elif b == '/':
                a.remove('/')
                temp = second / first
                a.insert(first_index, temp)
            elif b == '//':
                a.remove('//')
                temp = second // first
                a.insert(first_index, temp)
            elif b == '**':
                a.remove('**')
                temp = second ** first
                a.insert(first_index, temp)
            first_index = 0
            index = 2
    return a[0]


if __name__ == '__main__':
    x = input().split()
    expression = []
    for i in x:
        expression.insert(0, i)
    prefix_arithmetic_expression(expression)