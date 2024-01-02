from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

FONT = ("Calibre", 8, "bold")
RED = "#7D0A0A"
LIGHT_YELLOW = "#F3EDC8"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    """Generates a random complex password with 8 to 10 letters, 2 to 4 symbols and 2 to 4 numbers. Fills the password
    entry automatically and copy it to clipboard."""
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    generated_pass = []
    generated_pass += [choice(letters) for _ in range(randint(8, 10))]
    generated_pass += [choice(symbols) for _ in range(randint(2, 4))]
    generated_pass += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(generated_pass)
    new_password = "".join(generated_pass)

    # Clear and populate password entry field with generated password
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)
    # Copy the new password to clipboard
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def default_interface():
    """Clears all the entries and focus on website entry field"""
    website_entry.delete(0, END)
    # username_entry.delete(0, username_entry.get().find("@"))
    password_entry.delete(0, END)
    website_entry.focus()


def save_information():
    """Saves all the entries data into a local file, show warning if any field is left empty and show ok/cancel popup
    for user to double-check the data before it is saved"""
    # Get the text from all entries
    website_text = website_entry.get()
    username_text = username_entry.get()
    password_text = password_entry.get()
    new_data = {
        website_text: {
            "email": username_text,
            "password": password_text
        }
    }
    if not bool(website_text) or not bool(username_text) or not bool(password_text):
        messagebox.showwarning("Oops...", "Please don't leave any fields empty!")
    else:
        is_answer_ok = messagebox.askokcancel(title=website_text, message=f"These are the details entered: \n\n"
                                                                          f"Email: {username_text}\n"
                                                                          f"Password: {password_text} \n\n"
                                                                          f"Is it ok to save?")

        if is_answer_ok:
            # Dump the new data into local json file
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # Creates and write new data
                    json.dump(new_data, data_file)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                default_interface()


# ---------------------------- UI SETUP ----------------------
# --------- #
# Window settings
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
window.iconbitmap("lock.ico")

# Canvas with picture
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=0, row=0, columnspan=3)

# Labels
website_label = Label(text="Website:", bg="white", font=FONT, fg=RED)
website_label.grid(column=0, row=1)
username_label = Label(text="Email / Username:", bg="white", font=FONT, fg=RED)
username_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white", font=FONT, fg=RED)
password_label.grid(column=0, row=3)

empty_label = Label(bg="white", fg="white")
empty_label.grid(column=0, row=4, columnspan=4)

# Entries
website_entry = Entry(width=52, highlightthickness=1, border=1, font=FONT)
website_entry.grid(column=1, row=1, columnspan=2)
username_entry = Entry(width=52, highlightthickness=1, border=1, font=FONT)
username_entry.insert(0, "@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=32, highlightthickness=1, border=1, font=FONT)
password_entry.grid(column=1, row=3)

# Buttons
gen_pass_button = Button(text="Generate Password", width=16, font=FONT, bg=LIGHT_YELLOW, highlightthickness=0,
                         border=1, fg=RED, command=password_generator)
gen_pass_button.grid(column=2, row=3)
add_button = Button(text="Add", width=45, font=FONT, bg=LIGHT_YELLOW, highlightthickness=0,
                    border=1, fg=RED, command=save_information)
add_button.grid(column=1, row=5, columnspan=2)

default_interface()

window.mainloop()
