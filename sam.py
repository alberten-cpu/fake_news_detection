from tkinter import * 
from tkinter.ttk import *
from time import strftime 
  
# creating tkinter window 
root = Tk() 
 master=TK(className="sample_Tkinter")
master.geimetry("500x500") 
# Adding widgets to the root window 
Label(root, text = 'GeeksforGeeks',  
      font =('Verdana', 15)).pack(side = TOP, pady = 10) 
  
Button(root, text = 'Click Me !').pack(side = TOP) 
  
mainloop() 