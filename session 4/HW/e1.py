inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory)
print("*" * 136)
inventory['backpack'].remove('dagger')
print(inventory['backpack'], sep=' ')
print("*" * 136)
inventory['gold'] = 500, 50
print(inventory['gold'])
