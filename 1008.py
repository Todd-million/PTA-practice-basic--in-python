(total_num, start_num) = input().split(" ")
origin_list = input().split(" ")
total_num_1 = int(total_num)
start_num_1 = int(start_num)

if total_num_1 < start_num_1:
    start_num_1 = start_num_1 % total_num_1
moved_list = []

if total_num_1 > start_num_1:
    for a in range(total_num_1 - start_num_1, total_num_1):
        moved_list.append(str(origin_list[a]))

    for b in range(total_num_1 - start_num_1):
        moved_list.append(str(origin_list[b]))
else:
    for c in range(total_num_1):
        moved_list.append(str(origin_list[c]))

result = " ".join(moved_list)
print(result)

#debug needed
"""
n,m = map(int,input().split())
num1 = list(input().split())

num2 = []
for i in range(n):
    place = (i+m)%n
    num2.insert(place,num1[i])

print(' '.join(num2))
"""