def sum_with_range(min, max):
  sum = 0
  for x in range(min, max):
    sum += x
  return sum


result = sum_with_range(1, 4)

print(type(result))

if result > 4:
  print(result)

result2 = sum_with_range(result, 10 + 12)

print(result2)

sum_with_range(1, 2)
'''
def calculator(num_1, num_2, op):
  result = 0

  if op == "+":
    result = num_1 + num_2

  elif op == "-":
    result = num_1 - num_2

  elif op == "*":
    result = num_1 * num_2

  elif op == "/":
    result = num_1 / num_2

  print(f"{num_1} {op} {num_2} = {result}")

if __name__ == '__main__':
  list_op = ("+", "-", "*", "/")
  op = str(input(f'choose operator with symbol {list_op}: '))
  num_1 = int(input('Choose number: '))
  num_2 = int(input('Choose other number: '))
  calculator(num_1, num_2, op)
'''
