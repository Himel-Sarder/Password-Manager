from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#FCC981")

canvas = Canvas(height=200, width=200, bg="#FCC981", highlightthickness=0)
logo_img = PhotoImage(file="logo3.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
font_name = "Arial"
website_label = Label(text="Website:", bg="#FCC981", font=(font_name, 12, "bold"))
website_label.grid(row=1, column=0, pady=5)
email_label = Label(text="Email/Username:", bg="#FCC981", font=(font_name, 12, "bold"))
email_label.grid(row=2, column=0, pady=5)
password_label = Label(text="Password:", bg="#FCC981", font=(font_name, 12, "bold"))
password_label.grid(row=3, column=0, pady=5)
developer_label = Label(text="Developed by: Himel Sarder\nCopyright ©2024", bg="#FCC981", fg="#666666", font=(font_name, 10))
developer_label.grid(row=5, column=1, pady=5)

# Entries
entry_bg_color = "#ffffff"
entry_font = (font_name, 12)
website_entry = Entry(width=21, bg=entry_bg_color, highlightthickness=0, font=entry_font)
website_entry.grid(row=1, column=1, pady=5)
website_entry.focus()
email_entry = Entry(width=35, bg=entry_bg_color, highlightthickness=0, font=entry_font)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, "info.himelcse@gmail.com")
password_entry = Entry(width=21, bg=entry_bg_color, highlightthickness=0, font=entry_font)
password_entry.grid(row=3, column=1, pady=5)

# Buttons
button_bg_color = "#FA4616"
button_fg_color = "#ffffff"
button_font = (font_name, 12, "bold")
search_button = Button(text="Search", command=find_password, bg=button_bg_color, fg=button_fg_color, highlightthickness=0, font=button_font)
search_button.grid(row=1, column=2, padx=(5, 0))
generate_password_button = Button(text="Generate Password", command=generate_password, bg=button_bg_color, fg=button_fg_color, highlightthickness=0, font=button_font)
generate_password_button.grid(row=3, column=2, padx=(5, 0))
add_button = Button(text="Add", width=36, command=save, bg=button_bg_color, fg=button_fg_color, highlightthickness=0, font=button_font)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
