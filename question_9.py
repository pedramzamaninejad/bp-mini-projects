from utils.utils import insertion_sort
# TODO : i user box plot for this question
# INPUT TYPE: { NAME: {BIRHT: ... , DEATH: ...}}


def get_golden_time(data: dict):
    all_years = []
    for name in data:
        all_years.append(data.get(name).get('birth'))
        all_years.append(data.get(name).get('death'))

    # removing None data from aour data
    none_count = all_years.count(None)
    for i in range(none_count):
        all_years.remove(None)

    all_years = insertion_sort(all_years)

    # i used box plot method
    q1 = int(len(all_years) / 4)
    q3 = int((len(all_years) * 3) / 4)

    return f'Golden time: from {all_years[q1]} all the way to {all_years[q3]}'
