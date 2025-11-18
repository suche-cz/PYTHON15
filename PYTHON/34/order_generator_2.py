actual_number = 0
max_number = 999


while True:
    command = input('Zadejte příkaz: ')

    if command == 'exit':
        print('Ukončuji program')
        exit() # break by ukončil cyklus 
        
    elif command == 'reset':
        print('Resetuji pořadník')
        actual_number = 0

    elif command == 'next':
        if actual_number < max_number:
            actual_number += 1
        else:
            actual_number = 1

        print('Dostaváte číslo:', actual_number)

    else:
        print('Zadal/a jsi:', command)
    
