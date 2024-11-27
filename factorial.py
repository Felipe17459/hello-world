#Mi Modificacion:

def factorial(n):
  if n == 0:
    return 1
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result

print(factorial(5))

#Este programa que cuenta la factorial de multiplacion de un numero