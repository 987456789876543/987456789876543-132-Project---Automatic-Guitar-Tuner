######################################################################
# program to define a gui and excecute the wanted programs based off
# the information obtained from the gui
######################################################################
from tkinter import *

#function to display the current target note
def showNote(x):
    notes= ["E2", "A2", "D3", "G3", "B3", "E4"]
    currentNote["text"]=f"current target note: {notes[x]}"

#determine the direction the motor needs to rotate by getting which
#box which was checked
def getDirection():
    if clockwise.get():
        return 1
    return 0

#get the wanted frequency, then run the function to rotate the motor
def tune():
    #make sure a note and direction have been selected before proceeding
    if not check():
        return
    
    #dictionary pairing notes to their corresponding frequencies
    notes = {"E2":82, "A2":110, "D3":147, "G3":196, "B3":247, "E4":330}
    
    #get wanted frequency by looking at the current note and matching it to its frequency
    currentFreq = notes[currentNote["text"][-2:]]

    #get the selected direction, 1 for clockwise and 0 for counter clockwise
    direction = getDirection()
    
    #turnMotor()
    print(f'''current target frequency: {currentFreq}
{currentNote["text"]}
current direction: {getDirection()}\n''')

#function to ensure a note and direction has been selected
def check():
    try:
        currentNote["text"][-1]
    except:
        return False
    return clockwise.get() or counterClockwise.get() 

window = Tk()

#buttons for each note
e1 = Button(text="E2", width=20, command=lambda: showNote(0))
e1.grid(row=0,column=0,sticky=N+S+E+W)

a1 = Button(text="A2", width=20, command=lambda: showNote(1))
a1.grid(row=0,column=1,sticky=N+S+E+W)

d1 = Button(text="D3", width=20, command=lambda: showNote(2))
d1.grid(row=0,column=2,sticky=N+S+E+W)

g1 = Button(text="G3", width=20, command=lambda: showNote(3))
g1.grid(row=1,column=0,sticky=N+S+E+W)

b1 = Button(text="B3", width=20, command=lambda: showNote(4))
b1.grid(row=1,column=1,sticky=N+S+E+W)

e2 = Button(text="E4", width=20, command=lambda: showNote(5))
e2.grid(row=1,column=2,sticky=N+S+E+W)

#label asking whick direction the tuning key needs to turn to toghten the string
c = Label(text="Turn Clockwise or Counterclockwise to tighten?")
c.grid(row=3,columnspan=2,sticky=N+S+E+W, pady=15)

#make boxes for clockwise and counter clockwise, set the other box to be 0 so both
#are never checked at the same time
clockwise = IntVar()
Checkbutton(text="Clockwise",variable=clockwise, command=lambda: counterClockwise.set(0)).grid(row=4,column=0)

counterClockwise = IntVar()
Checkbutton(text="Counterclockwise",variable=counterClockwise, command=lambda: clockwise.set(0)).grid(row=4,column=1)

#display current selected note
currentNote= Label(text="")
currentNote.grid(row=3, column=2, sticky=N+S+E+W)

#button to start the function to get the frequencies and turn the motor
start = Button(text="start", command=tune)
start.grid(row=4, column=2, sticky=N+S+E+W)


window.mainloop()
