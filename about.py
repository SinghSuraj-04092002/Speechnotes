from cgitb import text
from tkinter import *
from PIL import ImageTk, Image
from tkinter.messagebox import*

root = Tk()

canvas= Canvas(root,width=700,height=300)
root.title("Speechnotes")
canvas.create_image(0,0,anchor=NW)
canvas.pack()

#frame2 = Frame(root,bg ="snow",width=600,height=300, relief=FLAT)
#frame2.place(x=0, y=0)
label_frame = Label(root,fg="purple3",text = "This is a platform where one can convert their voice into text by using \n speech recognition technology.                                                                     \n Also user can able to prepare notes by using their voice and later save \n it in pdf format.                                                                                             ",font=("Times New Roman bold",15),width= 50)
label_frame.place(x=0, y=0) 

lable_frame1 = Label(root, fg="purple3",bg="snow",text = "Developed By Suraj Singh , Himanshu Rane, Athrava Takle & Yogesh Kumbhar. \n Gmail: surajsingh04092002@gmail.com")
lable_frame1.place(x=150, y=250)

mainloop()