a = int (input ('Введите первое число: '))
b = int (input ('Введите второе число: '))

if a == 0 or b == 0:
  print ('На 0 делить нельзя')
elif a % b == 0:
  print ('Делится нацело')
  print ('Остатка нет')
  print (a / b)
else:
  print ('Не делятся нацело')