import audioop
from cgitb import text
from cmath import e
from decimal import Rounded
from sre_constants import IN
#from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
#from tkinter.tix import ComboBox
from PIL import ImageTk, Image
from tkinter.messagebox import*
from click import command
import wave, math, contextlib
import speech_recognition as sr
#import moviepy as mp
import moviepy.editor as mp
from tkinter import filedialog
import os 
from os import path
import pydub as AudioSegment
import tempfile
from pathlib import Path
import subprocess
import googletrans
import speech_recognition as sr
from textblob import TextBlob
from pydub import AudioSegment
from pydub.silence import split_on_silence


################################################################ Navigation Functionality #########################################################################

def close_window():
    root.destroy()
    import login

def text_editor():
    root.destroy()
    import texteditor

def translator():
    root.destroy()
    import translator

def home():
    root.destroy()
    import home

def paraphrasing():
    root.destroy()
    import paraphrasing

def about():
    import about   



#======================================================================Window===========================================================

root = Tk()

canvas= Canvas(root,width=1440,height=1024)
image=ImageTk.PhotoImage(Image.open("image\Desktop - 3 (3).png"))
root.title('Speechnotes')
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()


#==========================================================Audio to Text=============================================================

#Insert Audio
def add_audio():
    audio = filedialog.askopenfilename(defaultextension="audio.wav")
    Audio_box.insert(END, audio)


frame1 = Frame(root,bg ="snow",width=600,height=700, highlightthickness=5, highlightbackground= 'black', relief=FLAT)
frame1.place(x=80, y=50)
label1=Label(frame1,text="Audio To Text",font=("Times New Roman bold",20),bg="snow",width=20,fg="magenta4")
label1.place(x=125,y=10)

lbl_audio = Label(frame1, text="Audio File:",font=("Times New Roman bold",15), bg ="Snow",fg="purple4",width=15)
lbl_audio.place(x=15, y=70)

#List Box
Audio_box = Listbox(frame1, bg="white",fg="purple4")
Audio_box.place(x=200, y=70,width=250,height=35)

Insert_Button = Button(frame1, text="Insert",font=("Times New Roman bold",15), cursor="hand2", bg="snow" , fg="purple4",bd=0,command=add_audio)
Insert_Button.place(x=480, y=70)

text_1=Text(frame1, width=70,height=25,highlightbackground='black',highlightthickness=2)
text_1.place(x=15,y=200)
text_1.config(wrap='word')

convert_btn = Button(frame1, text="Audio to text",font=("Times New Roman bold",20),width=10,bg='purple4',fg='white',cursor="hand2",command=lambda: text_1.insert(END, conversionad()))
convert_btn.place(x=225,y=625)

# Grab Language List From GoogleTrans
languages1 = googletrans.LANGUAGES
StringVar = googletrans.LANGUAGES

# Convert to list
language_list_1 = list(languages1.values())

translated_combo_2 = Combobox(frame1, width=20, value=language_list_1,font="arial 14")
translated_combo_2.current(22)
translated_combo_2.place(x=200,y=120)
translated_combo_2.set('Select language')

def conversionad():
    r = sr.Recognizer()
    audio_file= sr.AudioFile(Audio_box.get(ACTIVE))
    with audio_file as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio2 = r.record(source)           
        try:
            for key, value in languages1.items():
                if (value==translated_combo_2.get()):
                    l1=key
            query = r.recognize_google(audio_data=audio2, language=l1)
               
        except Exception as e:
            messagebox.showinfo(title='Error!', message=e)
           

            return "Nothing"
        return query

#Save File 
def print_area(txt):
    temp_file = tempfile.mktemp('.txt')
    open(temp_file, 'w').write(txt)
    os.startfile(temp_file, 'print')

btn_print = Button(frame1, text="Print", font=("Helvetica", 15), bg = 'Purple4', fg='snow', command=lambda:print_area(text_1.get('1.0', END)))
btn_print.place(x=470, y= 625)

#===========================================================Video to Text=========================================================

#Insert Video
def add_video():
    video = filedialog.askopenfilename(defaultextension=".mp4")
    Video_box.insert(END, video)

def conversion():
    clip=mp.VideoFileClip(Video_box.get(ACTIVE))
    clip.audio.write_audiofile(Entry_vid.get())
    r = sr.Recognizer()
    audio = sr.AudioFile(Entry_vid.get())
    with audio as source:
        r.adjust_for_ambient_noise(source, duration=1)       
        audtext = r.record(source, duration=1000)
        try:
            for key, value in languages.items():
                
                if (value == translated_combo.get()):
                    from_language_key = key            
            query = r.recognize_google(audtext, language=from_language_key)
               
        except Exception as e:
            messagebox.showinfo(title='Error!', message=e)
           

            return "Nothing"
        return query


frame2 = Frame(root,bg ="snow",width=600,height=700, highlightthickness=5, highlightbackground= 'black', relief=FLAT)
frame2.place(x=730, y=50)
label2=Label(frame2,text="Video To Text",font=("Times New Roman bold",20),bg="snow",width=20,fg="magenta4")
label2.place(x=125,y=10)

lbl_video = Label(frame2, text="Video File:",font=("Times New Roman bold",15), bg ="Snow",fg="purple4",width=15)
lbl_video.place(x=15, y=70)

lbl_Filename = Label(frame2, text="Filename:",font=("Times New Roman bold",15), bg ="Snow",fg="purple4",width=15)
lbl_Filename.place(x=15, y=125)

# Grab Language List From GoogleTrans
languages = googletrans.LANGUAGES
StringVar = googletrans.LANGUAGES

# Convert to list
language_list = list(languages.values())

translated_combo = Combobox(frame2, width=20, value=language_list,font="arial 14")
translated_combo.current(22)
translated_combo.place(x=200,y=160)
translated_combo.set('Select language')


#List Box
Video_box = Listbox(frame2, bg="white",fg="purple4",border=2)
Video_box.place(x=200, y=70,width=250,height=35)

Insert_Button = Button(frame2, text="Insert",font=("Times New Roman bold",15), cursor="hand2", bg="snow" , fg="purple4",bd=0,command=add_video)
Insert_Button.place(x=480, y=70)

text_2=Text(frame2, width=70,height=25,highlightbackground='black',highlightthickness=2)
text_2.place(x=15,y=200)
text_2.config(wrap='word')

Entry_vid = Entry(frame2, bg="White",fg="Purple4",border=2)
Entry_vid.insert(0, "Filename .wav")
Entry_vid.place(x=200,y=125,width=250,height=25)

convert_btn1 = Button(frame2, text="Video to text",font=("Times New Roman bold",20),width=10,bg='purple4',fg='white',cursor="hand2",command=lambda: text_2.insert(END, conversion()))
convert_btn1.place(x=225,y=625)

#Save File
def print_area(txt):
    temp_file = tempfile.mktemp('.txt')
    open(temp_file, 'w').write(txt)
    os.startfile(temp_file, 'print')

btn_print = Button(frame2, text="Print", font=("Helvetica", 15), bg = 'Purple4', fg='snow', command=lambda:print_area(text_2.get('1.0', END)))
btn_print.place(x=470, y= 625)


#============================================================Navigation Buttons=========================================================

Home = Button(root,text='Home',font=("Helvetica"),width=10,compound=LEFT,background="white",fg="purple",cursor='hand2',bd=0,command=home)
Home.place(x=1,y=0)

Text_Editor = Button(root,text='Text Editor',font=("Helvetica"),width=10,compound=LEFT,background="white",fg="purple",cursor='hand2',bd=0,command=text_editor)
Text_Editor.place(x=120,y=0)

Translator = Button(root,text='Translator',font=("Helvetica"),width=10,compound=LEFT,background="white",fg="purple",cursor='hand2',bd=0,command=translator)
Translator.place(x=230,y=0)

Convertor = Button(root, text='Convertor',font=("Helvetica"),width=10,compound=LEFT,background="white",fg="purple",cursor='hand2',bd=0)
Convertor.place(x=350, y=0)

About = Button(root,text='About',font=("Helvetica"),width=10,compound=LEFT,background="white",fg="purple",cursor='hand2',bd=0,command=about)
About.place(x=625,y=0)

Paraphrasing= Button(root,text='Paraphrasing',font=("Helvetica"),width=10,compound=LEFT,background="white",fg="purple",cursor='hand2',bd=0,command=paraphrasing)
Paraphrasing.place(x=480,y=0)

LogOut_button = Button(root, text='LogOut',compound=LEFT,font=("Helvetica"),background='Magenta4',width=10, fg='White',command=close_window)
LogOut_button.place(x=1150,y=0)



root.mainloop()