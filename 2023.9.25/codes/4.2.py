import time as tm
import random as rd
import sys

sys.setrecursionlimit(5000)


def mp_sort(v: list):
    for r in range(len(v) - 1, 0, -1):
        for i in range(0, r):
            if v[i] > v[i + 1]:
                v[i], v[i + 1] = v[i + 1], v[i]


def q_sort(v: list, l, r):
    if len(v) <= 1 or r >= len(v) or r <= l: return
    head = l
    tail = r
    pivot = v[l]
    l_empty = True
    while l != r:
        if l_empty:
            if v[r] < pivot:
                v[l], v[r] = v[r], v[l]
                l += 1
                l_empty = False
            else:
                r -= 1
        else:
            if v[l] > pivot:
                v[l], v[r] = v[r], v[l]
                r -= 1
                l_empty = True
            else:
                l += 1
    v[l] = pivot
    q_sort(v, head, l - 1)
    q_sort(v, l + 1, tail)


def test(n: int):
    lis1 = []
    lis2 = []
    for i in range(0, n):
        tmp = rd.randint(-1e10, 1e10)
        lis1.append(tmp)
        lis2.append(tmp)
    print("测试长度为%d" % n)
    beg1 = tm.time()
    mp_sort(lis1)
    end1 = tm.time()
    print("冒泡排序用时", end1 - beg1)
    beg2 = tm.time()
    q_sort(lis2, 0, n - 1)
    end2 = tm.time()
    print("快速排序用时", end2 - beg2)
    print()


for i in range(4, 16):
    test(pow(2, i))
