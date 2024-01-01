from tkinter import *
FONT = ("Calibre", 8, "bold")
RED = "#7D0A0A"
LIGHT_YELLOW = "#F3EDC8"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry.focus()
username_entry = Entry(width=52, highlightthickness=1, border=1, font=FONT)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=32, highlightthickness=1, border=1, font=FONT)
password_entry.grid(column=1, row=3)

# Buttons
gen_pass_button = Button(text="Generate Password", width=16, font=FONT, bg=LIGHT_YELLOW, highlightthickness=0,
                         border=1, fg=RED)
gen_pass_button.grid(column=2, row=3)
add_button = Button(text="Add", width=45, font=FONT, bg=LIGHT_YELLOW, highlightthickness=0,
                    border=1, fg=RED)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()
