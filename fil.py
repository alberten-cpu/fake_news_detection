import tkinter as tk
import os

def callback():
    filename = 'prediction.py'
    os.system(filename) #Open file [Same as Right-click Open]
    
    
    
def show_entry_fields():
    print("gggg: %s" % (e1.get()))

master = tk.Tk()
tk.Label(master, 
         text="enter the text").grid(row=0)

e1 = tk.Entry(master)

e1.grid(row=0, column=1)


tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)


tk.Button(master, 
          text='show', command=lambda:(callback(),show_entry_fields())).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)
    
tk.mainloop()