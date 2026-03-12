def add_cool_text(func):

    def inner(*args, **kwargs):
        print('#####################')
        result = func(*args, **kwargs)
        print('*********************')
        return result * 100
    
    return inner
    
    
@add_cool_text
def funcA(a, b, c=10):
    return a + b + c


@add_cool_text
def funcB(a, b):
    return a * b


print(funcA(10, 20, 30))
print(funcB(10, 20))



def printer1(value):
    print('#######', value)

def printer2(value):
    print('*******', value)


def calculate(a, b, print_func):
    result = a * b
    print_func(result)


print('------------------')

calculate(10, 20, printer1)
calculate(100, 200, printer1)
