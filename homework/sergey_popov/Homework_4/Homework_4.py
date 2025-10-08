#Домашка №4
my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [1, False, 2.41, 'text', None],
    'dict': {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5'
    },
    'set': {1, None, 'text', False, 2.42}
}

print(my_dict['tuple'][-1])

my_dict['list'].append(60)
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = 'value'
my_dict['dict'].pop('one')

my_dict['set'].add(6)
my_dict['set'].discard(1)

print(my_dict)
