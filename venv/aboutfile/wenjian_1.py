import json
count=0
filename='/Users/fangmeiwen/json.txt'
with open(filename,'r') as f:
    # read到末尾会返回一个空字符串，末尾会显示空行
    # contents= f.read()
    # # 删掉末尾的空行
    # print(contents.rstrip())

    # 逐行读取文件
    # for line in f:
    #     print(line)
    #
    lines=f.readlines()

for line in lines:
    print(line.rstrip())

print(type(lines))
print(lines[2])





