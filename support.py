# utils.py

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y


def concatenate_strings(str1, str2):
    return str1 + " " + str2


def add_to_list(lst, item):
    lst.append(item)


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()
