from utils.utils import insertion_sort


#  TODO : Input function

# این تابع برا پیدا کردن سال ها با بیشترین تعداد دانشمند است
def golden_time(data: dict):
    scientists_amount = list(data.values())
    scientists_amount_sorted = insertion_sort(scientists_amount)
    most_scientists_in_era = scientists_amount_sorted[-1]  # این متغییر بیشترین تعداد دانشمندان است
    # ۴ خط پایین با کمک Chat gpt برای پیدا کردن سال هایی که بیشترین تعداد دانشمندان در آن هستند میباشد
    answer = []
    for key, val in data.items():
        if val == most_scientists_in_era:
            answer.append((key, val))
    # در بلاک پایین دوره ی این دانشمندان را پیدا کنیم
    # اساس این قطعه این است که اگر دوسالی که پیدا میشود پشت هم باشند پس ایندکس این دو سال اختلاف یک دارند
    # در غیر این صورت سالی یا سال هایی بوده که این ها سالها را از هم جدا کرده است
    era = []
    years = insertion_sort(list(data.keys()))
    for i in range(len(answer) - 1):
        try:
            start_era = years.index(answer[i][0])
            stop_era = years.index(answer[i + 1][0])
            if stop_era - start_era == 1:
                era.append((answer[i], answer[i + 1]))
        except IndexError:
            pass
    # اگر دوره ای وجود داشته باشد
    if era:
        return era
    # اگر دوره ای وجود نداشته باشد
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
            # مقایسه تاریخ تولدشان
            try:
                if j[1] <= target[1] < j[2]:
                    if not result.get(target[1]):
                        result[target[1]] = 0
                    result[target[1]] += 1
            except TypeError:
                if j[1] <= target[1]:
                    if not result.get(target[1]):
                        result[target[1]] = 0
                    result[target[1]] += 1
        # اگر تاریخ فوت یکی با تریخ تولد بکی دیگه تداخل داشته باشه
        #  پس فقط کافیه به اون تاریخ اضافه بشه
        if result.get(target[2]):
            result[target[2]] += 1
        else:
            if not target[2] is None:
                result[target[2]] = 1
                for j in data:
                    # مقایسه تاریخ مرگ
                    try:
                        if j[1] < target[2] <= j[2]:
                            result[target[2]] += 1
                    except TypeError:
                        if j[1] < target[2]:
                            result[target[2]] += 1

        # در اینجا شخص مورد نظر رو که حذف کرده بودیم برمیگردانیم
        data.insert(i, target)
    for i in golden_time(result):
        try:
            print(f"\nThe golden era was started from [{i[0][0]}] and ended in [{i[1][0]}]\n"
                  f"In this era there were [{i[0][1]}] scientists alive or died in these year\n")
        except TypeError:
            print(f'\nThere are no era with given data but this year [{i[0]}] is the year witch most scientists were alive\n')
        print("not included the baby scientist")


if __name__ == '__main__':
    find_golden_time([('name', '23', '50'), ('name2', '34', '43'), ('name3', '12', '44'), ('name4', '10', '34'),
                      ('name5', '6', None)])
