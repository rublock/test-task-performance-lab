import sys


def make_arr(n):
    arr = []
    for i in range(1, n + 1):
        arr.append(i)
    return arr


def iter_arr(arr, step):
    result = "1"
    start = step - 1
    while True:
        if arr[start] != 1:
            result += str(arr[start])
            if len(arr) // start == 1:
                arr += arr
            start += step - 1
        else:
            return result


if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    arr = make_arr(n)
    print(iter_arr(arr, m))
