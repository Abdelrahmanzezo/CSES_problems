def find_missing_num(n):
    numbers = set(n)
    result = []
    for i in range(1,n[-1]):
        if i not in numbers:
            result.append(i)
    return result
list_of_missing_nums = [1, 2, 10]
print(find_missing_num(list_of_missing_nums))
