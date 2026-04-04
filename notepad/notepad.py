from tkinter import *
from tkinter import filedialog

# Create main window
root = Tk()
root.title("Notepad App")
root.geometry("600x400")

# Create text area
text_area = Text(root)
text_area.pack(expand=True, fill="both")

# Function to save file
def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    if file:
        with open(file, "w") as f:
            f.write(text_area.get("1.0", END))

# Save button
Button(root, text="Save", command=save_file).pack()

# Run app
root.mainloop()
