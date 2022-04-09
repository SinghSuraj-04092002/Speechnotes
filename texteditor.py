from cgitb import text
from math import radians
from string import punctuation
from tkinter import *
import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from tkinter import font
from tkinter import ttk,tix
from tkinter.ttk import Combobox
import os
import gtts
import tempfile
from turtle import bgcolor, width
import googletrans
import speech_recognition as sr
from textblob import TextBlob              
import pyttsx3

win= tk.Tk()
win.title("Speechnotes")
win.geometry('1440x1024')
win.configure(background='white')

##################################################### navigating Buttons Functionality########################################

def close_window():
    win.destroy()
    import login

def home():
    win.destroy()
    import home


def translator():
    win.destroy()
    import translator

def Converter():
    win.destroy()
    import Audiototext

def about():
    import about

def paraphrasing():
    win.destroy()
    import paraphrasing


def print_area(txt):
    temp_file = tempfile.mktemp('.txt')
    open(temp_file, 'w').write(txt)
    os.startfile(temp_file, 'print')

######################################## spell checker ######################################################################################################################  


def check_spelling():
    a=TextBlob(text_editor.get(1.0 ,END))
    correct_text=text2.insert(tk.END,a.correct()) 
    correct_text.pack()
   
     


def clear():
    text2.delete(1.0, END)
    text_editor.delete(1.0, END)




#############################################################################################################################################################################
Home=tk.Button(win,text='Home',font=("Helvetica"),width=10,compound=tk.LEFT,background="white",fg="purple",cursor='hand2',bd=0,command=home)
Home.place(x=1,y=0)

Text_Editor=tk.Button(win,text='Text Editor',font=("Helvetica"),width=10,compound=tk.LEFT,background="white",fg="purple",cursor='hand2',bd=0)
Text_Editor.place(x=110,y=0)

Translator=tk.Button(win,text='Translator',font=("Helvetica"),width=10,compound=tk.LEFT,background="white",fg="purple",cursor='hand2',bd=0,command=translator)
Translator.place(x=230,y=0)

Convertor = tk.Button(win, text='Convertor',font=("Helvetica"),width=10,compound=tk.LEFT,background="white",fg="purple",cursor='hand2',bd=0,command=Converter)
Convertor.place(x=350, y=0)

Paraphrasing= Button(win,text='Paraphrasing',font=("Helvetica"),width=10,compound=LEFT,background="white",fg="purple",cursor='hand2',bd=0,command=paraphrasing)
Paraphrasing.place(x=480,y=0)

About=tk.Button(win,text='About',font=("Helvetica"),width=10,compound=tk.LEFT,background="white",fg="purple",cursor='hand2',bd=0,command=about)
About.place(x=610,y=0)

##############################################################################################################################################################


main_menu = tk.Menu()
#file icons
new_icon = tk.PhotoImage(file='image\ew.png')
open_icon = tk.PhotoImage(file='image\open.png')
save_icon = tk.PhotoImage(file='image\save.png')
save_as_icon = tk.PhotoImage(file='image\save_as.png')
exit_icon = tk.PhotoImage(file='image\exit.png')

file = tk.Menu(main_menu, tearoff=False)



#####edit
#edit icons
copy_icon = tk.PhotoImage(file='image\copy.png')
paste_icon = tk.PhotoImage(file='image\paste.png')
cut_icon = tk.PhotoImage(file='image\cut.png')
clear_all_icon = tk.PhotoImage(file='image\clear_all.png')
find_icon = tk.PhotoImage(file='image\ind.png')

edit = tk.Menu(main_menu, tearoff=False)


######## view icons
######## color theme
light_default_icon = tk.PhotoImage(file='image\light_default.png')
light_plus_icon = tk.PhotoImage(file='image\light_plus.png')
dark_icon = tk.PhotoImage(file='image\dark.png')
red_icon = tk.PhotoImage(file='image\ed.png')
monokai_icon = tk.PhotoImage(file='image\monokai.png')
night_blue_icon = tk.PhotoImage(file='image\ight_blue.png')
color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}


# cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
#main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)

win.config(menu=main_menu)
####################################################################################################


#frame=Frame(win,width=1440,height=1024, highlightthickness=1,background='white')
#frame.place(x=0,y=0)

can=tk.Canvas(win,bg="white",height=900,width=900)
coordinates=10,10,800,800
arc=can.create_arc(coordinates,start=0,extent=180,fill='purple1',outline="black" ,width=2)
can.place(x=-300,y=400)

can=tk.Canvas(win,bg="white",height=900,width=900)
coordinates=10,10,800,800
arc=can.create_arc(coordinates,start=90,extent=180,fill='medium purple',outline="black" ,width=2)
can.place(x=1000,y=-350)

LogOut_button =tk.Button(win, text='LogOut',compound=tk.LEFT,font=("Helvetica"),background='Magenta4',width=10, fg='White',command=close_window)
LogOut_button.place(x=1150,y=40)
###############################################################################################################################################################################################

frame1=Frame(win,width=400,height=300,highlightbackground='black', highlightthickness=2,background='white')
frame1.place(x=940,y=110)
############################################################################################################################

text2=Text(win,width=50,height=15,highlightbackground='black',highlightthickness=2)
text2.place(x=940,y=425,width=400,height=170)
scrollbar1=Scrollbar(text2)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar1.set)

Checkbutton= Button(win, text="check",font=("Arial",15,"bold"),bg="purple4",fg="white",command= check_spelling)
Checkbutton.place(x=1100,y=600)

clearbutton=Button(win, text="clear",font= ("Arial",15,"bold"), activebackground="purple",bg='purple4',fg="white",command=clear)
clearbutton.place(x=1000,y=600)



############################################################################################################################

tool_bar =Frame(win,width=100,height=600,highlightbackground='black', highlightthickness=2,background='white')
tool_bar.place(x=30,y=30)

## font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30,textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)


## size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable = size_var, state='readonly')
font_size['values'] = tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

## bold button
bold_icon = tk.PhotoImage(file='image\icons8-bold-50.png')
bold_btn = tix.Button(tool_bar, image=bold_icon,bg='white')
bold_btn.grid(row=0, column=3, padx=5)

## italic button
italic_icon = tk.PhotoImage(file='image\icons8-italic-48.png')
italic_btn = tix.Button(tool_bar, image=italic_icon, bg='white')
italic_btn.grid(row=0, column=7, padx=5)

## underline button
underline_icon = tk.PhotoImage(file='image\icons8-underline-50.png')
underline_btn = tix.Button(tool_bar, image = underline_icon,bg='white')
underline_btn.grid(row = 0, column=10, padx=5)

## font color button
font_color_icon = tk.PhotoImage(file='image\icons8-color-wheel-53.png')
font_color_btn = tix.Button(tool_bar, image=font_color_icon,bg='white')
font_color_btn.grid(row=0, column=14,padx=5)

## align left
align_left_icon = tk.PhotoImage(file='image\icons8-align-left-50.png')
align_left_btn = tix.Button(tool_bar, image=align_left_icon,bg='white')
align_left_btn.grid(row=0, column=18, padx=5)

## align center
align_center_icon = tk.PhotoImage(file='image\icons8-align-center-50.png')
align_center_btn = tix.Button(tool_bar, image=align_center_icon,bg='white')
align_center_btn.grid(row=0, column=22, padx=5)

## align right
align_right_icon = tk.PhotoImage(file='image\icons8-align-right-50.png')
align_right_btn = tix.Button(tool_bar, image=align_right_icon,bg='white')
align_right_btn.grid(row=0, column=26, padx=5)

################################################################################

text_editor=Text(win, width=98,height=29,highlightbackground='black',highlightthickness=2)
text_editor.place(x=30,y=110,width=900,height=534)
text_editor.config( relief=tk.FLAT)

scrollbar1=Scrollbar(text_editor)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text_editor.yview)
text_editor.configure(yscrollcommand=scrollbar1.set)


# font family and font size functionality
current_font_family = 'Arial'
current_font_size = 12

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))

font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)


######################################################################################################################################################################################33
# bold button functionality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_btn.configure(command=change_bold)


# italic functionlaity
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

italic_btn.configure(command=change_italic)

# underline functionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

underline_btn.configure(command=change_underline)


## font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_font_color)

### align functionality
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)

## center
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)

## right
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)

text_editor.configure(font=('Times New Roman', 12))

##############################################################################3
############################################## main menu functinality ###################################################

## variable
url = ''

## new functionality
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)

## file commands
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)

## open functionality
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '.txt'), ('All files', '.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    win.title(os.path.basename(url))

file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)

## save file
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '.txt'), ('All files', '.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return

file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command = save_file)


## save as functionality
def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '.txt'), ('All files', '.*')))
        url.write(content)
        url.close()
    except:
        return


file.add_command(label='Save As', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=save_as)

## exit functionality
def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        win.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '.txt'), ('All files', '.*')))
                    url.write(content2)
                    url.close()
                    win.destroy()
            elif mbox is False:
                win.destroy()
        else:
            win.destroy()
    except:
        return
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_func)


############ find functionality

def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ## frame
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

    ## label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()

## edit commands
edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C', command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+V', command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X', command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X', command= lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F', command = find_func)



## color theme
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count += 1
################################################################text to speech####################################################

#text = text_editor.get(1.0, tk.END)
def translate_it():
	try:
		for key, value in languages.items():
			if (value == translated_combo.get()):
				to_language_key = key

		# Turn Original Text into a TextBlob
		words = TextBlob(text_editor.get(1.0, END))
		engine = pyttsx3.init()
		voices = engine.getProperty("voices")
		engine.say(words)
		engine.runAndWait()
    
    
	except Exception as e:
		messagebox.showerror("Translator", e)

# Grab Language List From GoogleTrans
languages = googletrans.LANGUAGES
StringVar = googletrans.LANGUAGES

# Convert to list
language_list = list(languages.values())

Speak = tk.PhotoImage(file='image\Human.png')
translate_button =Button(frame1, text="Speak", compound=tk.LEFT,font=("Helvetica", 24), command=translate_it,background='Magenta4',image=Speak,width=180,fg="White")
translate_button.place(x=100,y=220)

btn_print = tk.Button(win, text="Save", font=("Helvetica", 15), bg = 'Purple4', fg='snow', command=lambda:print_area(text_editor.get('1.0', END)))
btn_print.place(x=850, y= 650)

translated_combo = ttk.Combobox(frame1, width=20, value=language_list,font="arial 14")
translated_combo.current(22)
translated_combo.place(x=70,y=40)
translated_combo.set('Select language')

speed_combobox=ttk.Combobox(frame1,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=20)
speed_combobox.place(x=70,y=180)
speed_combobox.set('Normal')

Select_language=Label(frame1,text='Select language',font=("Helvetica",15),width=20,compound=tk.RIGHT,background="white",fg="purple")
Select_language.place(x=90,y=0)

Speed=Label(frame1,text='Speed',font=("Helvetica",15),width=20,compound=tk.RIGHT,background="white",fg="purple")
Speed.place(x=90,y=150)

########################################################Speech To Text#################################################

def main():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Please say something")
        audio = r.listen(source)
        try:
            for key, value in languages.items():
                if (value == translated_combo.get()):
                    from_language_key = key
            query = r.recognize_google(audio, language=from_language_key)
        except Exception as e:
            messagebox.showinfo(title='Error!', message=e)
            # print("Error :  " + str(e))
        return query
            
        # write audio
        #with open("recorded.wav", "wb") as f:
            #f.write(audio.get_wav_data())




mic = tk.PhotoImage(file='image\icons8-microphone-55.png')    
record_btn = tix.Button(frame1,compound=tk.LEFT,text='Record',image=mic,font=("Helvetica", 22), command=lambda: text_editor.insert(tk.END, main()),width=180,background='Magenta4',fg="White")
record_btn.place(x=100, y=80)

win.mainloop()