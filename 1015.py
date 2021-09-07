'''
def class_division(total_student, threashold_1, threashold_2, student_info):
    rank_1 = 0
    rank_2 = 0
    rank_3 = 0
    rank_4 = 0
    for a in range(total_student):
        if student_info[a][1] > threashold_2 and student_info[a][2] > threashold_2:
            student_info[a].append("1")
            rank_1 += 1
        elif student_info[a][1] < threashold_1 and student_info[a][2] < threashold_1:
            student_info[a].append("5")
        elif student_info[a][1] > threashold_2 > student_info[a][2] > threashold_1:
            student_info[a].append("2")
            rank_2 += 1
        elif threashold_1 < student_info[a][2] < student_info[a][1] < threashold_2:
            student_info[a].append("3")
            rank_3 += 1
        else:
            student_info[a].append("4")
            rank_4 += 1

    return [rank_1, rank_2, rank_3, rank_4, student_info]


info_input = input().split(" ")
total_student = int(info_input[0])
minimum_score = int(info_input[1])
prior_score_h = int(info_input[2])

all_info = []
for a in range(total_student):
    temp_info = input().split(" ")
    temp_info_1 = []
    for b in temp_info:
        temp_info_1.append(int(b))
    all_info.append(temp_info_1)
all_info.append([])

[rk_1, rk_2, rk_3, rk_4, all_info] = class_division(total_student, minimum_score, prior_score_h, all_info)

print(all_info)

all_info_1 = sorted(all_info, key=lambda x:x[3])

# all_info.sort(key=lambda x:x[3])
'''


def rank(x):
    return x[3], int(x[1]), -int(x[0])


a = [int(i) for i in input().split()]
n = a[0];
l = a[1];
h = a[2]
a = [];
b = [];
c = [];
d = []
for i in range(n):
    x = input().split()
    if int(x[1]) < l or int(x[2]) < l:
        continue
    x.append(int(x[1]) + int(x[2]))
    if int(x[1]) >= h and int(x[2]) >= h:
        a.append(x)
    elif int(x[1]) >= h > int(x[2]):
        b.append(x)
    elif h > int(x[1]) >= int(x[2]) and int(x[2]) < h:
        c.append(x)
    else:
        d.append(x)
a = sorted(a, key=rank, reverse=True)
b = sorted(b, key=rank, reverse=True)
c = sorted(c, key=rank, reverse=True)
d = sorted(d, key=rank, reverse=True)
e = a + b + c + d
print(len(e))
for i in e:
    print(' '.join(i[:-1]))

# debug needed