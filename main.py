from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json


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
    new_data={
        website:{
            "email":email,
            "password":password 

        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Empty details",message="website and password feild can't left empty.")
    else:
        try:
            with open("password_manager/data.json","r")as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
                with open("password_manager/data.json","w")as data_file:
                     json.dump(new_data,data_file,indent=4)

        else:
            data.update(new_data)

            with open("password_manager/data.json","w")as data_file:
                json.dump(data,data_file,indent=4)

        finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)


def find_password():
    website=website_entry.get()
    try:
        with open("password_manager/data.json")as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error 69",message="No Data File Found.")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")  
        else:
            messagebox.showinfo(title="Error 96",message=f"No Details Found for {website}")
    
        


    






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
password_entry=Entry(width=25,font=("Courier",9 ))
password_entry.grid(row=3,column=1,columnspan=1,)
generate_button=Button(text="Generate",command=generate_password,font=("Courier",9 ))
generate_button.grid(column=2,row=3)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)
search_button=Button(text="Search",width=8,command=find_password)
search_button.grid(column=2,row=1)





window.mainloop()