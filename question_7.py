
from utils.utils import insertion_sort_str

def permutaions(data: list):
    result = [x for x in data]
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            result.append(data[i] + data[j])
            result.append(data[j] + data[i])
    counter = 2
    perm_count = len(data)
    while counter < len(data):
        for i in range(perm_count, len(result)):
            temp = [x for x in data]
            for r in result[i]:
                temp.remove(r)
            for j in range(len(temp)):
                result.append(result[i] + temp[j])
                result.append(temp[j] + result[i])
        # Delete duplicate
        perm = 1
        for i in range(counter):
            perm *= len(data) - i
        perm_count += perm
        counter += 1

    result = insertion_sort_str(list(set(result)))
    return result


if __name__ == '__main__':
    a = ['a', 'b', 'c', 'd']
    c = permutaions(a)
    print(len(c) == 64)