import json

with open('python/37/pokemon.json', encoding='utf-8') as file:
    data = json.load(file)
    # print(data)
    
    """
    ukol: vyprintovat:
    1. pocet celkem pokemonu ['count'] # -> 1328
    2. pocet pokemonu z v datech ['results'] # -> 151
    3. vytisknout pokemona na 15. pozici (index 15) # -> {name: 'pidgey', url: 'https://pokeapi.co/api/v2/pokemon/16/'}
    4. pokemony od indexu 100 až 121 (včetně) # ->
    [
        {name: 'electrode', url: 'https://pokeapi.co/api/v2/pokemon/101/'},
        .
        .
        .
        {'name': 'mr-mime', 'url': 'https://pokeapi.co/api/v2/pokemon/122/'},
    ]
    5. projít pokemony a vytisknout ty které mají v názvu písmeno 'y'
    """

    results = data['results']
    print(data['count'])
    print(len(results))
    print(results[15])
    print(results[100:122])

    print('---------------------------------------')

    for item in results:
        name = item['name']
        if 'y' in name:
            print(name)


