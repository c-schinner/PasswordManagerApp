from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
               'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '*', '+', '(', ')']

    password = []

    for i in range(random.randint(5, 7)):
        password.append(random.choice(letters))
    for i in range(random.randint(2, 4)):
        password.append(random.choice(numbers))
    for i in range(random.randint(2, 4)):
        password.append(random.choice(symbols))

    random.shuffle(password)
    new_password = "".join(password)

    generated_password.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button():
    website = website_input.get().title()
    email = username_input.get()
    password = generated_password.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="You have left some fields empty")

    else:
        try:
            with open("data.json", "r") as file:
                # Reading the data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            # Updating the old data with the new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving the updated data
                json.dump(data, file, indent=4)

        finally:
            website_input.delete(0, END)
            generated_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Our window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Our canvas setup with photo image
canvas = Canvas(width=200, height=200, highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# Our label setup with location setup
website_label = Label(window, text="website :", font=("Italic", 10, "bold"))
email_username_label = Label(window, text="email/username :", font=("Italic", 10, "bold"))
password_label = Label(window, text="password :", font=("Italic", 10, "bold"))

website_label.grid(column=0, row=1)
website_label.config(padx=5, pady=5)
email_username_label.grid(column=0, row=2)
email_username_label.config(padx=5, pady=5)
password_label.grid(column=0, row=3)
password_label.config(padx=5, pady=5)

website_input = Entry(width=24, font=("Courier", 10, "bold"))
website_input.grid(row=1, column=1)
website_input.focus()
username_input = Entry(width=40, font=("Courier", 10, "bold"))
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "YOUReMAIL@eMAIL.com")
generated_password = Entry(width=24, font=("Courier", 10, "bold"))
generated_password.grid(row=3, column=1)


def search_button():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="There is no such information on file.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            message = f"Email : {email}\nPassword : {password}"
            messagebox.showinfo(title="User Information", message=message)
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} in the database")


# Button layout with location setup
generate_password = Button(window, text="Generate Password", font=("Courier", 8, "bold"), command=gen_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=46, font=("Courier", 8, "bold"), command=add_button)
add_button.grid(row=4, column=1, columnspan=2)

search = Button(window, text="Search", width=17, font=("Courier", 8, "bold"), command=search_button)
search.grid(column=2, row=1)

window.mainloop()
