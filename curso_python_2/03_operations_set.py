set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

set_c = set_a.union(set_b)

print(set_c)

#utilizar operador lógico para la unión de los dos conjuntos
print(set_a | set_b)

#Intersección
set_c = set_a.intersection(set_b)
print(set_c)

#Hacerlo con el operador &
print(set_a & set_b)

# Diferencia
set_c = set_a.difference(set_b)
print(set_c)

#Con operador
print(set_a - set_b)
