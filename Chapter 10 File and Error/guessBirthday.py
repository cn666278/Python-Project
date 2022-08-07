filename = 'text1.txt'
with open(filename) as file_object:

    lines = file_object.readlines() # list

pi_string = ''
for line in lines:
    pi_string += line.strip()  # 删除左边空格
#
# birthday = input("Enter your birthday, in the form of mm/dd/yy:")
#
# if birthday in pi_string:
#     print("Your birthday is in the txt file!")
# else:
#     print("Your birthday is not in the txt file!")

count = 0
num = "gay"
if num in pi_string:
    count += 1
print("The number 0 occurs in the file is " + str(count) + " times.")

# 写入空文件
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    # 'w': write mode
    # 'r': read mode
    # 'a': add mode （给文件添加内容而不覆盖原有内容）
    # 'r+': read & write mode

    for i in range(0,20):
        file_object.write("I love python programming!\n")

with open(filename, 'a') as file_object:
    for i in range(0,2):
        file_object.write("I love java programming too!\n")

# <for testing only>
# with open(filename, 'w') as file_object:
#     for i in range(0,2):
#         file_object.write("I love java programming too!\n")

