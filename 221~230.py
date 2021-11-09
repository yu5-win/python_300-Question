# 221
# def print_reverse(a):
#     print(a[::-1])

# print_reverse("python")

# 222
# def print_score(arr):
#     sum = 0
#     for n in arr:
#         sum += n
#     print(sum/3)


# print_score([1, 2, 3])

# 223
# def print_even(arr):
#     for n in arr:
#         if n % 2 == 0:
#             print(n)


# print_even([1, 3, 2, 10, 12, 11, 15])

# 224
# def print_keys(dic):
#     arr = dic.keys()
#     for n in arr:
#         print(n)


# print_keys({"이름": "김말똥", "나이": 30, "성별": 0})

# 225
# my_dict = {"10/26": [100, 130, 100, 100],
#            "10/27": [10, 12, 10, 11]}


# def print_value_by_key(arr, date):
#     print(arr[date])


# print_value_by_key(my_dict, "10/26")

# 226
# def print_5xn(a):
#     print(a[:5])
#     print(a[5:])

# print_5xn("아이엠어보이유알어걸")

# 227
# def printmxn(str, a):
#     for n in range(a+1):
#         print(str[a*n:a*n+a])


# printmxn("아이엠어보이유알어걸", 3)

# 228
# def calc_monthly_salary(annual_salary):
#     print(annual_salary/12)


# calc_monthly_salary(12000000)


# 229
# def my_print(a, b):
#     print("왼쪽:", a)
#     print("오른쪽:", b)


# my_print(a=100, b=200)
# 왼쪽: 100
# 오른쪽: 200

# 230
def my_print(a, b):
    print("왼쪽:", a)
    print("오른쪽:", b)


my_print(b=100, a=200)
# 왼쪽: 200
# 오른쪽: 100
