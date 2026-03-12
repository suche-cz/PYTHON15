import timeit


def faktorial(cislo):
    if cislo == 1:
        return 1
    
    return cislo * faktorial(cislo - 1)


def faktorial_cyklus(cislo):
    vysledek = 1

    for i in range(2, cislo + 1):
        vysledek *= i
    
    return vysledek


print(timeit.timeit(lambda: faktorial(90), number=100_000))
print(timeit.timeit(lambda: faktorial_cyklus(90), number=100_000))
