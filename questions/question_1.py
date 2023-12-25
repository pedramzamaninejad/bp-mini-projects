def tajzie(number):
    avamel = {}
    for i in range(2, number):
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
    n = int(input('Please enter a number: '))
    result = tajzie(n)

    print(result)
