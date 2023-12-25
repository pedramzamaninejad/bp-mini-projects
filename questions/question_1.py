def tajzie(number):
    avamel = {}
    for i in range(2, int(number ** 1/2) + 1):
        reminder = True
        while reminder:
            if number == 0:
                return avamel

            elif number % i == 0:
                number /= i
                if avamel.get(f'{i}'):
                    avamel[f'{i}'] += 1
                else:
                    avamel[f'{i}'] = 1
            else:
                reminder = False
    return avamel


if __name__ == "__main__":
    from time import time

    n = int(input('Please enter a number: '))
    t1 = time()
    result = tajzie(n)
    t2 = time()

    print(result, f'time: {t2 - t1}')
