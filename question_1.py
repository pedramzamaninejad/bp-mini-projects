def tajzie(number):
    avamel = {}
    # تست کردن تمام اعداد کمتر از نصف زیرا اگر عددی برای مثال به دو بخش پذیر باشد
    # پس بقیه عوامل آن هم کمتر از مکمل دو است
    for i in range(2, number // 2 + 1):
        reminder = True
        # این لوپ برای چک کردن این که ایا عدد تست شده به عدد گرفته شده توسط کاربر بخش پذیر است یا خیر
        # تا وقتی تمام ضریب های این توابع پیدا نشده سراغ چک کردن عدد بعدی نمی رود
        while reminder:
            # وقتی عدد مورد نظر به یک میرسد پی دیگر عامل دیگری ندارد و میتوان جواب را برگرداند
            if number == 1:
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
