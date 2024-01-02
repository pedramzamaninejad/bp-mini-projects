def tajzie(number):
    avamel = {}
    original_num = number
    while number % 2 == 0:
        if not avamel.get('2'):
            avamel['2'] = 0
        avamel['2'] += 1
        number /= 2
    # تست کردن تمام اعداد کمتر از نصف زیرا اگر عددی برای مثال به دو بخش پذیر باشد
    # پس بقیه عوامل آن هم کمتر از مکمل دو است
    for i in range(3, int(original_num / 2) + 1, 2):
        # این لوپ برای چک کردن این که ایا عدد تست شده به عدد گرفته شده توسط کاربر بخش پذیر است یا خیر
        # تا وقتی تمام ضریب های این توابع پیدا نشده سراغ چک کردن عدد بعدی نمی رود
        # وقتی عدد مورد نظر به یک میرسد پی دیگر عامل دیگری ندارد و میتوان جواب را برگرداند
        while True:
            if number == 1:
                return avamel
            temp_num = number / i
            if f'{temp_num}'[-1] == '0':
                if not avamel.get(f'{i}'):
                    avamel[f'{i}'] = 0
                avamel[f'{i}'] += 1
                number = temp_num
            else:
                break

    return avamel


if __name__ == "__main__":
    n = int(input('Please enter a number: '))
    result = tajzie(n)

    print(result)
