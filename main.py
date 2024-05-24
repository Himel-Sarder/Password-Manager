from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#ffe4e1")

canvas = Canvas(height=200, width=200, bg="#ffe4e1", highlightthickness=0)
logo_img = PhotoImage(file="logo2.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
font_name = "Arial"
website_label = Label(text="Website:", bg="#ffe4e1", font=(font_name, 12, "bold"))
website_label.grid(row=1, column=0, pady=5)
email_label = Label(text="Email/Username:", bg="#ffe4e1", font=(font_name, 12, "bold"))
email_label.grid(row=2, column=0, pady=5)
password_label = Label(text="Password:", bg="#ffe4e1", font=(font_name, 12, "bold"))
password_label.grid(row=3, column=0, pady=5)
developer_label = Label(text="Developed by: Himel Sarder\nCopyright ©2024", bg="#ffe4e1", fg="#666666", font=(font_name, 10))
developer_label.grid(row=5, column=1, pady=5)

# Entries
entry_bg_color = "#ffffff"
website_entry = Entry(width=35, bg=entry_bg_color, highlightthickness=0)
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()
email_entry = Entry(width=35, bg=entry_bg_color, highlightthickness=0)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, "info.himelcse@gmail.com")
password_entry = Entry(width=21, bg=entry_bg_color, highlightthickness=0)
password_entry.grid(row=3, column=1)

# Buttons
button_bg_color = "#e7305b"
button_fg_color = "#ffffff"
generate_password_button = Button(text="Generate Password", command=generate_password, bg=button_bg_color, fg=button_fg_color, highlightthickness=0)
generate_password_button.grid(row=3, column=2, padx=(5, 0))
add_button = Button(text="Add", width=50, command=save, bg=button_bg_color, fg=button_fg_color, highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=10, pady=3)

window.mainloop()
