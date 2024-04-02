import customtkinter
import tkinter as tk
from tkinter import messagebox

#I mainly used CTk for the widgets, which is known to be more easier and more modern to use than the
# default tkinter widgets 

#Set appearance mode to system(my own color)
customtkinter.set_appearance_mode("dark")

#Set default color theme 
customtkinter.set_default_color_theme("blue")

#root is the main window
root = customtkinter.CTk()
root.title("Minou's app") #root.title is used to set the title of the window
#root.geometry is used to set the size of the window
root.geometry("500x350")

#frame is the container for the widgets. master = root means that the frame is inside the root window
frame = customtkinter.CTkFrame(master = root)
#frame.pack is used to display the frame. pack means to display the frame
frame.pack(pady = 20, padx = 60, fill= "both", expand = True)

#label is the text that will be displayed on the window, in this case it is "Login"
label = customtkinter.CTkLabel(master=frame, text="LOGIN", font=("Arial", 20))
#again, pack the label to display it
label.pack(pady = 12, padx = 10)

#if the user clicks the "Forgot password?" text, then the forgot_password_click function will be executed
def forgot_password_click(event=None):
    messagebox.showinfo("Forgot Password", "Please contact the administrator to reset your password")

#function where the login button will be linked
def login():
    username = entry1.get() #get the username from the entry1 field
    password = entry2.get() #get the password from the entry2 field
    
    #applied logic for the login
    if username == "admin" and password == "123": #if the username and password is admin, then print "Login Successful"
        messagebox.showinfo("Login Successful", "Welcome " + username + "!")
    else: #if the username and password is not admin, then print "Login Failed"
        messagebox.showerror("Login Failed", "Invalid Username or Password")

#entry1 is the first entry field where the user will enter the username, with the Username as the placeholder text
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
#again, pack the entry1 to display it
entry1.pack(pady = 12, padx = 10)

#same thig goes here, but instead with the password as the placeholder text, also show = "*" is used to hide the password
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady = 12, padx = 10)

#button is the login button, with the text "Login" and the command login, which is the function 
# that will be executed when the button is clicked
button = customtkinter.CTkButton(master=frame, text="Login", command=login)
#again, pack the button to display it
button.pack(pady = 12, padx = 10)

#checkbox is the remember me checkbox, with the text "Remember me"
checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(pady = 12, padx = 10)

forgot = customtkinter.CTkLabel(master=frame, text="Forgot password?", font=("Arial", 10))
forgot.pack(pady = 12, padx = 10)

#bind the forgot label to the forgot_password_click function
#Button-1 means the left mouse button
forgot.bind("<Button-1>", forgot_password_click)

#root.mainloop is for the window to keep running
root.mainloop()