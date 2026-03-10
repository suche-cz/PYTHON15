"""
desítková soustava
znaky 0-9

---------------------------------------------------------
https://cs.wikipedia.org/wiki/Dvojkov%C3%A1_soustava

bit = základní informační jednotka
znaky 0-1

ano, ne
0, 1
zapnuto, vypnuto

využívá se binární (dvojková soustava)

data -> kombinace 0,1


hodnota * 2 ** pozice

1 = 1 (1 * 2 ** 0)
10 = 2 (0 * 2 ** 0 + 1 * 2 ** 1)
11 = 3 (1 * 2 ** 0 + 1 * 2 ** 1)
100 = 4 (0 * 2 ** 0 + 0 * 2 **1 + 1 * 2 **2)
101 = 5
110 = 6
111 = 7

---------------------------------------------------------

kombinace 8 bitů nám dává bajt
- 256 kombinací - 0 - 255
- zápis v hexadecimálním tvaru (16. soustava)
- znaky 0-F
- #00 11 DD

např
0100 0001 = 65 = A v ASCII tabulce

"""

number = 65

bit_number = bin(number)
hex_number = hex(number)

print(bit_number)
print(hex_number)

symbol = chr(number)
print(symbol)
print(ord('A'))

