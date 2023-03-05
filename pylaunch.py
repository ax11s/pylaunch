import tkinter as tk

# create a Tkinter window
window = tk.Tk()

# define a function to be called when the button is clicked
def launch_command():
    command = entry.get()
    print("Launching command:", command)


# create a label for the text input
window.geometry("300x700")
label = tk.Label(window, text="Command:")

# create a text input widget
entry = tk.Entry(window)

# create a button to launch the command
button = tk.Button(window, text="Launch Command", command=launch_command)

# add the widgets to the window
label.pack()
entry.pack()
button.pack()

# start the Tkinter event loop
window.mainloop()
