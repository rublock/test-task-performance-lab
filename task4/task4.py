import sys
from copy import deepcopy


def first_iter(nums_list):
    temp_l = deepcopy(nums_list)
    target = temp_l[0]
    count = 0
    for i in range(len(temp_l)):
        if temp_l[i] != target:
            if target < temp_l[i]:
                while temp_l[i] != target:
                    temp_l[i] -= 1
                    count += 1
            elif target > temp_l[i]:
                while temp_l[i] != target:
                    temp_l[i] += 1
                    count += 1
    return count


def main(l, min_count):
    count = 0
    temp_l = deepcopy(l)
    for i in temp_l[1:]:
        for j in range(len(temp_l)):
            if temp_l[j] != i:
                if temp_l[j] > i:
                    while temp_l[j] != i:
                        temp_l[j] -= 1
                        count += 1
                elif temp_l[j] < i:
                    while temp_l[j] != i:
                        temp_l[j] += 1
                        count += 1
        if count < min_count:
            min_count = count
        temp_l = deepcopy(l)
        count = 0
    return min_count


if __name__ == "__main__":
    numbers = open(sys.argv[1], "rt", encoding="utf-8")
    nums_list = [int(lines) for lines in numbers.readlines()]
    min_count = first_iter(nums_list)
    print(main(nums_list, min_count))
