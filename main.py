from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[choice(letters) for _ in range(randint(8,10))]
    password_symbols=[choice(symbols) for _ in range(randint(2,4))]
    password_numbers=[choice(numbers) for _ in range(randint(2,4))]

    password_list=password_letters+password_numbers+password_symbols

    shuffle(password_list)
    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Empty details",message="website and password feild can't left empty.")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are details entered: \nEmail: {email} \nPassword: {password} \n Do you want to save?")

        if is_ok:
            with open("password_manager/data.txt","a")as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
    






# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
image=PhotoImage(file="password_manager/logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(column=1,row=0)
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
email_label=Label(text="Email:")
email_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

website_entry=Entry(width=40)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=40)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"krishnkapoor00@gmail.com",)
password_entry=Entry(width=26,font=("Courier",9 ))
password_entry.grid(row=3,column=1,columnspan=1,)
generate_button=Button(text="Generate Password",command=generate_password,font=("Courier",9 ))
generate_button.grid(column=2,row=3)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)





window.mainloop()