print('Hola')


def my_print(text):
  print(text * 2)
  print('Llamo a la función print dentro de my_print' + text)
  print('Llamo a la función print dentro de my_print 2' + text)


my_print('oiga')

def suma(a, b, c):
  d = a + b + c
  print(d)

suma(12, 13, 14)
suma(1, 2, 3)

