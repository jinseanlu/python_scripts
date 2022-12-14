names = ["JinSean", "Mark", "Xiaoran", "Raymond", "Johnson", "Ryan", "Daniel"]

def add_your_name():
    user_input = input("input your name ")
    names.append(user_input)
    print(names)
    
while True:
    add_your_name()
