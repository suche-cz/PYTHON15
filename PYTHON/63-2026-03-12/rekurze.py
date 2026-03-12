data = {
    'name': 'Czech',
    'parts': [
        {
            'name': 'Olomoucký kraj',
            'parts': [
                {
                    'name': 'Okres Olomouc',
                    'parts': [
                        {'name': 'Olomouc', 'parts': [
                            {'name': 'Malé město', 'parts': []}
                        ]}
                    ]
                }
            ]
        },
    ]
}


def print_parts(item):
    if 'parts' in item:
        for item in item['parts']:
            print(item['name'])
            print_parts(item)


print_parts(data)
