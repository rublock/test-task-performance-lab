import sys

n = int(sys.argv[1])
m = int(sys.argv[2])


def make_arr(n):
    """Создание массива"""
    arr = []

    for i in range(1, n + 1):
        arr.append(i)

    return arr


def iter_arr(arr, step):
    """Перебор массива"""
    result = "1"
    start = step - 1
    while True:
        if arr[start] != 1:
            result += str(arr[start])
            arr += arr
            start += step - 1
        else:
            return result


if __name__ == "__main__":
    arr = make_arr(n)
    print(iter_arr(arr, m))
