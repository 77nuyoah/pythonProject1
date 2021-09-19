import re

keyword_list = ['auto','break','case','char','const','continue','default','do',
                'double','else','enum','extern','float','for','goto','if',
                'int','long','register','return','short','signed','sizeof',
                'static','struct','switch','typedef','union','unsigned',
                'void','volatile','while']


filepath = input("代码文件的路径:")
degree = eval(input("完成等级（从低到高为1，2，3，4）:"))

code = []
with open(filepath, 'r' ) as f:
    for line in f:
        code.append(line)
f.close()
text = "".join(code)

reg = r'\b[a-zA-Z]+\b'
line = re.findall(reg, text)

def switch_count():
    switch_num = 0
    switch_flag = 0
    case_num = []
    if line.count('switch') == 0:
        print('switch num: 0')
        return 0

    for kw in line:
        if kw == 'switch':
            switch_num += 1
            switch_flag = 1
            case_num.append(0)
        if switch_flag == 1 and kw == 'case':
            case_num[switch_num-1] += 1

    print("switch num: {}".format(line.count('switch')))
    print("case num:", end = '')
    for i in range(len(case_num)):
        print(" {}".format(case_num[i]), end = '')


def total_num():
    keyword_dict = {}
    total = 0
    for word in keyword_list:
        num = line.count(word)
        if num != 0:
            keyword_dict[word] = num
            total += num
    print("total num: {}".format(total))


total_num()
switch_count()