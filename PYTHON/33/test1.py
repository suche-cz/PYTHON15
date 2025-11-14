import my_test
import pathlib

age = 30

text = my_test.MY_NAME + " " + str(age)

text2 = f"{my_test.MY_NAME} {age} {10 + 30}"  # f-string

# TOTO je řádkový komentář
"""
Toto je blokový komentář
"""

print(text)
print(text2)
