import copy
from typing import List


def main():
    org_sort = [17, 11, 12, 5, 14, 9, 6, 16, 4,
                10, 1, 19, 13, 15, 0, 2, 3, 18, 7, 8]

    result = selection_sort(org_sort)
    assert sorted(org_sort) == result

    print("result: {}".format(result))


#######################################################
# 選択ソート アルゴリズム
#
# org_sort = [1, 3, 0, 2, 4, 5] の場合
# org_sortの最小値&org_sortでのindexを調べ、最小値をorg_sortから取り除き、new_sortの末尾に追加していく。
#
# org_sort = [1, 3, 0, 2, 4, 5]
# new_sort = []
#
#   -----------------------
#   |                     |
# new_sort[] org_sort[1, 3, 0, 2, 4, 5]
# new_sort[0] org_sort[1, 3, 2, 4, 5]
#
#   --------------------
#   |                  |
# new_sort[0] org_sort[1, 3, 2, 4, 5]
# new_sort[0, 1] org_sort[3, 2, 4, 5]
#
#   -------------------------
#   |                        |
# new_sort[0, 1] org_sort[3, 2, 4, 5]
# new_sort[0, 1, 2] org_sort[3, 4, 5]
#
# をn(len(org_sort))回繰り返す
#
#######################################################


def selection_sort(org_list: List[int]) -> List[int]:
    list = copy.copy(org_list)
    new_sort = []
    for _ in range(len(list)):
        m = min(list)
        index = list.index(m)
        value = list.pop(index)
        new_sort.append(value)

        print("m:{}, index:{}, new_sort:{}".format(m, index, new_sort))
        print("---------------------------------------------")

    return new_sort


if __name__ == "__main__":
    main()
