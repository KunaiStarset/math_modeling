n = int(input('Введите кол-во чисел для вывода: '))
i = 2
b = 1
c = 1
a = 0

print (b, c, sep = '\n' )
while i <= n:
  a = b + c
  b = c
  c = a
  print (a)
  i += 1