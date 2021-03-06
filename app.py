import tkinter as tk
from tkinter import filedialog, Text
import os
import subprocess

#main
root = tk.Tk()
#create list
apps = []

#read in save.txt file
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        #gets text from document and saves as string
        tempApps = f.read()
        #splits file by commas
        tempApps = tempApps.split(',')
        #gets rid of empty spaces when window is closed
        apps = [x for x in tempApps if x.strip()]

def addApp():
    #clear frame
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir= "/", title= "Select File",
                                          filetypes = (("executables", "*.exe"),
                                                        ("all files", "*.*")))

    #add file to list
    apps.append(filename)
    print(filename)
    #iterate through list
    for app in apps:
        #print label to frame portion of UI
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    #iterate through list of apps and open them all
    for app in apps:
        #use subprocess to open app
        subprocess.run(["open", "-a", app])

canvas = tk.Canvas(root, height=700, width=700, bg="#33F9FF")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely = 0.1)

openFile = tk.Button(root, text = "Open File", padx = 10, pady = 5, fg="black",
                     bg="#33F9FF", command=addApp)
openFile.pack()

runApps = tk.Button(root, text = "Run Apps", padx = 10, pady = 5, fg="black",
                    bg="#33F9FF", command=runApps)
runApps.pack()

#show label from read in file
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

#serialize Apps
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
