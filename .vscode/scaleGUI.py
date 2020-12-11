from tkinter import *
from playsound import playsound
# Sets Init Values For the Variables
noteIntake = "Init"
majorMinor = "Init"
doIntake = "Init"
notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
# Gets Values From GUI, assigns them, prints them out and plays sound
def getNums():
    majorMinor = enterMM.get()
    noteIntake = enterKey.get()
    doIntake = enterSolfege.get()
    if majorMinor == "Major":
        numList = {}
        numList["Do"] = 0
        numList["Re"] = 2
        numList["Mi"] = 4
        numList["Fa"] = 5
        numList["Sol"] = 7
        numList["La"] = 9
        numList["Ti"] = 11
    elif majorMinor == "Minor":
        numList = {}
        numList["Do"] = 0
        numList["Re"] = 2
        numList["Mi"] = 3
        numList["Fa"] = 5
        numList["Sol"] = 7
        numList["La"] = 8
        numList["Ti"] = 10
    while noteIntake != notes[0]:
        counter = 11
        holder = notes[11]
        for i in reversed(notes):
            notes[counter] = notes[counter - 1]
            counter = counter -1
        notes[0] = holder
    print(notes)
    print(notes[numList[doIntake]])
    labelAnswer = Label(root, text = notes[numList[doIntake]])
    labelAnswer.grid(row = 3, column = 1)
    playsound('C:/Users/Evanf/Music/PianoNotes/%s.wav' %(notes[numList[doIntake]]))
# GUI organization
root = Tk()
root.geometry("500x200")
labelMM = Label(root, text = "Major or Minor?")
labelKey = Label(root, text = "What Key?")
labelSolfege = Label(root, text = "What Solfege?")
bigButton = Button(root, width = 10, height = 5, text = "Push Me", command = getNums)
bigButton.grid(row = 2, column = 1)
labelMM.grid(row = 1, column = 0)
labelKey.grid(row = 1, column = 1)
labelSolfege.grid(row = 1, column = 2)
enterMM = Entry(root, width = 20)
enterKey = Entry(root, width = 20)
enterSolfege = Entry(root, width = 20)
enterSolfege.grid(row = 0, column = 2)
enterMM.grid(row = 0, column = 0)
enterKey.grid(row = 0,column = 1)
# Sets the major or minor values



root.mainloop()