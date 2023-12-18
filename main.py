from tkinter import *
import pyperclip
import tkinter as tk
from tkinter import messagebox
import pandas as pd

from encryption import Encryption, SEED
from passgen import PasswordGen
from user import User

# Initialize User, PasswordGen, and Encryption instances
user = User()
passgen = PasswordGen()
encryption = Encryption(SEED)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # creating a container
        container = tk.Frame(self, padx=50, pady=50)
        self.geometry("250x400")
        container.grid(column=0, row=0)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (LoginPage, SignUpPage, MainPage):
            frame = F(container, self)

            # initializing frame of that object from
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        # Checking if user has passcode data
        self.show_frame(LoginPage if user.get_passcode() else SignUpPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def update_window_size(self, width, height):
        self.geometry(f"{width}x{height}")


class SignUpPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Labels
        self.logo_image = PhotoImage(file="assets/logo.png")
        self.panel = Label(self, image=self.logo_image, height=200, width=150)
        self.panel.grid(row=0, column=0)

        self.welcome_label = Label(self, text="Welcome First Time User", font=("Helvetica", 10, "bold"))
        self.welcome_label.grid(row=1, column=0)
        self.passcode_label = Label(self, text="Set up a passcode", font=("Helvetica", 10, "italic"))
        self.passcode_label.grid(row=2, column=0)

        # Entry
        self.passcode_entry = Entry(self, width=20)
        self.passcode_entry.grid(row=3, column=0)

        # Button
        self.passcode_signup_button = Button(self, text="Sign Up", width=12, fg="white", background="#D51396", font=("Helvetica", 12, "bold"), command=self.signup)
        self.passcode_signup_button.grid(row=4, column=0, pady=10)

    def signup(self):
        passcode = self.passcode_entry.get()
        if len(passcode) < 4:
            messagebox.showinfo(title="Passcode too short", message="Passcode must be at least 4 characters")
            return
        user.set_passcode(passcode)
        self.controller.show_frame(MainPage)
        self.controller.update_window_size(620, 480)

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Labels
        self.logo_image = PhotoImage(file="assets/logo.png")
        self.panel = Label(self, image=self.logo_image, height=200, width=150)
        self.panel.grid(row=0, column=0)

        self.welcome_label = Label(self, text="Welcome", font=("Helvetica", 15, "bold"))
        self.welcome_label.grid(row=1, column=0)
        self.passcode_label = Label(self, text="What is the passcode?", font=("Helvetica", 10, "italic"))
        self.passcode_label.grid(row=2, column=0)

        # Entry
        self.passcode_entry = Entry(self, width=20)
        self.passcode_entry.grid(row=3, column=0)

        # Button
        self.passcode_login_button = Button(self, text="Login",  width=12, fg="white", background="#D51396", font=("Helvetica", 12, "bold"), command=self.login)
        self.passcode_login_button.grid(row=4, column=0, pady=10)

    def login(self):
        password = self.passcode_entry.get()
        if user.login(password):
            self.controller.show_frame(MainPage)
            self.controller.update_window_size(620, 480)
        else:
            messagebox.showinfo(title="Wrong!", message="Wrong Passcode")


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.logo_image = PhotoImage(file="assets/logo.png")
        self.panel = Label(self, image=self.logo_image, height=200, width=150)
        self.panel.grid(row=0, column=2, columnspan=2)

        # Labels
        self.website_label = Label(self, text="Website:")
        self.website_label.grid(row=1, column=1)
        self.user_email_label = Label(self, text="Email/Username:")
        self.user_email_label.grid(row=2, column=1)
        self.password_label = Label(self, text="Password:")
        self.password_label.grid(row=3, column=1)

        # Entry
        self.website_entry = Entry(self, width=50)
        self.website_entry.focus()
        self.website_entry.grid(row=1, column=2, columnspan=2)
        self.user_email_entry = Entry(self, width=50)
        self.user_email_entry.insert(0, "@gmail.com")
        self.user_email_entry.grid(row=2, column=2, columnspan=2)
        self.password_entry = Entry(self, width=34)
        self.password_entry.grid(row=3, column=2)

        # Buttons
        self.pass_gen_button = Button(self, text="Gen. Password", width=12, fg="white", background="#D51396", font=("Helvetica", 12, "bold"), command=self.pass_generate)
        self.pass_gen_button.grid(row=3, column=3)


        self.add_pass_button = Button(self, text="Add", width=34, fg="white", background="#A81B98", font=("Helvetica", 12, "bold"), command=self.add_password)
        self.add_pass_button.grid(row=5, column=2, columnspan=2)

        self.view_pass_button = Button(self, text="View Passwords",fg="white", width=34, background="#812B9A", font=("Helvetica", 12, "bold"), command=self.view_passwords)
        self.view_pass_button.grid(row=6, column=2, columnspan=2, pady=10)

        self.update_pass_button = Button(self, text="Update Passwords", fg="white", background="#73309B", font=("Helvetica", 12, "bold"), width=34, command=self.update_password)
        self.update_pass_button.grid(row=7, column=2, columnspan=2)

    def add_password(self):
        website = self.website_entry.get()
        email = self.user_email_entry.get()
        password = self.password_entry.get()

        if len(website) == 0:
            messagebox.showinfo(title="Oops", message="Dont forget to include a website")
        elif len(password) == 0:
            messagebox.showinfo(title="Oops", message="Dont forget to generate or add a password")
        elif len(email.split("@")[0]) == 0:
            messagebox.showinfo(title="Oops", message="Dont forget to add your username/email")
        else:
            is_ok = messagebox.askokcancel(title=website,
                                           message=f"These are the details entered: \n Email: {email} \n Password: {password} \n Is it ok to save?")
            if is_ok:
                with open("application_data/password_data.txt", "a") as data_file:
                    # Encrypt the password before saving
                    encrypted_password = encryption.encrypt(password)
                    data_file.write(f"{website} | {email} | {encrypted_password}\n")
                    self.website_entry.delete(0, END)
                    self.user_email_entry.delete(0, END)
                    self.password_entry.delete(0, END)
            else:
                pass

    def pass_generate(self):
        password = passgen.generate_password()
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)
        # Copies password to clipboard
        pyperclip.copy(password)
        messagebox.showinfo(title="Password Generated", message="Password Copied to Clipboard")
        passgen.reset()

    def view_passwords(self):
        try:
            data = pd.read_csv("application_data/password_data.txt", sep=" | ", engine='python')

            # Define a function to decrypt a row
            def decrypt_column(column):
                # Decrypt the password in the row using your decryption method
                decrypted_password = encryption.decrypt(column["Password"], SEED)
                # Update the password in the row with the decrypted value
                column["Password"] = decrypted_password
                # Return the modified row
                return column

            # Apply the decrypt_row function to each row in the DataFrame
            decrypted_data = data.apply(decrypt_column, axis=1)

            # Show the information in a message box (excluding index and header)
            messagebox.showinfo(title="Passwords", message=decrypted_data.to_string(index=False, header=False))
        except pd.errors.EmptyDataError:
            # Show a message if the CSV file is empty
            messagebox.showinfo(title="Passwords", message="No data found.")

    def update_password(self):
        website = self.website_entry.get()
        new_password = self.password_entry.get()

        if len(website) == 0:
            messagebox.showinfo(title="Oops", message="Don't forget to include a website")
        elif len(new_password) == 0:
            messagebox.showinfo(title="Oops", message="Don't forget to generate or add a password")
        else:
            try:
                with open("application_data/password_data.txt", "r") as data_file:
                    lines = data_file.readlines()

                found_website = False

                with open("application_data/password_data.txt", "w") as data_file:
                    for line in lines:
                        if website in line:
                            _, _, existing_password = line.split(" | ")
                            data_file.write(
                                f"{website} | {self.user_email_entry.get()} | {encryption.encrypt(new_password)}\n")
                            found_website = True
                        else:
                            data_file.write(line)

                if found_website:
                    messagebox.showinfo(title="Success", message="Password updated successfully.")
                else:
                    messagebox.showinfo(title="Website Not Found", message=f"Website '{website}' not found.")
            except FileNotFoundError:
                messagebox.showinfo(title="File Not Found", message="No passwords.txt file found.")


# Driver Code
app = tkinterApp()
app.mainloop()
