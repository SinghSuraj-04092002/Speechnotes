from cgitb import text
from decimal import Rounded
from tkinter import *
from PIL import ImageTk, Image
from tkinter.messagebox import*
from click import command


################################################################Functionality#########################################################################
def close_window():
    root.destroy()
    import login

def text_editor():
    root.destroy()
    import texteditor

def translator():
    root.destroy()
    import translator

def Converter():
    root.destroy()
    import Audiototext

def paraphrasing():
    root.destroy()
    import paraphrasing

def about():
    import about   





root = Tk()

canvas= Canvas(root,width=1440,height=1024)
image=ImageTk.PhotoImage(Image.open("image\Desktop - 3 (3).png"))
root.title('Speechnotes')
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

#==========================================================Frames=============================================================


frame1 = Frame(root,bg ="snow",width=289,height=81, relief=FLAT)
frame1.place(x=104, y=200)
label_frame = Label(frame1,fg="black",bg="snow",text = "Turn Your Speech",font=("Times New Roman bold",40))
label_frame.pack()

frame2 = Frame(root,bg ="snow",width=289,height=81, relief=FLAT)
frame2.place(x=100, y=270)
label_frame = Label(frame2,fg="purple3",bg="snow",text = "Into Text right now.",font=("Times New Roman bold",40))
label_frame.pack()

frame3 = Frame(root,bg ="snow",width=289,height=81, relief=FLAT)
frame3.place(x=130, y=350)
label_frame = Label(frame3,fg="black",bg="snow",text = "A platform where you can convert your \n speech into text can perform various task too.",font=("Times New Roman",15))
label_frame.pack()

#============================================================Buttons=========================================================

Button_getstarted=Button(root, text='Get Started',font=("Times New Roman bold",20),width=10,bg='purple4',fg='white',
                            cursor="hand2",command=text_editor).place(x=220,y=420)

homebutton = Button(root, text='Home', font=('Times New Roman bold',20), bd=0, fg='purple4', bg='white',
                      cursor='hand2',
                      activebackground='white', activeforeground='gray20')
homebutton.place(x=50, y=35)

txteditorbutton = Button(root, text='Text Editor', font=('Times New Roman bold',20), bd=0, fg='purple4', bg='white',
                      cursor='hand2',command=text_editor,
                      activebackground='white', activeforeground='gray20')
txteditorbutton.place(x=150, y=35)

translatorbutton = Button(root, text='Translator', font=('Times New Roman bold',20), bd=0, fg='purple4', bg='white',
                      cursor='hand2',command=translator,
                      activebackground='white', activeforeground='gray20')
translatorbutton.place(x=315, y=35)

Convertor = Button(root, text='Converter',font=('Times New Roman bold',20), bd=0, fg='purple4', bg='white',
                      cursor='hand2',command=Converter,
                      activebackground='white', activeforeground='gray20')
Convertor.place(x=490, y=35)


aboutbutton = Button(root, text='About', font=('Times New Roman bold',20), bd=0, fg='purple4', bg='white',
                      cursor='hand2',command=about,
                      activebackground='white', activeforeground='gray20')
aboutbutton.place(x=840, y=35)

Button_logout=Button(root, text='Logout',font=("Times New Roman bold",15),width=10,bg='purple4',fg='white',
                            cursor="hand2",command=close_window).place(x=1200,y=30)

Paraphrasing = Button(root, text='Paraphrasing',font=('Times New Roman bold',20), bd=0, fg='purple4', bg='white',
                      cursor='hand2',command=paraphrasing,
                      activebackground='white', activeforeground='gray20')
Paraphrasing.place(x=650, y=35)



root.mainloop()