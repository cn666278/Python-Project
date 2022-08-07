# JSON -- JavaScript Object Notation

# Using json.dump / json.load

import json
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_object:
    # dump:储存列表到内存中
    json.dump(numbers, f_object)

with open(filename) as f_object:
    # load:读取列表到内存中
    numbers = json.load(f_object)
print(numbers)

# ------------------------------------------------------------------------
username = input("What is your name?\n")

filename = 'username.json'
with open(filename, 'w') as f_object:
    json.dump(username, f_object)
    print("We'll remember you when you come back, " + username + "!")

with open(filename) as f_object:
    username = json.load(f_object)
    print("Welcome back, " + username + "!")

# --------------------------------------------------------------------------
# Using try-except-else

filename = 'username.json'

# 如果文件 username.json 存在则运行 try 将内容值储存在username之中
try:
    with open(filename) as f_object:
        username = json.load(f_object)
# 如果文件 username.json 不存在则运行 except
except FileNotFoundError:
    username = input("What is your name?\n")
    with open(filename, 'w') as f_object:
        json.dump(username, f_object)
        print("We'll remember you when you come back, " + username + "!")
# 如果文件 username.json 存在则运行 else
else:
    print("Welcome back, " + username + "!")

# ---------------------------------------------------------------------------
# 重构 Reconstruction

def greet_user():
    filename = 'username.json'

    try:
        with open(filename) as f_object:
            username = json.load(f_object)

    except FileNotFoundError:
        username = input("What is your name?\n")
        with open(filename, 'w') as f_object:
            json.dump(username, f_object)
            print("We'll remember you when you come back, " + username + "!")

    else:
        print("Welcome back, " + username + "!")

greet_user()

# ---------------------------------------------------------------------------
# 重构 greet_user into 3 different functions

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_object:
            username = json.load(f_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name?\n")
    filename = 'username.json'
    with open(filename, 'w') as f_object:
        json.dump(username, f_object)
    return username

def greet_user():
    """问候用户，并指出名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()


