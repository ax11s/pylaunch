import tkinter as tk

# create a Tkinter window
window = tk.Tk()

# define a function to be called when the button is clicked
def launch_command():
    command = text_input.get()
    print("Launching command:", command)


# create a label and setup arguments for the text input
window.geometry("300x500")
window.configure(background="black")
label = tk.Label(window, text="Command:", bg="black", fg="white")

text_input = tk.Entry(window, width=22)

# create a button widget
button = tk.Button(window, text="Add file", width=8, height=1, bg="black", border=0)

# use the grid() method to position the widgets in a grid
label.grid(row=0, column=0, padx=5, pady=5)
text_input.grid(row=0, column=1, padx=5, pady=5)
button.grid(row=0, column=2, padx=5, pady=5)

# start the Tkinter event loop
window.mainloop()