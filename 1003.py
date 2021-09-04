str_num = int(input())
str_list = []
n_1 = 0
n_2 = 0

for count in range(str_num):
    str_list.append(input())

for count in range(str_num):
    if "A" in str_list[count] and "P" in str_list[count] and "T" in str_list[count]:
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

#the question is ambiguous in description

"""

def test(a):
    x = -1
    y = -1
    for i in range(len(a)):#找出P，T的位置
        if (a[i]=='P'):
            x = i
        if (a[i]=='T'):
            y = i
    if (x==-1 or y==-1):#如果找不到P，T则返回0
        return 0
    if (x>y):#P在T的后面，返回0
        return 0
    if (y==x+1):#P，T之间没有字符，返回0
        return 0
    if (x!=0):#字符串不以P开头
        b = a[0:x]
    else:#字符串以P开头
        b = []
    c = a[x+1:y]
    if (y!=len(a)-1):#字符串不以T结尾
        d = a[y+1:len(a)]
    else:#字符串以T结尾
        d = []
    for i in b:#判断各个分段是否是字符A组成
        if (i!='A'):
            return 0
    for i in c:
        if (i!='A'):
            return 0
    for i in d:
        if (i!='A'):
            return 0
    if (d==b*len(c)):#条件判断
        return 1
    else:
        return 0

n = input()
for i in range(int(n)):
    s = input()
    if (test(s)==1):
        print('YES')
    else:
        print("NO")
        
"""