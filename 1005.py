def get_set(numbers):
    tmp = []
    while True:
        if numbers == 1:
            tmp.append(1)
            break
        numbers = numbers // 2 if numbers % 2 == 0 else (numbers * 3 + 1) // 2
        tmp.append(numbers)
    return set(tmp)


# for the given input "number", find all its path number and return the set they form

total_number = int(input())
while total_number:
    num_strs = input().split(' ')
    result = set([int(num) for num in num_strs])  # result is the set of all input numbers
    for num in num_strs:
        num_set = get_set(int(num))
        result = result.difference(num_set)  # use the difference with all path number sets
        total_number -= 1  # loop control

result = list(result)
result.sort(reverse=True)
result = [str(val) for val in result]
print(' '.join(result))

'''
total_num = int(input())
total_list = [input()]

sep_list = total_list[0].split(" ")
sep_list_1 = []
for a in range(total_num):
    sep_list_1.append(int(sep_list[a]))
#sep_list is the list contain all numbers requiring validation in format str
#sep_list_1 is the sep_list whose components are in format int

sep_list_1.sort(reverse=False)
num_set = set(sep_list_1)
result = []
compare_set = {sep_list_1[0]}
compare_set_1 = {sep_list_1[0]}

for n in sep_list_1:
    if n not in compare_set_1:
        result.append(n)
    compare_set.add(n)
    while n > 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int((3 * n + 1) / 2)
        compare_set.add(n)
    compare_set_1 = compare_set.copy()

result.sort(reverse=True)
for a in range(len(result)):
    result[a] = str(result[a])
print(' '.join(result))
'''
# mistake: only valid for later numbers
