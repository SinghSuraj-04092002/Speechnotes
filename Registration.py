from cgitb import text
from sqlite3 import Cursor
from tkinter import *
from PIL import ImageTk, Image
from tkinter.messagebox import*
import mysql.connector 


#======================================================Functions==========================================================
def login_window():
    root.destroy()
    import login

def clear():
    entry_fname.delete(0, END)
    entry_uname.delete(0, END)
    entry_cnum.delete(0, END)
    entry_pwd.delete(0, END)
    entry_cpwd.delete(0, END)
    check.set(0)


def register():
    mobile=entry_cnum.get()
    if entry_fname.get() == '' or entry_uname.get() == '' or entry_cnum.get() == '' or \
            entry_pwd.get() == '' or entry_cpwd.get() == '':
        showerror('Error', "All Fields Are Required", parent=root)

    elif entry_pwd.get() != entry_cpwd.get():
        showerror('Error', "Password Mismatch", parent=root)

    elif len(mobile) >= 10:
        showerror('Error', "Invalid Contact number", parent=root) 

    elif check.get() == 0:
        showerror('Error', "Please Agree To Our Terms & Conditions", parent=root)

    else:
        try:
            # Database Connectivity #
            con =  mysql.connector.connect(host="localhost",user="root",password="",database='speechtotext')
            cur = con.cursor()
            cur.execute('select * from signup where uname', entry_uname.get())
            row = cur.fetchone()
            if row != None:
                showerror('Error', "User Already Exists", parent=root)
            else:

                cur.execute(
                    'insert into signup (fname,uname,cnum,pwd) values(%s,%s,%s,%s)',
                    (entry_fname.get(), entry_uname.get(), entry_cnum.get(), entry_pwd.get(),))
                con.commit()
                con.close()
                showinfo('Success', "Registration Successful", parent=root)
                clear()
                root.destroy()
                import login


        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)    

## Tkinter Window ##
root = Tk()

canvas= Canvas(root,width=1440,height=1024)
image=ImageTk.PhotoImage(Image.open("image\Desktop - 1.jpg"))
root.title('Speechnotes')
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

#======================================================Frames=======================================================================================

frame1 = Frame(root,bg = "snow",width=1150,height=600,relief=FLAT)
frame1.place(x=116, y=69)

frame2 = Frame(root,bg ="snow",width=100,height=100,relief=FLAT)
frame2.place(x=700, y=100)
#Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("image\Ellipse 5.png"))
#Create a Label Widget to display the text or Image
label = Label(frame2, image = img)
label.pack()

frame3 = Frame(root,bg ="snow",width=289,height=81, relief=FLAT)
frame3.place(x=850, y=127)
label_frame = Label(frame3,fg="purple3",bg="snow",text = "SignUp",font=("Times New Roman bold",40))
label_frame.pack()

frame4_img= Frame(root,bg = "purple",width=355,height=600,relief=FLAT)
frame4_img.place(x=160, y=68)

frame5_img = Frame(frame4_img,bg="snow",width=355,height=600,relief=FLAT)
frame5_img.place(x=160, y=68)
img2 = ImageTk.PhotoImage(Image.open("image\Genderless-Voice_02.jpg"))
label_frame5= Label(frame4_img, image = img2)
label_frame5.pack()

#=========================================labels and Textfields=============================================================

label_fname = Label(root, bg="snow", text="Full Name*",width=20,font=("Times New Roman bold", 15),fg="magenta4")
label_fname.place(x=620,y=259)
entry_fname = Entry(root, bg="snow",font=("Times New Roman", 15),highlightthickness="1",
                        highlightbackground="magenta4",highlightcolor="magenta4")
entry_fname.place(x=700,y=294,width=400,height=30)

label_uname = Label(root, bg="snow", text="Username*",width=20,font=("Times New Roman bold", 15),fg="magenta4")
label_uname.place(x=620,y=330)
entry_uname = Entry(root, bg="snow",font=("Times New Roman", 15),highlightthickness="1",
                        highlightbackground="magenta4",highlightcolor="magenta4")
entry_uname.place(x=700,y=365,width=400,height=30)

label_cnum = Label(root, bg="snow", text="Contact no*",width=20,font=("Times New Roman bold", 15),fg="magenta4")
label_cnum.place(x=620,y=400)
entry_cnum = Entry(root, bg="snow",font=("Times New Roman", 15),highlightthickness="1",
                        highlightbackground="magenta4",highlightcolor="magenta4")
entry_cnum.place(x=700,y=435,width=400,height=30)

label_pwd = Label(root, bg="snow", text="Password*",width=20,font=("Times New Roman bold", 15),fg="magenta4")
label_pwd.place(x=620,y=470)
#Create Entry Widget for password
entry_pwd= Entry(root, show="*",bg="snow",font=("Times New Roman", 15),highlightthickness="1",
                        highlightbackground="magenta4",highlightcolor="magenta4")
entry_pwd.place(x=700,y=505,width=400,height=30)

label_cpwd = Label(root, bg="snow", text="Confirm Password*",width=20,font=("Times New Roman bold", 15),fg="magenta4")
label_cpwd.place(x=660,y=540)
#Create Entry Widget for confirm password
entry_cpwd= Entry(root, show="*",bg="snow",font=("Times New Roman", 15),highlightthickness="1",
                        highlightbackground="magenta4",highlightcolor="magenta4")
entry_cpwd.place(x=700,y=570,width=400,height=30)

check = IntVar()
checkButton = Checkbutton(root, text='I Agree All The Terms & Conditions', variable=check, onvalue=1,
                          offvalue=0, font=('times new roman', 10,"bold"), bg='white')
checkButton.place(x=700, y=600)

#==========================================================Buttons================================================================

Button_Register=Button(root, text='Register',font=("Times New Roman",15),width=20,bg='purple4',fg='white',
                            cursor="hand2",command=register).place(x=1000,y=610)

Button_back=Button(root, text='Back',font=("Times New Roman",15),width=5,bg='purple4',fg='white',
                            cursor="hand2",command=login_window).place(x=1170,y=100)


root.mainloop()





