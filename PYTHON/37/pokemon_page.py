import json

with open('python/37/pokemon.json', encoding='utf-8') as file:
    data = json.load(file)
    results = data['results']

with open('python/37/poke-list-item.html', encoding='utf-8') as file:
    list_item_template = file.read()

list_items = []

for item in results:
    list_item = list_item_template.format(
        name=item['name'],
        number='000',
        type='type',
        image='image',
    )

    list_items.append(list_item)


list_items_html = '\n\n'.join(list_items)

# print(list_items_html)


with open('python/37/poke-list.html', encoding='utf-8') as file:
    list_template = file.read()


full_list_html = list_template.replace('{pokemon_list}', list_items_html)

# print(full_list_html)


result_list_path = 'python/37/pokemon-list.html'

with open(result_list_path, mode='w', encoding='utf-8') as file:
    file.write(full_list_html)
    print('page was generated')

