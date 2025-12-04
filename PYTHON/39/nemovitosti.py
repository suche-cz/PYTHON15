import re
from pathlib import Path


html = Path('python/39/nemovitosti.html').read_text(encoding='utf-8')

# print(html)


rx_item = re.compile(r'<div class="col-6 col-md-5 text-right slider_cena pl-0">([\d\s]+) (EUR|Kč) <')

data = rx_item.findall(html)

for cena, mena in data:
    cena = int(cena.replace(' ', ''))
    print(cena, mena)
