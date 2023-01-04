from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    number_of_letters = random.randint(8, 10)
    number_of_symbols = random.randint(2, 4)
    number_of_numbers = random.randint(2, 4)

    password_list = []

    for char in range(number_of_letters):
      password_list.append(random.choice(letters))

    for char in range(number_of_symbols):
      password_list += random.choice(symbols)

    for char in range(number_of_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    # print(f"Your password is: {password}")
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="oops",message="Dont leabe any fields empty")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details enteres:\nEmail:{email}"
        f"\nPassword:{password}\nIs it okay to save ")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website}|{email}|{password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Mypass")
window.config(padx=40,pady=50)


canvas = Canvas(width=200,height=200,)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)


website_label = Label(text="Website")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2,column=0)
password_label = Label(text="Password")
password_label.grid(row=3,column=0)


website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
email_entry = Entry(width=35)
email_entry.insert(0,"mummaneni.nikhilgmail.com")
email_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=19)
password_entry.grid(row=3,column=1)


button=Button(text="Generate Pasword",command=generate_password)
button.grid(row=3,column=2)
button = Button(text="Add",width=30,command=save)
button.grid(row=4,column=1,columnspan=2)

window.mainloop()