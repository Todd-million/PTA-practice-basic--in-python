str_num = int(input())
str_list = []
n_1 = 0
n_2 = 0

for count in range(str_num):
    str_list.append(input())

for count in range(str_num):
    if "A" not in str_list[count]:
        n_1 = str_list[count].find('P')
        n_2_1 = str_list[count].find('T')
        n_2 = n_2_1 - n_1
        n_3 = len(str_list[count]) - n_2_1
        if n_3 - n_1 * n_2 != 0 or n_2 - n_1 == 1:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')

need debug