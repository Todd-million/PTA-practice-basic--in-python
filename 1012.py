user_input_list = input().split(" ")
user_input_list = [int(a) for a in user_input_list]
total_input = user_input_list[0]

a_1 = []
a_2 = []
a_3 = []
a_4 = []
a_5 = []
for a in range(1, total_input + 1):
    residual = user_input_list[a] % 5
    if residual == 0:
        if user_input_list[a] % 2 == 0:
            a_1.append(user_input_list[a])
    elif residual == 1:
        a_2.append(user_input_list[a])
    elif residual == 2:
        a_3.append(user_input_list[a])
    elif residual == 3:
        a_4.append(user_input_list[a])
    else:
        a_5.append(user_input_list[a])

result = []
if len(a_1) == 0:
    result.append("N")
else:
    result.append(str(sum(a_1)))

if len(a_2) == 0:
    result.append("N")
else:
    (sum_1, sum_2) = (0, 0)
    for a in range(0, len(a_2), 2):
        sum_1 += a_2[a]
    for a in range(1, len(a_2), 2):
        sum_2 += a_2[a]
    result.append(str(sum_1 - sum_2))

if len(a_3) == 0:
    result.append("N")
else:
    result.append(str(len(a_3)))

if len(a_4) == 0:
    result.append("N")
else:
    a = round(sum(a_4) / len(a_4), 1)
    result.append(str(a))
    # result.append('%0.1f' % a)

if len(a_5) == 0:
    result.append("N")
else:
    result.append(str(max(a_5)))

print(" ".join(result))
