import random  # Importeert de random functie.

guesInput = input(
    "Kies een getal? "
)  # Input waarin de gebruiker zijn nummer moet invoeren.

if guesInput.isdigit():  # Checkt of de gebruiker een getal heeft ingevoerd.
    guesInput = int(
        guesInput
    )  # Variabele waarin de gebruiker zijn antwoord wordt verwerkt in een interger.

    if guesInput <= 0:  # Als het getal kleiner is dan 0 dan stopt de code.
        print("Het getal is groter dan 0 probeer het nog een keer")
        quit()
else:
    print("Dit is geen nummer!")
    quit()  # Zorgt dat de code meteen stopt.

randomNum = random.randint(0, 10)  # Kiest een getal tussen 0 en 10.
score = 0  # Variabele waarin de score word bijgehouden

while True:  # Als de gebruiker een getal heeft ingevoerd word de while loop uitgevoerd.
    score += 1  # Elke keer als er verkeerd word geraden word 1 opgeteld bij de score.
    guesInput2 = input("Raad het nog een keer ")

    if guesInput2.isdigit():
        guesInput2 = int(guesInput2)
    else:
        print("Type een nummer in!")
        continue  # Ook al word er verkeerd geraden het spel blijft doorvragen

    if guesInput2 == randomNum:
        print("Je hebt het juiste nummer geraden!")
        break  # Als de gebruiker het nummer heeft geraden word het spel stop gezet.
    elif guesInput2 > randomNum:
        print("Je zat boven het nummer")
    else:
        print("Je zat onder het nummer")
print(
    "Je hebt het in ", score, "moeten raden"
)  # Laat de score zien na hoeveel keer je het geraden hebt.
