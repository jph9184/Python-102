set_countries = {"col", 'mex', 'bol'}

size = len(set_countries)

print(size)

print('col' in set_countries)
print('pe' in set_countries)

# add
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

# update
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

# remove
set_countries.remove('col')
print(set_countries)

# si el elemento no existe entonces envía error
set_countries.remove('ar')
set_countries.discard('arg')
print(set_countries)

set_countries.add('arg')

# Limpiar diccionario
set_countries.clear()
print(set_countries)
print(len(set_countries))
