nato = {"A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"}

print("==================\nNATO PHONETIC ALPHABET\n==================\n")

name = input("Please enter your name: ").upper()
print("The spelling of your name is phonetically is: ")
for letter in name:
        if letter in nato:
                word = nato[letter]
                print(f"{letter}: {word}")
        elif letter == " ":
                print("___")
        else:
                print(f"{letter}: {letter}")