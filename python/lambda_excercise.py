import re
import datetime

r = lambda x: x + 15

print(r(10))

r = lambda x, y: x * y

print(r(12, 4))


def multiply_By(n):
    return lambda x: x * n


subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(subject_marks)
subject_marks.sort(key=lambda x: x[1])
print(subject_marks)

res = multiply_By(15)
print(res(2))
print(res(3))
print(res(4))
print(res(5))

models = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

print(models)
sorted_mod = sorted(models, key=lambda x: x['color'])
print(sorted_mod)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums)

even_nums = list(filter(lambda x: x % 2 == 0, nums))
odd_nums = list(filter(lambda x: x % 2 != 0, nums))

print(even_nums)
print(odd_nums)

square_nums = list(map(lambda x: x ** 2, nums))
cube_nums = list(map(lambda x: x ** 3, nums))

print(square_nums)
print(cube_nums)

string_check = lambda x: True if re.search('^P', x) else False
print(string_check("Python"))
print(string_check("Java"))

now = datetime.datetime.now()
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()

print(year(now))
print(month(now))
print(day(now))
print(t(now))


