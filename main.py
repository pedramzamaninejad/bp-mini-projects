# پدرام زمانی نژاد‍
from question_1 import tajzie
from question_2 import bast_factorial
from question_3 import lcm
from question_9 import find_golden_time
from question_5 import integral


n = input('Choose from 1 to 10 depending of which question you want to answer: ')


match n:
    case '1':
        number = int(input('this question will show you the Prime factorization of an integer\n '
                           'Enter your choosen number: '))
        print(number)
    case '2':
        number = int(input('This question will show you the show you Factorial Expansion\n'
                           'Enter your choosen number: '))
        print(number)
    case '3':
        x = list(map(int, input('Enter a array of numbers: ').split()))
        print(*x)

    case '4':
        ...

    case '5':
        ...

    case '6':
        ...

    case '7':
        ...

    case '8':
        ...

    case '9':
        ...

    case '10':
        ...
