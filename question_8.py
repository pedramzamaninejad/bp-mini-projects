# پدرام زمانی نژاد
# لطفا در مورد چگونگی حل این سوال حضوری سوال شود توضیح به شدت سخت میباشد
def prefix_arthmetic_expression(a):
    index = 2
    first_index = 0
    counter = 0
    while len(a) != 1:
        b = a[index]
        try:
            b = int(b)
            if counter != 0:
                index += 1
                first_index += 1
                counter = 0
            continue
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
            counter = 1
            first_index = 0
            index = 2
    return a[0]
