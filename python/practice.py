import random
# creating range of list
lst = list(range(10))
print(lst)
# creating string of list from integer list
lst1 = list(map(str, lst))
print(lst1)
# multiply list by 2
lst2 = list(n*2 for n in lst)
print(lst2)
# choose odd  numbers from list
lst3 = list(n for n in lst if n % 2 != 0)
print(lst3)
# change odd numbers by -1
lst4 = list(n if n % 2 == 0 else -1 for n in lst)
print(lst4)
# change list to bool
lst5 = list(bool(n) for n in lst)
print(lst5)
# change even values to their negative values
lst6 = list(n * -1 if n % 2 == 0 else n for n in lst)
print(lst6)
lst7 = [[n for n in range(3, 6)] for _ in range(3)]
mean = sum(sum(row) for row in lst7)/9
print(mean)

