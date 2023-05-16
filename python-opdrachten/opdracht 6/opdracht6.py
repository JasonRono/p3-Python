# Opdracht 6.
word = input("Type een woord in:")  # Input waar de gebruiker zijn woord in kan typen.
word = str(word)  # Zorgt dat het word in een string word gezet.
reverse = word[::-1]  # Draait het word om.
print(reverse)  # Print het omgedraaide woord uit.

if word == reverse:
    print("Dit woord is een palindroom.")
else:
    print("Dit woord is geen palindroom")
