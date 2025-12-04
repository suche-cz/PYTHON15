"""
regularní výraz pro názvy souboru končící na .png
"""

import re

text = """
Data jsou v souboru data.txt, také je tam word.docx a kdyby jsi chtěl obrázky to:

my_image.png
xyz.png

věděl jsi že png soubory končí koncovkou .png 

dale je tam logo.png

věděli jste že soubory mohou obsahovat i speciální znaky?
např: _my-i.mage1000.png

např: _my-i.mag\e1000.png
"""

# data mining (těžba)


rx_png = re.compile(r'[_a-z0-9-\.]+\.png')
data = rx_png.findall(text)
print(data)
