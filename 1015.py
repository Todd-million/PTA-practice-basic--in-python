def class_division(total_student, threashold_1, threashold_2, de_score, talent_score):
    rank = []
    for a in range(total_student):
        if de_score[a] > threashold_2 and talent_score > threashold_2:
            rank.append(1)
        elif de_score[a] < threashold_1 and talent_score < threashold_1:
            rank.append(5)
        elif


info_input = input().split(" ")
total_student = int(info_input[0])
minimum_score = int(info_input[1])
prior_score_h = int(info_input[2])

license_num = []
de_score = []
talent_score = []
all_info = []

a: int
for a in range(total_student):
   all_info = input().split(" ")
   license_num.append(int(all_info[0]))
   de_score.append(int(all_info[1]))
   talent_score.append(int(all_info[2]))

