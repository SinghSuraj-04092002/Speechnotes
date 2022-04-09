from cgitb import text
from tkinter import *
from PIL import ImageTk, Image
from tkinter.messagebox import*
from cProfile import label
from tkinter import ttk,messagebox
from tokenize import Whitespace 
import googletrans
from googletrans import Translator
import textblob
from click import command
import speech_recognition as sr
import pyttsx3


#################################################Buttons Function#############################################################
def close_window():
    root.destroy()
    import login

def text_editor():
    root.destroy()
    import texteditor

def home():
    root.destroy()
    import home

def Converter():
    root.destroy()
    import Audiototext

def about():
    import about

def paraphrasing():
    root.destroy()
    import paraphrasing  

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)

###############################################Translator & Text To Speech########################################################3
def translate_now():
    text_=text1.get(1.0,END)
    t1=Translator()
    trans_text=t1.translate(text_,src=combo1.get(),dest=combo2.get())
    trans_text= trans_text.text

    text2.delete(1.0,END)
    text2.insert(END,trans_text)

    # Initialize the Speech engine
    engine = pyttsx3.init()

    # engine Property
    engine.setProperty('rate', 125)
    engine.setProperty('volume', 100)

    # Pass text to speech engine
    engine.say(text2.get(1.0, END))

    # Run to engine
    engine.runAndWait()


language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()


def clear():
    text1.delete(1.0, END)
    text2.delete(1.0, END)


###############################################################Speech To Text###################################################

def main():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Please say something")
        audio = r.listen(source)
        try:
            for key, value in language.items():
                if (value == combo1.get()):
                    from_language_key = key
            query = r.recognize_google(audio, language=from_language_key)
        except Exception as e:
            messagebox.showinfo(title='Error!', message=e)
        return query
            
        # write audio
        #with open("recorded.wav", "wb") as f:
            #f.write(audio.get_wav_data())


            
    

root = Tk()

canvas= Canvas(root,width=1440,height=1024)
image=ImageTk.PhotoImage(Image.open("image\Desktop - 5.png"),height=800,width=1220)
root.title('Speechnotes')
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

frame2 = Frame(root,bg ="snow",width=100,height=100,relief=FLAT,bd=0)
frame2.place(x=650, y=120)
# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("image\Ellipse 26.jpg"))
# Create a Label Widget to display the text or Image
label = Label(frame2, image = img)
label.pack()

#==========================================================Engish Frames=============================================================

combo1=ttk.Combobox(root,values=languageV,font=("Times New Roman bold",15),state="r")
combo1.place(x=250,y=150)
combo1.set("Select language")

label1=Label(root,text="ENGLISH",font=("Times New Roman bold",20),bg="snow",width=15,fg="magenta4")
label1.place(x=250,y=200)

f1=Frame(root,bd=5,bg="black")
f1.place(x=70,y=270,width=610,height=360)

text1=Text(f1,font=("Times New Roman bold",12),bg="white",relief=GROOVE,wrap=WORD,bd=5)
text1.place(x=0,y=0,width=600,height=350)

scrollbar1=Scrollbar(text1)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


#===========================================================Select language frame=======================================================

combo2=ttk.Combobox(root,values=languageV,font=("Times New Roman bold",15),state="r")
combo2.place(x=970,y=150)
combo2.set("SELECT LANGUAGE")

label2=Label(root,text="ENGLISH",font=("Times New Roman bold",20),bg="snow",width=20,fg="magenta4")
label2.place(x=927,y=200)

f2=Frame(root,bg="black",bd=5)
f2.place(x=733,y=270,width=610,height=360)

text2=Text(f2,font=("Times New Roman bold",12),bg="white",relief=GROOVE,wrap=WORD,bd=5)
text2.place(x=0,y=0,width=600,height=350)

scrollbar2=Scrollbar(text2)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

label_change()


#============================================================Buttons=========================================================

homebutton = Button(root, text='Home', font=('Times New Roman bold',20), bd=0, fg='purple4', bg='white',
                      cursor='hand2',command=home,
                      activebackground='white', activeforeground='gray20')
homebutton.place(x=50, y=35)

txteditorbutton = Button(root, text='Text Editor', font=('Times New Roman bold',20), bd=0, fg='purple4', bg='white',
                      cursor='hand2',command=text_editor,
                      activebackground='white', activeforeground='gray20')
txteditorbutton.place(x=150, y=35)

translatorbutton = Button(root, text='Translator', font=('Times New Roman bold',20), bd=0, fg='purple4', bg='white',
                      cursor='hand2',
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

Paraphrasing = Button(root, text='Paraphrasing',font=('Times New Roman bold',20), bd=0, fg='purple4', bg='white',
                      cursor='hand2',command=paraphrasing,
                      activebackground='white', activeforeground='gray20')
Paraphrasing.place(x=650, y=35)

Button_logout=Button(root, text='Logout',font=("Times New Roman bold",15),width=10,bg='purple4',fg='white',
                            cursor="hand2",command=close_window).place(x=1200,y=30)

translate=Button(root,text="Translate", font= ("Times New Roman bold",15), 
                        activebackground="purple",cursor="hand2",bd=5,bg='purple4',fg="white",command=translate_now)
translate.place(x=650,y=650)

clear1=Button(root,text="Clear", font= ("Times New Roman bold",15), 
                        activebackground="purple",cursor="hand2",bd=5,bg='purple4',fg="white",command=clear)
clear1.place(x=1200,y=650)

Speak=Button(root,text="Speak", font= ("Times New Roman bold",15), 
                        activebackground="purple",cursor="hand2",bd=5,bg='purple4',fg="white",command=lambda: text1.insert(END, main()))
Speak.place(x=500,y=650)



root.mainloop()