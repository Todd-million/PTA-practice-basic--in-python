test_total = int(input())
all_list = []
temp_list = []
for i in range(test_total):
    temp_list = input().split(" ")
    temp_list = [int(a) for a in temp_list]
    all_list.append(temp_list)

# all_list contains test_total lists in total

result = []
for i in range(test_total):
    if all_list[i][0] + all_list[i][1] > all_list[i][2]:
        result.append("Case #" + str(i+1) + ": true")
    else:
        result.append("Case #" + str(i+1) + ": false")

print("\n".join(result),end="")
