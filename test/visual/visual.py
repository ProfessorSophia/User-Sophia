
#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox

# Create a function to show the pop-up
def show_popup():
    # Create a message box with a title and message
    messagebox.showinfo("Hello!", "This is a pop-up message!")

# Create the main window (it will not be shown)
root = tk.Tk()
root.withdraw()  # Hide the main window

# Call the function to show the pop-up
show_popup()

# Run the application
root.mainloop()
