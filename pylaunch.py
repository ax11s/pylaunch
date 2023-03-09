import tkinter as tk
import os

# create a Tkinter window
window = tk.Tk()
filename = "config.txt"




with open(filename, "r") as f:
    lines = f.readlines()

linecount = sum(1 for line in lines)



# define a function to be called when the button is clicked
def getinput():
    with open(filename, "r") as f:
      lines = f.readlines()

    filepath = file_input.get()

    for line in lines:
        if line == "":
            lines[line] = filepath + "\n"

    with open(filename, "w") as file:
        file.writelines(lines)


# define a function to be called when the run button is clicked
def firescript(argument):
    line = lines[argument].strip()

    if line == "":
        print("no such file")
    else:       
        os.system("python3.10 " + "./pyfiles/" + line + ".py")



# create a label and setup arguments for the text input
window.geometry("300x500")
window.configure(background="black")
labelmain = tk.Label(window, text="Command:", bg="black", fg="white")

file_input = tk.Entry(window, width=22)

# create a button widget
buttonmain = tk.Button(window, text="Add file", width=8, height=1, bg="white", border=0, command=getinput)

# use the grid() method to position the widgets in a grid
labelmain.grid(row=0, column=0, padx=5, pady=5)
file_input.grid(row=0, column=1, padx=5, pady=5)
buttonmain.grid(row=0, column=2, padx=5, pady=5)

labelitems = tk.Label(window, text="", bg="black", fg="white")
labelitems.grid(row=1, column=1, padx=5, pady=5)

#get items form a file
i = 2
testlist = ["apple", "banana", "cherry"]
#display items
for argument in enumerate(lines):
    name = argument[1]
    labellist = tk.Label(window, text=name, bg="black", fg="white")
    buttonlist = tk.Button(window, text="Run File", width=8, height=1, bg="white", border=0, command=lambda arg=argument[0]: firescript(arg))
    labellist.grid(row=i, column=0, padx=0, pady=5)
    buttonlist.grid(row=i, column=2, padx=0, pady=5)
    i = i + 1





# start the Tkinter event loop
window.mainloop()