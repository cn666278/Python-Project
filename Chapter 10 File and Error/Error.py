try:
    print(1/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")

# 使用error避免崩溃 (Using error avoid breaking)
print("Give me two numbers, and I will divide them for you.")
print("Enter 'q' for quitting")

while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("Second number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    # Using try-except-else construction
    else:
        print(answer)

# Error: File not found
filename = 'bilibili.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    message = "Sorry, the file <" + filename + "> does not exist."
    print(message)

# Word count

def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        message = "Sorry, the file <" + filename + "> does not exist."
        print(message)
    else:
        words = contents.split() #以空格为分隔
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'programming.txt'
count_words(filename)