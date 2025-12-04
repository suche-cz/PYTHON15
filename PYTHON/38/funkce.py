# funkce.py


def moje_funkce(a, b):
    c = a + b
    return c


vysl1 = moje_funkce(10, 20)
vysl2 = moje_funkce(100, 200)
vysl3 = moje_funkce(1, 2)

print(vysl1)
print(vysl2)
print(vysl3)


def obvod_trojuhelnika(a, b, c):
    o = a + b + c
    return o


vysl1 = obvod_trojuhelnika(20, 20, 20)
vysl2 = obvod_trojuhelnika(15, 20, 12)

print(vysl1)
print(vysl2)


# --------------------------------------------------


def is_valid_triangle1(a, b, c) -> bool:
    count = 0

    if (a + b) > c:
        count += 1
    if (a + c) > b:
        count += 1
    if (b + c) > a:
        count += 1
    
    return count == 3


def is_valid_triangle2(a, b, c):
    ab = a + b > c
    ac = a + c > b
    bc = b + c > a
    return ab and ac and bc


def is_valid_triangle3(a, b, c):
    data = [a,b,c]
    data.sort()
    return data[0] + data[1] > data[2]


print(is_valid_triangle2(100, 1, 1))

import math

# math.pi


def obvod_kruhu():
    # jaké budou vstupní parametry
    # jaký bude výpočet
    # navratová hodnota
    # + test 
    pass



def obsah_kruhu():
    pass



def get_quadrangle_type(a, b, c, d):
    """
    pokud jsou všechny strany stejné tak je to čtverec
    pokud jsou protilehlé strany stejné tak je to odbdelník
    jinak to bude nepravidlný čtyřúhelník
    """

get_quadrangle_type(1, 2, 3, 4)


def my_func(a, b, c=10, d=None, data=None):
    data = data or []
    


def get_icecream(icecream_type='Vanille'):
    pass


get_icecream()
get_icecream(icecream_type='Choko')


my_func(10, 20)
my_func(10, 20, 30)
my_func(10, 20, data=30, c=10)
