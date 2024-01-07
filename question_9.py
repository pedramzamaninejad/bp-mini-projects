# پدرام زمانی نژاد
from utils.utils import insertion_sort
#  TODO : Input function, and make an era

# این تابع برا پیدا کردن سال ها با بیشترین تعداد دانشمند است
def golden_time(data: dict):
    scientists_amount = [x for x in data.values()]
    scientists_amount_sorted = insertion_sort(scientists_amount)
    most_scientists_in_era = scientists_amount_sorted[-1]  # این متغییر بیشترین تعداد دانشمندان است
    # ۳ خط پایین با کمک Chat gpt برای پیدا کردن سال هایی که بیشترین تعداد دانشمندان در آن هستند میباشد
    answer = []
    for key, val in data.items():
        if val == most_scientists_in_era:
            answer.append((key, val))

    return answer


def find_golden_time(data: list):
    # تمام سال ها در اینجا با تعداد دانشمندان ریخته میشود
    result = {}
    for i in range(0, len(data)):
        # اشخاص را برمیداریم تا از تاریخ تولد آنها را مقایسه کنیم
        target = data.pop(i)
        for j in data:
            # در چند خط پایین دانشمندانی که در تاریخ تولد این فرد زنده بوده اند حساب میشود
            # خوده شخض به دنیا امده اینجا حساب نمیشود
            try:
                if j[1] <= target[1] < j[2]:
                    if not result.get(f'{target[1]}'):
                        result[f'{target[1]}'] = 0
                    result[f'{target[1]}'] += 1
            except TypeError:
                if j[1] <= target[1]:
                    if not result.get(f'{target[1]}'):
                        result[f'{target[1]}'] = 0
                    result[f'{target[1]}'] += 1

        # در اینجا شخص مورد نظر رو که حذف کرده بودیم برمیگردانیم
        data.insert(i, target)
    for i in golden_time(result):
        print(f'Year {i[0]} was golden time with {i[1]} scientists living in that time')
    print('scientists how were borned in this year was not counted\n'
          'becouse there were nowborn babies and not a scientists')


if __name__ == '__main__':
    find_golden_time([('name', 23, 50), ('name2', 34,43), ('name3', 12, 44), ('name4', 10, 34), ('name5', 6, None)])
