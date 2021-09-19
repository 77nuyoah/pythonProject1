keyword_list = ['auto','break','case','char','const','continue','default','do',
                'double','else','enum','extern','float','for','goto','if',
                'int','long','register','return','short','signed','sizeof',
                'static','struct','switch','typedef','union','unsigned',
                'void','volatile','while']


filepath = input("代码文件的路径:")


code = []
with open(filepath, 'r' ) as f:
    for line in f:
        code.append(line)
f.close()
text = "".join(code)


keyword_dict = {}
total = 0
for word in keyword_list:
    num = text.count(word)
    if num != 0:
        keyword_dict[word] = num
        total += num
print("total num: {}".format(total))