import tkinter as tk
from tkinter import filedialog, Text
import os


#main
root = tk.Tk()

def addApp():
    filename = filedialog.askopenfilename

canvas = tk.Canvas(root, height=700, width=700, bg="#33F9FF")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely = 0.1)

openFile = tk.Button(root, text = "Open File", padx = 10, pady = 5, fg="black", bg="#33F9FF", command="addApp")
openFile.pack()

runApps = tk.Button(root, text = "Run Apps", padx = 10, pady = 5, fg="black", bg="#33F9FF")
runApps.pack()

root.mainloop()
