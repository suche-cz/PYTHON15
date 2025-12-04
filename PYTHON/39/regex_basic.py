import re # regular expression

# regex_basic.py
# regex, regularní výrazy
# vzorce v textu


text = 'Ahoj Petře, toto je moje telefoní číslo 725 272 272, a jestli by jsi chtěl můžeš zavolat i Lence, její číslo je 654 726 262'

# cislo cislo cislo mezera cislo cislo cislo mezera cislo cislo cislo


rx_telefon = re.compile(r'\d{3}\s\d{3}\s\d{3}')

telefony = rx_telefon.findall(text)

print(telefony)
