"""
!5 = 5 * !4
!4 = 4 * !3
!3 = 3 * !2
!2 = 2 * !1
!1 = 1
"""


def faktorial(cislo):
    if cislo == 1:
        return 1
    
    return cislo * faktorial(cislo - 1)


def faktorial_cyklus(cislo):
    vysledek = 1

    for i in range(2, cislo + 1):
        vysledek *= i
    
    return vysledek


print(faktorial(10))
print(faktorial_cyklus(10))


def suma(cislo):
    """ suma všech čísel 1..cislo pomocí rekurze """
    pass


print(suma(10)) # 55
