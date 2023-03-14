#Mijn Python code.
inputNumber = int(input('Type een nummer in: '))
result = int(inputNumber)

if result % 4 == 0:
    print('Dit getal is een veelvoud van 4')
elif result % 2 == 0:
    print('Dit getal is een even getal.')
else:
    print('Dit getal is een oneven getal')

num = int(input('Type een getal in: '))
check = int(input('Type een deel getal in: '))

if num % check == 0:
    print('Dit getal is gelijkmatig')
else: 
    print('Dit getal is niet gelijkmatig')