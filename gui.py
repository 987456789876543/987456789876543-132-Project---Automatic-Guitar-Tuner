from ast import Break
from logging import exception
import getFrequency
from tkinter import *
import time
import numpy as np
import motor


# function to start code in getFrequency
def tune(val):
    getFrequency.NOTE = val
    try:
        global thing
        thing = getFrequency.sd.InputStream(channels=1, callback=getFrequency.callback, blocksize=getFrequency.WINDOW_STEP, samplerate=getFrequency.SAMPLE_FREQ)
        thing.start()
        for i in range (100):
            time.sleep(0.5)
        thing.stop()
        motor.Stop()
    except Exception as exc:
        print(str(exc))
    



window = Tk()

#buttons for each note
e1 = Button(text="E2", width=20, command=lambda: tune(82))
e1.grid(row=0,column=0,sticky=N+S+E+W)

a1 = Button(text="A2", width=20, command=lambda: tune(110))
a1.grid(row=0,column=1,sticky=N+S+E+W)

d1 = Button(text="D3", width=20, command=lambda: tune(147))
d1.grid(row=0,column=2,sticky=N+S+E+W)

g1 = Button(text="G3", width=20, command=lambda: tune(196))
g1.grid(row=1,column=0,sticky=N+S+E+W)

b1 = Button(text="B3", width=20, command=lambda: tune(247))
b1.grid(row=1,column=1,sticky=N+S+E+W)

e2 = Button(text="E4", width=20, command=lambda: tune(330))
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


window.mainloop()