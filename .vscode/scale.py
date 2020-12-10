majorMinor = input("Major or Minor?: ")

if majorMinor == "Major":
    noteIntake = input("Enter What Major We Are In?: ")
elif majorMinor == "Minor":
    noteIntake = input("Enter What Minor We Are In?: ")

doIntake = input("What Pitch Are You Looking For?: ")

majorNumList = {}
majorNumList["Do"] = 0
majorNumList["Re"] = 2
majorNumList["Mi"] = 4
majorNumList["Fa"] = 5
majorNumList["So"] = 7
majorNumList["La"] = 9
majorNumList["Ti"] = 11

minorNumList = {}
minorNumList["Do"] = 0
minorNumList["Re"] = 2
minorNumList["Mi"] = 3
minorNumList["Fa"] = 5
minorNumList["So"] = 7
minorNumList["La"] = 8
minorNumList["Ti"] = 10
notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

while noteIntake != notes[0]:
    counter = 11
    holder = notes[11]
    for i in reversed(notes):
        notes[counter] = notes[counter - 1]
        counter = counter -1
        print(notes)
    notes[0] = holder
print(notes)
if majorMinor == "Major":
    print(notes[majorNumList[doIntake]])
elif majorMinor == "Minor":
    print(notes[minorNumList[doIntake]])