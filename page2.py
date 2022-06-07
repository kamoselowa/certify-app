from tkinter import *

window = Tk()
window.title("Certify")
window.resizable(False, False)
window.geometry('700x500')
#window['bg'] = 'lightseagreen'

Title = Label(window,text="Register",  font='bold,arial 17')
Title.grid(row=2, column=5)
Title.place(relx=0.5, rely=0.1, anchor=CENTER)

username = Label(window,text='FirstName: ',  font='bold')
userEntry = Entry(window)

username.grid(row=3, column=1)
userEntry.grid(row=4, column=1)
username.place(relx=0.5, rely=0.2, anchor=CENTER)
userEntry.place(relx=0.7, rely=0.2, anchor=CENTER)

Lastname = Label(window,text='LastName: ',  font='bold')
lastEntry = Entry(window)

Lastname.grid(row=3, column=1)
lastEntry.grid(row=4, column=1)
Lastname.place(relx=0.5, rely=0.3, anchor=CENTER)
lastEntry.place(relx=0.7, rely=0.3, anchor=CENTER)

passWord = Label(window, text='Password: ', font='bold')
passEntry = Entry(window)

passWord.grid(row=3, column=1)
passEntry.grid(row=4, column=1)
passWord.place(relx=0.5, rely=0.4, anchor=CENTER)
passEntry.place(relx=0.7, rely=0.4, anchor=CENTER)

reEnter = Label(window, text='Re enter password: ', font='bold')
reEntry = Entry(window)

reEnter.grid(row=3, column=1)
reEntry.grid(row=4, column=1)
reEnter.place(relx=0.5, rely=0.5, anchor=CENTER)
reEntry.place(relx=0.7, rely=0.5, anchor=CENTER)

Email = Label(window, text='Email: ', font='bold')
emailEntry = Entry(window)

Email.grid(row=3, column=1)
emailEntry.grid(row=4, column=1)
Email.place(relx=0.5, rely=0.6, anchor=CENTER)
emailEntry.place(relx=0.7, rely=0.6, anchor=CENTER)


def my_command():
   reg_button.config(text= "Register")

#Import the image using PhotoImage function
click_btn= PhotoImage(file="Images/img1(2).jpg")

reg_button = Button(window, text="Register", font='bold', image=click_btn, command=my_command, borderwidth=0)
img_label= Label(image=click_btn)

reg_button.grid(row=3, column=1)
reg_button.place(relx=0.5, rely=0.7)

window.mainloop()