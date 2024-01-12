from questions.question_1 import tajzie
from questions.question_2 import bast_factorial
from questions.question_3 import lcm
from questions.question_5 import integral
from questions.question_6 import main_idea
from questions.question_7 import permutations
from questions.question_8 import prefix_arithmetic_expression
from questions.question_9 import find_golden_time
from questions.question_10 import calc_x


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
                print(f"tajzie = {tajzie(number)}\n")
            except ValueError:
                print('\nBad Isome shienput Error\n'
                      'Try again later')
            if exit_file():
                break
        case '2':
            try:
                number = int(input('\nThis question will show you the show you Factorial Expansion\n'
                                   'Enter your chosen number: '))
                print(f"Cantor expansion = {bast_factorial(number)}\n")
            except ValueError:
                print('\nBad Input Error\n'
                      'Try again later')
            if exit_file():
                break
        case '3':
            try:
                x = list(map(int, input('\nEnter a array of numbers: ').split()))
                if len(x) < 2:
                    print(f'lcm = {x[0]}\n')
                else:
                    print(f'lcm = {lcm(*x)}\n')
            except ValueError:
                print('\nBad Input Error\n'
                      'Try again later')
            if exit_file():
                break
        case '4':
            print('Error 404: question not Found\n'
                  'unfortunately i couldnt solve this question')
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
                    print(f"answer = {answer}")
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
            print(f"permutations are:\n{permutations(char)}")
            if exit_file():
                break

        case '8':
            expression_raw = input('\nEnter your expression\n'
                               'Im counting on you that you know how to write these expressions\n'
                               'An example is [* + 2 3 - 9 4]'
                               'Again please separate them with a blank space: ').split()
            expression = []
            for i in expression_raw:
                expression.insert(0, i)
            print(f"The answer of this expression is :\n{prefix_arithmetic_expression(expression)}")
            if exit_file():
                break

        case '9':
            n = int(input('\nHow meny sceintists do you want to Enter: \n'))
            data = []
            for i in range(n):
                s = input('Enter the sceintist and birth date and death date like\n'
                          'pedram 2004 2023\n'
                          'If the sceintist is not dead yet enter it like\n'
                          'pedram 2004\n'
                          'If other than this two options were given the scientist will not be added\n').split()
                if len(s) == 3:
                    data.append(s)
                elif len(s) == 2:
                    s.append(None)
                    data.append(s)
            find_golden_time(data)
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
                counter = 1
                while counter < 11:
                    answer_matrix = list(map(int, input(f'\nEnter the answer matrix with {n} numbers\n'
                                               f'separate with blank space: ').split()))
                    if len(answer_matrix) == n:
                        break
                    else:
                        print('\nBad input try again\n'
                              f'You have {10 - counter} try left')
                    if exit_file():
                        break
                print(coefficient_matrix, answer_matrix)
                print('befor going thoro')
                print(calc_x(coefficient=coefficient_matrix, answer=answer_matrix))
            except ValueError:
                print('\nBad input try again late')

            if exit_file():
                break
