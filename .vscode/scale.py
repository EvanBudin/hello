majorMinor = input("Major or Minor?: ")

if majorMinor == "Major":
    noteIntake = input("Enter What Major We Are In?: ")
    numList = {}
    numList["Do"] = 0
    numList["Re"] = 2
    numList["Mi"] = 4
    numList["Fa"] = 5
    numList["So"] = 7
    numList["La"] = 9
    numList["Ti"] = 11
elif majorMinor == "Minor":
    noteIntake = input("Enter What Minor We Are In?: ")
    numList = {}
    numList["Do"] = 0
    numList["Re"] = 2
    numList["Mi"] = 3
    numList["Fa"] = 5
    numList["So"] = 7
    numList["La"] = 8
    numList["Ti"] = 10

doIntake = input("What Pitch Are You Looking For?: ")
notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

while noteIntake != notes[0]:
    counter = 11
    holder = notes[11]
    for i in reversed(notes):
        notes[counter] = notes[counter - 1]
        counter = counter -1
    notes[0] = holder
print(notes)
print(notes[numList[doIntake]])