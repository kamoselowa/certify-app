from msilib.schema import CheckBox
from tkinter import *

from numpy import column_stack

window = Tk()
window.title("Certify")
window.resizable(False, False)
window.geometry('500x500')


#Labels
main_label = Label(window,text="Welcome to the certify app \nDo you have an account?",  font='bold,arial')
username = Label(window,text='UserName: ')
userEntry = Entry(window)
password = Label(window, text='Password: ')
passEntry = Entry(window)
#register_label = Label(window,text="If you don't have an account please Register")

def next_page():
    window.destroy()
    import page2        

def prev_page():
    window.destroy()
    import certify
    
Label(window, text="If you don't have an account please Register").grid(row=4, column=0)
Button(window, text='HERE', command=next_page).grid(row=4, column=1)

#Buttons
login_button = Button(window, text="Login")
login_button = Button(text='Login')
#register_button = Button(window, text='HERE',)

main_label.grid(row=0, column=0)
username.grid(row=1, column=0) 
userEntry.grid(row=1, column=1)
password.grid(row=2, column=0)
passEntry.grid(row=2, column=1)
login_button.grid(row=3, column=1)
#next_page.grid(fill=X,expand=True,row=4, column=0, command=True)
#next_page.grid( row=4, column=1, command=next_page)

window.mainloop()