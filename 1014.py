"""
def time_format(input_num):
    input_num_str = "0" + str(input_num)
    return input_num_str


dict_day = {"A": "MON", "B": "TUE", "C": "WED", "D": "THU", "E": "FRI", "F": "SAT", "G": "SUN"}
dict_time_append = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20,
                    "L": 21, "M": 22, "N": 23}

input_str = []
while len(input_str) != 4:
    input_str.append(input())

uppercase_1 = []
uppercase_2 = []
lowercase_3 = []
lowercase_4 = []

for a in input_str[0]:
    if a.isupper():
        uppercase_1.append(a)
for a in input_str[1]:
    if a.isupper():
        uppercase_2.append(a)

for b in input_str[2]:
    lowercase_3.append(b)
for b in input_str[3]:
    lowercase_4.append(b)

result_week = []
for a in uppercase_1:
    if a in uppercase_2:
        result_week.append(a)

result_min = []
for b in range(len(lowercase_3)):
    if lowercase_3[b] == lowercase_4[b]:
        if lowercase_3[b].isalpha():
            result_min.append(b)

if result_week[1].isalpha():
    print(dict_day[result_week[0]] + " " + str(dict_time_append[result_week[1]]) + ":" + time_format(result_min[0]))
else:
    print(dict_day[result_week[0]] + " " + time_format(result_week[1]) + ":" + time_format(result_min[0]))
"""
# debug needed


week = {'A': 'MON',
        'B': 'TUE',
        'C': 'WED',
        'D': 'THU',
        'E': 'FRI',
        'F': 'SAT',
        'G': 'SUN'}
num0to9 = [str(i) for i in range(0, 10)]

letterAtoN = [chr(i) for i in range(65, 79)]
# chr()函数用于生成相应ASCII码对应的字符
# A/N的ASCII码分别是65/79

num0to23 = ['{:0>2}'.format(str(i)) for i in range(0, 24)]
# 生成00~23，format格式化函数实现个位数的补位

hour = dict(zip(num0to9 + letterAtoN, num0to23))
# zip()函数用于将两个列表合并
# 在hour中，num0to9+letterAtoN为索引，num0to23为对应元素

rst = ''
# rst用于保存结果，初始化为空串

a = []
for i in range(0, 4):
    a.append(input())  # 接受4行的输入

for i in range(0, len(a[0])):  # 星期
    if a[0][i] in week and a[0][i] == a[1][i]:
        rst += (week[a[0][i]] + ' ')
        break  # 检测到星期后加空格，并及时跳出

for j in range(i + 1, len(a[0])):
    # 在上一步检测星期的基础上继续寻找小时
    # 遍历的初始位置=上一步星期的位置+1
    if a[0][j] in hour and a[0][j] == a[1][j]:
        rst += (hour[a[0][j]] + ':')
        break

for k in range(0, len(a[2])):
    if a[2][k] == a[3][k]:
        if ('A' <= a[2][k] <= 'Z') or ('a' <= a[2][k] <= 'z'):
            # 相同字符为字母
            rst += '{:0>2}'.format(str(k))
            # 格式化字符串，个位数以'0'补位
            break
print(rst)
