def sum_Rec(val):
    if val > 0:
        sumR = val + int(sum_Rec(val - 1))
    else:
        return 0

    return sumR

def sum_recursion(ls):
    if len(ls) == 1:
        return ls[0]
    else:
        return ls[0] + sum_recursion(ls[1:])


print(sum_Rec(5))
print(sum_recursion([2, 4, 5, 6, 7]))