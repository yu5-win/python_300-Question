# 291
# import csv
# f = open("./매수종목1.txt", 'wt')
# f.write("005930\n005380\n035420")
# f.close()

# 292
# f = open("./매수종목2.txt", 'wt', encoding='utf-8')
# f.write("005930 삼성전자\n")
# f.write("005380 현대차\n")
# f.write("035420 NAVER")
# f.close()

# 293

# f = open('./매수종목.csv', mode='wt', encoding='cp949', newline='')
# writer = csv.writer(f)
# writer.writerow(["종목명", "종목코드", "PER"])
# writer.writerow(["삼성전자", "005930", 15.79])
# writer.writerow(["NAVER", "035420", 55.82])
# f.close()

# 294
# f = open("./매수종목1.txt", encoding="utf-8")
# lines = f.readlines()

# codes = []
# for line in lines:
#     code = line.strip()
#     codes.append(code)

# print(codes)
# f.close()

# 295
# f = open("./매수종목2.txt", encoding="utf-8")
# lines = f.readlines()

# data = {}
# for line in lines:
#     line = line.strip()
#     k, v = line.split()
#     data[k] = v

# print(data)
# f.close()

# 296
# per = ["10.31", "", "8.00"]

# for i in per:
#     try:
#         print(float(i))
#     except ValueError:
#         print(0)

# 297
# per = ["10.31", "", "8.00"]
# per_f = []
# for i in per:
#     try:
#         v = float(i)
#     except:
#         v = 0.0
#     per_f.append(v)
# print(per_f, type(per_f[1]))

# 298
# try:
#     y = 5 / 0
# except ZeroDivisionError:
#     print("0으로 나누면 안돼요")

# 299
# data = [1, 2, 3]

# for i in range(5):
#     try:
#         print(data[i])
#     except IndexError as e:
#         print(e)

# 300
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("예외가 발생하지 않았을 때 수행할 코드")
    finally:
        print("예외 발생 여부와 상관없이 항상 수행할 코드")
