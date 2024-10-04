import math
from statistics import median, mean, mode, variance


def avgSum_recursion(ls):
    if len(ls) == 1:
        return ls[0]
    else:
        return ls[0] + avgSum_recursion(ls[1:])


#this methed finds the average or mean value
def meann(ls):
    summ = avgSum_recursion(ls)

    return summ / len(ls)


def sort(ls, lenghtArray1=0, lenghtArray2=0):
    if len(ls) == lenghtArray1:
        return ls
    else:
        if ls[lenghtArray1] < ls[lenghtArray2]:
            tmp = ls[lenghtArray1]
            ls[lenghtArray1] = ls[lenghtArray2]
            ls[lenghtArray2] = tmp
        lenghtArray2 += 1
        if len(ls) == lenghtArray2:
            lenghtArray1 += 1
            lenghtArray2 = 0
        return sort(ls, lenghtArray1, lenghtArray2)


def med(ls):
    lsSorted = sort(ls)
    if len(lsSorted) % 2 == 0:
        lg = int(len(lsSorted) / 2)
        me = lsSorted[lg - 1] + lsSorted[lg]
        return me / 2
    else:
        lg = int(len(lsSorted) / 2)
        me = lsSorted[lg]
        return me


def mod(ls, it1=0, it2=0, cntP=0, cntN=0, mo=0):
    if len(ls) == it1:
        return mo
    else:
        if ls[it1] == ls[it2]:
            cntN += 1

        it2 += 1
        if len(ls) == it2:
            if cntP <= cntN:
                mo = ls[it1]
                cntP = cntN
                cntN = 0
            it2 = 0
            it1 += 1

        return mod(ls, it1, it2, cntP, cntN, mo)


def vari_sum(ls, it1=0):
    if (len(ls) - 1) == it1:
        return (ls[it1] - meann([2, 4, 5, 6, 7, 6])) ** 2
    else:
        it1 += 1
        return ((ls[it1 - 1] - meann([2, 4, 5, 6, 7, 6])) ** 2) + vari_sum(ls, it1)


def vari(ls):
    return vari_sum(ls) / len(ls)


def standard_D(ls):
    return math.sqrt(vari(ls))

# print(med([9, 4, 3, 6, 7]))
# print(median([9, 4, 3, 6, 7]))
# print(meann([2, 4, 5, 6, 7, 6]))
# print(mean([2, 4, 5, 6, 7, 6]))
# print(mod([2, 4, 5, 6, 7, 6]))
# print(mode([2, 4, 5, 6, 7, 6]))
# print(vari([2, 4, 5, 6, 7, 6]))
# print(standard_D([2, 4, 5, 6, 7, 6]))
