# پدرام زمانی نژاد‍
from question_1 import tajzie
from question_2 import bast_factorial
from question_3 import lcm
from question_5 import integral
from question_6 import main_idea
from question_7 import permutations
from question_8 import prefix_arithmetic_expression
from question_9 import find_golden_time
from question_10 import calc_x


def exit_file():
    done = input('\nif you dont want to check any other question!\n'
                 'please type --> Done\n'
                 'if you want to check other question just press any other key\n'
                 'Enter what you want to do\n').lower()
    if done == 'done':
        return True
    return False


while True:
    n = input('\nChoose from 1 to 10 depending of which question you want to answer:\n')
    match n:
        case '1':
            try:
                number = int(input('\nthis question will show you the Prime factorization of an integer\n '
                                   'Enter your chosen number: '))
                print(tajzie(number))
            except ValueError:
                print('\nBad Input Error\n'
                      'Try again later')
            if exit_file():
                break
        case '2':
            try:
                number = int(input('\nThis question will show you the show you Factorial Expansion\n'
                                   'Enter your chosen number: '))
                print(bast_factorial(number))
            except ValueError:
                print('\nBad Input Error\n'
                      'Try again later')
            if exit_file():
                break
        case '3':
            try:
                x = list(map(int, input('\nEnter a array of numbers: ').split()))
                print(lcm(*x))
            except ValueError:
                print('\nBad Input Error\n'
                      'Try again later')
            if exit_file():
                break
        case '4':
            print('Error 404: question not Found')
            if exit_file():
                break

        case '5':
            try:
                start = float(input('\nEnter the start point: '))
                stop = float(input('\nEnter the stop point: '))
                part = int(input('\nHow meny part do you want to split the start stop point?\n'
                                 '[More part will be more accurate]: '))
                while True:
                    functions = input('\nChose you function:\n[sin - sqrt - poly]: ')
                    answer = integral(start, stop, part, functions)
                    if answer is None:
                        print('\nBad input function chose one of the given one: ')
                        continue
                    print(answer)
                    break
            except ValueError:
                print('\nBad Input with your start - stop - part inputs!\n'
                      'try again later')
            if exit_file():
                break
        case '6':
            try:
                main_point = tuple(map(int, input('\nEnter the top right point coordinates of rectangular!\n'
                                                  'with type of | x, y: ').split()))
                print('\nfor lack of algorithm this will work for 3 points the best so were will be 3 more input\n'
                      'with type of | x, y')
                store_point = []
                for i in range(3):
                    print('\nYou are entering STORE POINTS')
                    store_point.append(tuple(map(int, input('\nEnter the store point\n'
                                                            'with type of | x, y: ').split())))
                    print(f'\n{3 - (i + 1)} store point remaining')
                main_idea(store_point, main_point)
            except ValueError:
                print('\nError Bad input\n'
                      'Try again later')
            if exit_file():
                break
        case '7':
            char = input('\nHow meny character do you want to write permutations for ?\n'
                         'Enter them here via separation of one blank space: ').split()
            print(permutations(char))
            if exit_file():
                break

        case '8':
            expression = input('\nEnter your expression\n'
                               'Im counting on you that you know how to write these expressions\n'
                               'An example is [* + 2 3 - 9 4]'
                               'Again please separate them with a blank space: ').split()
            print(prefix_arithmetic_expression(expression))
            if exit_file():
                break

        case '9':
            if exit_file():
                break

        case '10':
            try:
                coefficient_matrix = []
                n = int(input('\nEnter the matrix level it will be an square matrix: '))
                for i in range(1, n + 1):
                    counter = 1
                    while counter < 11:
                        rows = list(map(int, input(f'\nEnter the row number {i}\n'
                                                   f'separate with blank space: ').split()))
                        if len(rows) == n:
                            coefficient_matrix.append(rows)
                            break
                        else:
                            print('\nBad input try again\n'
                                  f'You have {10 - counter} try left')
                            counter += 1
                        if exit_file():
                            break
                answer_matrix = []
                counter = 1
                while counter < 11:
                    rows = list(map(int, input(f'\nEnter the answer matrix with {n} numbers\n'
                                               f'separate with blank space: ').split()))
                    if len(rows) == n:
                        coefficient_matrix.append(rows)
                        break
                    else:
                        print('\nBad input try again\n'
                              f'You have {10 - counter} try left')
                    if exit_file():
                        break
                print(calc_x(coefficient_matrix, answer_matrix))
            except ValueError:
                print('\nBad input try again late')

            if exit_file():
                break
