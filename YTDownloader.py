from pytube import YouTube
from sys import argv
import tkinter
import os
import customtkinter


# mydir = '/Users/martinrichter/PycharmProjects/test'
myfile = 'YTDownloader.py'
# training_images_labels_path = os.path.join(mydir, myfile)

with open(myfile, 'r') as file:
    file =open("/Users/martinrichter/PycharmProjects/test/YTDownloader.py")



customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x400")

def login():
    print(entry1.get())
    newLink = entry1.get()


    # link = argv[1]
    # link = newLink
    yt = YouTube(newLink)

    print("Title: ", yt.title)

    print("View: ", yt.views)

    yd = yt.streams.get_highest_resolution()

    yd.download("/Users/martinrichter/Desktop/Ytvideo")

frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=app, text="Youtubedownloader")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=app, placeholder_text="Youtubelink einfügen")
entry1.pack(pady=12, padx=12)

button = customtkinter.CTkButton(master=app, text="Download", command=login)
button.pack(pady=12, padx=12)

#
# checkbox = customtkinter.CTkCheckBox(master=app, text="Test")
# checkbox.pack(pady=12, padx=12)

app.mainloop()