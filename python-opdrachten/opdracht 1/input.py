#Mijn Python code.
name = input('Geef me jouw naam: ')
age = int(input('Geef me jouw leeftijd: '))
yearofNow = int(input("Welk jaar is het nu: "))
ageHundred = yearofNow - age + 100
 
print("Jouw naam is " + name)
print("Jij bent " + str(age) + " oud")
print("Jij wordt in het jaar " + str(ageHundred) + " ,100 jaar oud.")
