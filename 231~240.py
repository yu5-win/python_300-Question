# 231
# def n_plus_1 (n) :
#     result = n + 1

# n_plus_1(3)
# print (result)

# 232
# def make_url(url):
#     print("www."+url+".com")


# make_url("naver")

# 233
# def make_list(a):
#     print(list(a))


# make_list("abcd")

# 234
# def pickup_even(arr):
#     a = []
#     for n in arr:
#         if n % 2 == 0:
#             a.append(n)
#     print(a)


# pickup_even([3, 4, 5, 6, 7, 8])

# 235
# def convert_int(a):
#     print(a.replace(',', ''))


# convert_int("1,234,567")

# 236
# def 함수(num):
#     return num+4


# a = 함수(10)  # 14
# b = 함수(a)  # 18
# c = 함수(b)  # 22
# print(c)
# 22

# 237
# def 함수(num):
#     return num + 4


# c = 함수(함수(함수(10)))
# print(c)
# 22

# 238
# def 함수1(num):
#     return num + 4


# def 함수2(num):
#     return num * 10


# a = 함수1(10)
# c = 함수2(a)
# print(c)
# 140

# 239
# def 함수1(num):
#     return num + 4


# def 함수2(num):
#     num = num + 2
#     return 함수1(num)


# c = 함수2(10)
# print(c)
# 16

# 240
# def 함수0(num):
#     return num * 2


# def 함수1(num):
#     return 함수0(num + 2)


# def 함수2(num):
#     num = num + 10
#     return 함수1(num)


# c = 함수2(2)
# print(c)
# 28
