# پدرام زمانی نژاد


def permutations(data: list):
    # تمام حالات با یک حرف
    result = [x for x in data]
    # تمام حالات با دو حرف با ترکیب یک حرفی ها
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            result.append(data[i] + data[j])
            result.append(data[j] + data[i])
    counter = 2  # بعدا با روابط جایگشت ها بدون تکرار تعدا جایگشت های بدست آمده حساب میشود
    perm_count = len(data)  # تعداد جایگشت های با یک حرف
    while counter < len(data):
        # این قسمت هر حالت ۲ حرفی با یک حالت تک حرفی جمع میشود و به حالات مورد نیاز خودش و برعکسش اضافه میشود
        for i in range(perm_count, len(result)):
            # برای پیدا کردن حروف غیر تکراری
            temp = [x for x in data]
            for r in result[i]:
                temp.remove(r)
            for j in range(len(temp)):
                result.append(result[i] + temp[j])
        # Delete duplicate
        # پیدا کردن تعداد جایگشت ها برای مثال اگر ۴ حرف داشته باشیم و جایگشت های ۳ تایی را بدست اورده باشیم با این
        # قطعه کد میتوانیم تعداد آن جایگشت هارا بدست آورین
        # نحوه ی کار : ۳ تا جای خالی داریم پس جایگشت انها برابر با ==> ۲*۳*۴ خواهد بود
        perm = 1
        for i in range(counter):
            perm *= len(data) - i
        perm_count += perm
        counter += 1

    return result


if __name__ == '__main__':
    a = ['a', 'b', 'c', 'd']
    c = permutations(a)
    print(len(c) == 64)
