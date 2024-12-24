import sys

n = 5


def make_arr(n):
    """Создание массива"""
    arr = []

    for i in range(1, n + 1):
        arr.append(i)

    return arr


if __name__ == '__main__':
    my_array = make_arr(int(sys.argv[1]))
    print(my_array)
