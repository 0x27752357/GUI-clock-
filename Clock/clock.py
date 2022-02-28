
from calendar import day_name
from tkinter import *
from time import *
from tkinter import font
from turtle import right
from typing import Literal



def update() :
    
        time_string = strftime("%I:%M:%S %p")
        time_lable.config(text=time_string) 
        

        
        day_string = strftime("%A %B %Y") #%A %B %Y
        day_lable.config(text=day_string) 
        
        
        time_lable.after(1000 , update)
    


window = Tk()

time_lable = Label(window , font=("Arial" , 50) , fg="white" , bg="#4285F4" , justify="center" )
time_lable.pack()


day_lable = Label(window , font=("Arial" , 25) , fg="white" , bg="#DB4437")
day_lable.pack()



update()
window.mainloop()
