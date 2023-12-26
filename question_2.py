from utils.utils import factorial as fk


# اینجا ما بزرگترین فاکتوریلی که کوچکتر از عدد هست را محاسبه میکنیم
def min_factorial(number):
    i = 1
    while True:
        if number < fk(i):
            break
        i += 1
    return i - 1


def bast_factorial(number):
    avamel = {}  # { تعداد ,فاکتوریل}
    current_min_factorial = min_factorial(number)
    while current_min_factorial != 0:
        # اگر هیچ بار فاکتوریل تکرار نشده باشد نشان ندهیم
        if number // fk(current_min_factorial) == 0:
            current_min_factorial -= 1

        else:
            avamel[f'{current_min_factorial}!'] = number // fk(current_min_factorial)
            number %= fk(current_min_factorial)
            current_min_factorial -= 1

    return avamel


if __name__ == '__main__':
    print(bast_factorial(1000))
