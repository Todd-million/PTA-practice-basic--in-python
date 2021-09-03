#taking polynomial derivatives
coefficient_list = []
exponential_list = []
all_num = input().split(" ")
loop_time = len(all_num)

for a in range(loop_time):
    if a % 2 == 0:
        coefficient_list.append(int(all_num[a]))
    else:
        exponential_list.append(int(all_num[a]))

loop_time_2 = len(exponential_list)
new_coefficient_list = []
new_exponential_list = []

for a in range(loop_time_2):
    if exponential_list[a] != 0 and coefficient_list[a] != 0:
        new_coefficient_list.append(exponential_list[a] * coefficient_list[a])
        new_exponential_list.append(exponential_list[a] - 1)
    else:
        continue

new_all_num = []
new_list_len = len(new_exponential_list)
for a in range(new_list_len):
    new_all_num.append(str(new_coefficient_list[a]))
    new_all_num.append(str(new_exponential_list[a]))

result = " ".join(new_all_num)
print(result,end="")

#debug needed