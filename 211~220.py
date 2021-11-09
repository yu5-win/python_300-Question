# 211
# def 함수(문자열):
#     print(문자열)

# 함수("안녕")
# 함수("Hi")
# 안녕 Hi

# 212
# def 함수(a, b) :
#     print(a + b)

# 함수(3, 4)
# 함수(7, 8)
# 7 15

# 213
# def 함수(문자열):
# print(문자열)
# 함수안에 매개변수가 없어서

# 214
# def 함수(a, b) :
#     print(a + b)

# 함수("안녕", 3)
# 문자열과 정수는 더할수없다

# 215~216
# string = input()

# def print_with_smile(str):
#     print(str + ":D")

# print_with_smile(string)

# 217
# def print_upper_price(price):
#     upper = 1.3
#     print(price*upper)

# 218
# def print_sum(a, b):
#     print(a+b)

# 219
# def print_arithmetic_operation(a, b):
#     print(a, '+', b, '=', a+b)
#     print(a, '-', b, '=', a-b)
#     print(a, '*', b, '=', a*b)
#     print(a, '/', b, '=', a/b)

# print_arithmetic_operation(3, 4)

# 220
def print_max(a, b, c):
    max = 0
    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    elif c > a and c > b:
        max = c


print(max(9, 8, 15))
