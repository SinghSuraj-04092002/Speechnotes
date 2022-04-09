from cgitb import text
from tkinter import *
from turtle import color, left
from PIL import ImageTk, Image
from tkinter.messagebox import*
import mysql.connector 


#############################################################Fuctionality & Database#########################################################
def home_window():
    root.destroy
    import home


def forget_password():
    def reset():
        entry_cnum.delete(0, END)
        entry_newpwd.delete(0, END)
        entry_uname.delete(0, END)
        entry_pwd.delete(0, END)

    def reset_password():
        if entry_cnum.get() == '' or entry_newpwd.get() == '':
            showerror('Error', 'All Fields Are Required', parent=root2)
        else:
            try:
                con = mysql.connector.connect(host="localhost",user="root",password="",database='speechtotext')
                cur = con.cursor(buffered = True)
                cur.execute('select * from signup where cnum',
                            entry_cnum.get())
                row = cur.fetchone()
                if row == None:
                    showerror('Error', 'Contact Number is Incorrect ', parent=root2)

                else:
                    cur.execute('update signup set pwd=%s where cnum=%s', entry_newpwd.get(), entry_cnum.get())
                    con.commit()
                    con.close()
                    showinfo('Success', 'Password is reset, please login with new password', parent=root2)
                    reset()
                    root2.destroy()


            except Exception as e:
                showerror('Error', f"Error due to: {e}", parent=root)

    if entry_uname.get() == '':
        showerror('Error', 'Please enter the Username to reset your password', parent=root)
    else:
        try:
            con =  mysql.connector.connect(host="localhost",user="root",password="",database='speechtotext')
            cur = con.cursor()
            cur.execute('select * from signup where uname', entry_uname.get())
            row = cur.fetchone()
            if row != None:
                showerror('Error', "Invalid username", parent=root)
            else:
###################################New Window For Forgot PassWord####################################################
                con.close()
                root2 = Toplevel()
                root2.title('Forget Password')
                root2.geometry('470x560+400+60')
                root2.config(bg='white')
                root2.focus_force()
                root2.grab_set()
                forgetLabel = Label(root2, text='Forget', font=('times new roman', 22, 'bold'), fg='purple4', bg='white')
                forgetLabel.place(x=128, y=10)
                forgetpassLabel = Label(root2, text='Password', font=('times new roman', 22, 'bold'), fg='magenta4',
                                        bg='white')
                forgetpassLabel.place(x=225, y=10)

                passwordimage = PhotoImage(file='image\pass.png')
                forgetimageLabel = Label(root2, image=passwordimage, bg='white')
                forgetimageLabel.place(x=170, y=70)
               
                CnumLabel = Label(root2, text='Contact N0', font=('times new roman', 19, 'bold'), fg='magenta4',
                                          bg='white')
                CnumLabel.place(x=60, y=310)
                entry_cnum = Entry(root2, font=('times new roman', 19,), fg='black', width=30,
                                          bg='white')
                entry_cnum.place(x=60, y=350)

                newpassLabel = Label(root2, text='New Password', font=('times new roman', 19, 'bold'), fg='magenta4',
                                     bg='white')
                newpassLabel.place(x=60, y=400)
                entry_newpwd = Entry(root2, font=('times new roman', 19,), fg='black', width=30,
                                     bg='white')
                entry_newpwd.place(x=60, y=440)

                changepassbutton = Button(root2, text='Change Password', font=('arial', 17, 'bold'), bg='purple4',
                                          fg='white', cursor='hand2', activebackground='green',
                                          activeforeground='white',
                                          command=reset_password)
                changepassbutton.place(x=130, y=500)

                root2.mainloop()

        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)

def register_window():
    root.destroy()
    import Registration

## Signin and its Database ##
def signin():
    if entry_uname.get() == '' or entry_pwd.get() == '':
        showerror('Error', 'All Fields Are Required')

    else:
        try:
            con = mysql.connector.connect(host="localhost",user="root",password="",database='speechtotext')
            cur = con.cursor()
            cur.execute('select * from signup where uname=%s and pwd=%s', (entry_uname.get(), entry_pwd.get()))
            row = cur.fetchone()
            if row == None:
                showerror('error', 'Invalid Username or Password')


            else:
                root.destroy()
                import home


            con.close()
        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)

## Tkinter Window ##
root = Tk()

canvas= Canvas(root,width=1440,height=1024)
image=ImageTk.PhotoImage(Image.open("image\Desktop - 1.jpg"))
root.title('Speechnotes')
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

#==================================================================Frames==================================================

frame1 = Frame(root,bg = "snow",width=1150,height=600,relief=FLAT)
frame1.place(x=116, y=69)

frame2 = Frame(root,bg ="snow",width=350,height=600,relief=FLAT)
frame2.place(x=160, y=65)
# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("image\Rectangle 6.jpg"))
# Create a Label Widget to display the text or Image
label = Label(frame2, image = img)
label.pack()

frame3 = Frame(root,bg ="snow",width=289,height=81, relief=FLAT)
frame3.place(x=700, y=135)
label_frame = Label(frame3,fg="purple3",bg="snow",text = "Welcome Back!",font=("Times New Roman bold",40))
label_frame.pack()



#==============================================================labels and Textfields=================================================

label_uname = Label(root, bg="snow", text="Username",width=20,font=("Times New Roman bold", 15),fg="magenta4")
label_uname.place(x=620,y=259)
entry_uname = Entry(root,highlightthickness="1", bg="snow",font=("Times New Roman", 15),
                        highlightbackground="magenta4",highlightcolor="magenta4")
entry_uname.place(x=700,y=294,width=400,height=30)

label_pwd = Label(root, bg="snow", text="Password",width=20,font=("Times New Roman bold", 15),fg="magenta4")
label_pwd.place(x=620,y=330)

#Create Entry Widget for password
entry_pwd= Entry(root,highlightthickness="1", show="*",bg="snow",font=("Times New Roman", 15),
                        highlightbackground="magenta4",highlightcolor="magenta4")
entry_pwd.place(x=700,y=365,width=400,height=30)

#================================================================Buttons===============================================================

forgetbutton = Button(root, text='Forget Password?', font=('Times New Roman bold', 15,), bd=0, fg='purple4', bg='white',
                      cursor='hand2', command=forget_password,
                      activebackground='white', activeforeground='gray20')
forgetbutton.place(x=950, y=430)

Button_Login=Button(root, text='Login',font=("Times New Roman bold",20),width=10,bg='purple4',fg='white',
                        cursor="hand2", command=signin).place(x=700,y=420)

registerbutton = Button(root, text='New User? SignUp here', font=('Times New Roman bold', 15,), bd=0, fg='purple4', bg='white',
                      cursor='hand2', command=register_window,
                      activebackground='white', activeforeground='gray20')
registerbutton.place(x=1050, y=90)

root.mainloop()
