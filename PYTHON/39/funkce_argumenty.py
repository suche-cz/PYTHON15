# funkce_argumenty.py



def my_func(*args, **kwargs):
    print(args)
    print(kwargs)


my_func(10, 20, 30, 40, x=10, y=20)


def my_func2(params, key_values):
    print(params)
    print(key_values)


my_func2((10, 20, 30, 40), {'x': 10, 'y': 20})

