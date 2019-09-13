if __name__ == '__main__':
    
    birthdays = {
        'Michelangelo': 'March 6, 1475',
        'Leonardo da Vinci': 'April 15, 1452',
        'Marie Curie': 'November 7, 1867'}


    print('Welcome to the Birthday Dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)

    print('Who\'s birthday do you want to look up?')
    name = input()
    if name in birthdays:
        print('{}\'s birthday was born on {}.'.format(name, birthdays[name]))
    else:
        print('Please use a name from the provided list.')

    # Can i put "print(birthdays.get(name, 'Please use a name from the provided list.'))

   ###### ATTEMPT 2 
    
    if __name__ == '__main__':
    
    birthdays = {
        'Michelangelo': 'March 6, 1475',
        'Leonardo da Vinci': 'April 15, 1452',
        'Marie Curie': 'November 7, 1867'}

    print('Welcome to the Birthday Dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)      
        
    print('Would you like to access the birthday dictionary?')
    'response' = input()
    While 'response' != 'no'): 
        print('Who\'s birthday do you want to look up?')
        name = input()
        for name in birthdays:
            print(birthdays.get(name, 'Please use a name from the provided list.'))
    else:      
        print('Thank you for using the birthday dictionary!")
        
    

    

    # Can i put "print(birthdays.get(name, 'Please use a name from the provided list.'))
    # print('{}\'s birthday was born on {}.'.format(name, birthdays[name]))
        # else:
            #print('Please use a name from the provided list.')
