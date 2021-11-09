# 261
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

# 262
# 삼성 = Stock("삼성전자", "005930")


# 263
# a = Stock(None, None)
# a.set_name("삼서전자")

# 264
# a = Stock(None, None)
# a.set_code("005930")

# 265
# 삼성 = Stock("삼성전자", "005930")

# 266

# 267
# 삼성 = Stock("삼성전자", 005930, 15.79, 1.33, 2.83)

# 268

# 269
# 삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# 삼성.set_per(12.75)
# print(삼성.per)

# 270
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

stock = [삼성, 현대차, LG전자]
for n in stock:
    print(n.per, n.code)
