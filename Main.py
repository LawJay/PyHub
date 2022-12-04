import tkinter
import customtkinter
from tkinter import filedialog as fd
from tkinter import *
from Sorter import sortDirectory



customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.title('Codemy.com - Dictionary')

root.geometry("620x470")

def dialog():
    path = folder_selected = fd.askdirectory()
    my_entry.delete(0,END)
    my_entry.insert(0,path)

def Sort():
    path = my_entry.get()
    if not path == "":
        sortDirectory(path)



my_labelframe = customtkinter.CTkFrame(root, corner_radius= 10)
my_labelframe.pack(pady=20)

my_entry = customtkinter.CTkEntry(my_labelframe, width=400,height=40,border_width=1,placeholder_text="Enter a Word",placeholder_text_color= "silver"
                                                                                                                                            )
my_entry.grid(row=0, column=0, padx=10, pady=10)

dialog_button = customtkinter.CTkButton(my_labelframe, text="Choose Path", command=dialog)
dialog_button.grid(row=0, column=1, padx=10)

my_button = customtkinter.CTkButton(my_labelframe, text="Clean", command=Sort)
my_button.grid(row=0, column=2, padx=10)

text_frame = customtkinter.CTkFrame(root, corner_radius= 10)
text_frame.pack(pady=10)

my_text = Text(text_frame, height=20, width=67, wrap=WORD, bd=0,bg="#292929",fg="silver")
my_text.pack(pady=10,padx=10)


root.mainloop()


