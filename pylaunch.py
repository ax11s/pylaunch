import tkinter as tk

# create a Tkinter window
window = tk.Tk()



# define a function to be called when the button is clicked
def launch_command():
    command = file_input.get()
    labelitems = tk.Label(window, text="done" + command, bg="black", fg="white")
    labelitems.grid(row=1, column=1, padx=5, pady=5)


# create a label and setup arguments for the text input
window.geometry("300x500")
window.configure(background="black")
labelmain = tk.Label(window, text="Command:", bg="black", fg="white")

file_input = tk.Entry(window, width=22)

# create a button widget
buttonmain = tk.Button(window, text="Add file", width=8, height=1, bg="white", border=0)

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
for item in testlist:
    labellist = tk.Label(window, text=item, bg="black", fg="white")
    buttonlist = tk.Button(window, text="Run File", width=8, height=1, bg="white", border=0)
    labellist.grid(row=i, column=0, padx=0, pady=5)
    buttonlist.grid(row=i, column=2, padx=0, pady=5)
    i = i + 1




# start the Tkinter event loop
window.mainloop()