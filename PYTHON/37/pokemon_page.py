import json

with open('python/37/pokemon.json', encoding='utf-8') as file:
    data = json.load(file)
    results = data['results']

with open('python/37/poke-list-item.html', encoding='utf-8') as file:
    list_item_template = file.read()

list_items = []

for item in results[:3]:
    list_item = list_item_template.format(
        name=item['name'],
        number='000',
        type='type',
        image='image',
    )

    list_items.append(list_item)


list_items_html = '\n\n'.join(list_items)

print(list_items_html)

