dict_1 = {'0': "ling", '1': 'yi', '2': 'er', '3': 'san', '4': 'si', '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba',
          '9': 'jiu'}

input_sum = input()
all_sum = 0
count = 0

for var in input_sum:
    all_sum += int(var)

string_len = len(str(all_sum))

for var in str(all_sum):
    count += 1
    if count != string_len:
        print(dict_1[var] + ' ', end='', sep='')
    else:
        print(dict_1[var], end='', sep='')
