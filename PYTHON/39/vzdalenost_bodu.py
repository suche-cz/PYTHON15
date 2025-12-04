data = [
    (1, 3), # 0
    (5, 5), # 1
    (9, 5), # 2
]


count = len(data) # 3
distance = 0

for index in range(count - 1):
    # print(index, index + 1)

    x1, y1 = data[index]
    x2, y2 = data[index + 1]

    dx = x1 - x2
    dy = y1 - y2

    # c = (a**2 + b**2) ** 0.5
    c = (dx ** 2 + dy ** 2) ** 0.5
    distance += c

print('celková vzdálenost je:', distance)
    

