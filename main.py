if __name__ == '__main__':
    
    birthdays = {
        'Michelangelo': 'March 6, 1475',
        'Leonardo da Vinci': 'April 15, 1452',
        'Marie Curie': 'November 7, 1867',
        'Jane Goodall': 'April 3, 1934',
        'Charles Dickens': 'February 7, 1812',
        'Jane Austen':'December 16, 1775',
        'John Powell':'September 18, 1963',
        'Josh Gad':'February 23, 1981'}


    print('Welcome to the Birthday Dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)

    print('\n\nWho\'s birthday do you want to look up?')
    name = input()
    if name in birthdays:
        print('{} was born on {}.'.format(name, birthdays[name]))
    else:
        print('Please use a name from the provided list.')


