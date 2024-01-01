from tkinter import *
FONT = ("Calibre", 8, "bold")
RED = "#7D0A0A"
LIGHT_YELLOW = "#F3EDC8"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def default_interface():
    """Clears all the entries and focus on website entry field"""
    website_entry.delete(0, END)
    username_entry.delete(0, username_entry.get().find("@"))
    password_entry.delete(0, END)
    website_entry.focus()


def save_information():
    """Saves all the entries data into a local file"""
    # Get the text from all entries
    website_text = website_entry.get()
    username_text = username_entry.get()
    password_text = password_entry.get()
    # Append the data into a local file
    with open("data.txt", "a") as data_file:
        data_file.write(f"{website_text} | {username_text} | {password_text}\n")
    default_interface()


# ---------------------------- UI SETUP ------------------------------- #
# Window settings
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

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
                         border=1, fg=RED)
gen_pass_button.grid(column=2, row=3)
add_button = Button(text="Add", width=45, font=FONT, bg=LIGHT_YELLOW, highlightthickness=0,
                    border=1, fg=RED, command=save_information)
add_button.grid(column=1, row=5, columnspan=2)

default_interface()

window.mainloop()
