actual_number = 0
max_number = 999


def command_exit():
    print('Ukončuji program')
    exit()

def command_reset():
    # global se znažíme vyhnout
    global actual_number
    print('Resetuji pořadník')

    actual_number = 0

def command_next():
    # global se znažíme vyhnout
    global actual_number
    global max_number

    if actual_number < max_number:
        actual_number += 1
    else:
        actual_number = 1

    print('Dostaváte číslo:', actual_number)


commands = {
    'exit': command_exit,
    'reset': command_reset,
    'next': command_next,
}


while True:
    command = input('Zadejte příkaz: ')

    func = commands.get(command)

    if func:
        func()
    else:
        print('Zadal/a jste neznámý příkaz')
    
