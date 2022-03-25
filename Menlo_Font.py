from time import * 
from tkinter import *
import os 



def time_show() :
    hour = strftime("%H:%M:%S")
        
    
    Hour_label.config(text=hour)
    Hour_label.after(1000 , time_show)    
        
    
    
    



window = Tk()

window.title("Time")

window.geometry("150x40") # 150x40

Hour_label = Label(window , font=('Menlo',30) , bg="white" , fg="black")
Hour_label.grid(row=0)

time_show()

window.mainloop()