# 191
# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for n in data:
#     for m in n:
#         print(m * 1.00014)

# 192
# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for n in data:
#     for m in n:
#         print(m * 1.00014)
#     print("----")

# 193
# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []
# for n in data:
#     for m in n:
#         result.append(m * 1.00014)

# print(result)

# 194
# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []

# for n in data:
#     sub = []
#     for m in n:
#         sub.append(m * 1.00014)
#     result.append(sub)

# print(result)

# 195
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for n in ohlc[1:]:
#     print(n[3])

# 196
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for n in ohlc[1:]:
#     if n[3] > 150:
#         print(n[3])

# 197
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for n in ohlc[1:]:
#     if n[3] >= n[0]:
#         print(n[3])

# 198
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# volatility = []

# for n in ohlc[1:]:
#     volatility.append(n[1]-n[2])
# print(volatility)

# 199
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for n in ohlc[1:]:
#     if n[3] > n[0]:
#         print(n[1]-n[2])

# 200
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# sum = 0
# for n in ohlc[1:]:
#     sum += n[3]-n[0]
# print(sum)
