# File
with open('gay.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip()) #删除结尾空行
    print("------------------")

# 逐行读取
filename = 'gay.txt'
with open(filename) as file_object:
    # for line in file_object:
    #     print(line)
    #     print(line.rstrip()) # 删除空行

    lines = file_object.readlines() # list

    for Line in lines:
        print(Line.rstrip())

print("-----------------------------------")
pi_string = ''
for line in lines:
    pi_string += line.strip() # 删除左边空格

print(pi_string)
print(len(pi_string))