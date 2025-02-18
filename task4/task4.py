import sys


def main(nums):
    arr = []
    num = 0
    nums.sort()
    for i in nums:
        for j in nums:
            num += abs(j - i)
        arr.append(num)
        num = 0

    return min(arr)


if __name__ == "__main__":
    numbers = open(sys.argv[1], "rt", encoding="utf-8")
    nums_list = [int(lines) for lines in numbers.readlines()]
    print(main(nums_list))
