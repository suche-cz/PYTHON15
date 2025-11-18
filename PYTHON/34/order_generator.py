start_number = 0
actual_number = start_number
max_number = 10
increment = 1

"""
upgrade:
1) jednotlivé části dát do funkcí
2) vytvořit mapovací dict pro command a funkci

Dalš úkoly:
najít nejstarší, nejmladší soubor
najít největší, nejmenší soubor
"""


while True:
    command = input('Zdejte příkaz: ')

    if command == 'next':
        if actual_number < max_number:
            actual_number += increment
        else:
            actual_number = start_number + increment
        print('Next number:', actual_number)

    elif command == 'reset':
        print('Number generator reset')
        actual_number = start_number

    elif command == 'exit':
        print('Exiting program')
        break

    elif command == 'help':
        print(
            'Use commands:\n'
            'next - to get next number\n'
            'reset - to reset counter\n'
            'exit - to exit program\n'
        )

    else:
        print('Uknown command')