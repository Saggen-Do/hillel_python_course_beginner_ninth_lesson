def decorator(name):
    def print_great():
        print("hello," + name)

    return print_great


res = decorator("Ivan")
res()