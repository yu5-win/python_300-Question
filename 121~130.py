# 121
# a = input()
# if a.islower():
#     print(a.upper())
# else:
#     print(a.lower())

# 122
# score = int(input("score: "))
# grade = ''
# if 80 < score <= 100:
#     grade = 'A'
# elif 60 < score <= 80:
#     grade = 'B'
# elif 40 < score <= 60:
#     grade = 'C'
# elif 20 < score <= 40:
#     grade = 'D'
# elif 0 <= score <= 20:
#     grade = 'E'
# print("grade is ", grade)

# 123
# dalla = input("입력: ")
# money = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
# num, currency = dalla.split()

# print(float(num)*money[currency], '원')

# 124
# num = []
# num1 = int(input("input numbere1: "))
# num.append(num1)
# num2 = int(input("input numbere2: "))
# num.append(num2)
# num3 = int(input("input numbere3: "))
# num.append(num3)

# print(max(num))

# 125
# phone = {"011": "SKT", "016": "KT", "019": "LGU", "010": "알수없음"}
# phone_num = input("휴대전화 번호 입력: ")
# num = phone_num[:3]

# print(phone.get(num))

# 126
# num = input("우편번호: ")
# n = int(num[2])
# address = ''
# if 0 <= n <= 3:
#     address = "강북구"
# elif 3 <= n <= 5:
#     address = "도봉구"
# else:
#     address = "노원구"
# print(address)

# 127
# num = input("주민등록번호: ")
# num_sex = int(num[7])
# if num_sex == 1 or num_sex == 3:
#     print("남자")
# else:
#     print("여자")

# 128
# num = input("주민등록번호: ")
# code = int(num.split('-')[1][1:3])
# if 0 <= code <= 8:
#     print("서울 입니다.")
# else:
#     print("서울이 아닙니다.")

# 129
# social = input("주민등록번호: ")
# if 11 - (int(social[0])*2+int(social[1])*3+int(social[2])*4+int(social[3])*5+int(social[4])*6+int(social[5])*7 +
#          int(social[7])*8+int(social[8])*9+int(social[9])*2+int(social[10])*3+int(social[11])*4+int(social[12])*5) % 11 == social[12]:
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")


# 130
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# 변동폭 = int(btc["max_price"])-int(btc["min_price"])
# if int(btc["opening_price"])+변동폭 > int(btc["max_price"]):
#     print("상승장")
# else:
#     print("하락장")
