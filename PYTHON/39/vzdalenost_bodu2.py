def get_distance(point1, point2):
    # x1 = point1[0]
    # y1 = point1[1]
    # x2 = point2[0]
    # y2 = point2[0]

    x1, y1 = point1
    x2, y2 = point2

    dx = x1 - x2
    dy = y1 - y2
    distance = (dx ** 2 + dy ** 2) ** 0.5

    return distance


def get_total_distance(*points):
    count = len(points)
    total_distance = 0

    for index in range(count - 1):
        point1 = points[index]
        point2 = points[index + 1]
        distance = get_distance(point1, point2)
        total_distance += distance
    
    return total_distance


# print('__name__ is', __name__)

if __name__ == '__main__':
    # tato část kódu se spustí pouze pokud je tento soubor hlavním (není importovaný)
    distance1 = get_total_distance(
        (1, 3),
        (5, 5),
        (9, 5),
    )

    distance2 = get_total_distance(
        (10, 3),
        (5, 50),
        (90, 5),
        (9, -15),
        (190, 65),
    )

    print(distance1)
    print(distance2)

