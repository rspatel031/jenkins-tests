import requests

from support import add, add_to_list, concatenate_strings, divide, multiply, read_file, subtract


def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtraction():
    assert subtract(5, 2) == 3
    assert subtract(10, 5) == 5
    assert subtract(0, 0) == 0


def test_multiplication():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 6) == -12


def test_division():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(7, 0) == "Error: Division by zero"


def test_concatenate_strings():
    assert concatenate_strings("Hello", "World") == "Hello World"
    assert concatenate_strings("", "Test") == "Test"
    assert concatenate_strings("Python", "") == "Python"


def test_add_to_list():
    my_list = [1, 2, 3]
    add_to_list(my_list, 4)
    assert my_list == [1, 2, 3, 4]


def test_dict_key_exists():
    my_dict = {"name": "Alice", "age": 30}
    assert "name" in my_dict
    assert "email" not in my_dict


def test_read_file():
    content = read_file("test_file.txt")
    assert "Hello, World!" in content
    assert "Python" not in content


def test_api_response_status_code():
    response = requests.get("https://www.google.com")
    assert response.status_code == 200
