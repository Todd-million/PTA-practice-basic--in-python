#method 1

student_number = int(input())

full_info_list = []
name_list = []
serialnum_list = []
score_list = []

for a in range(student_number):
    full_info_list.append(input())
    split_list = full_info_list[a].split(" ")
    name_list.append(split_list[0])
    serialnum_list.append(split_list[1])
    score_list.append(int(split_list[2]))

max_index = score_list[:].index(max(score_list))
min_index = score_list[:].index(min(score_list))

print(name_list[max_index] + ' ' + serialnum_list[max_index])
print(name_list[min_index] + ' ' + serialnum_list[min_index])
