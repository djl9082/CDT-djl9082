#djl9082@rit.edu
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Toplevel

def show_image_popup(image_path):
    #create window
    popup = Toplevel()
    popup.overrideredirect(True)  # Remove window borders and title bar


    # Load the image
    img = Image.open(image_path)
    img = img.resize((1920, 1080), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)

    #display the image
    label = tk.Label(popup, image=img)
    label.image = img
    label.pack()

    # Schedule the popup to close after 30 seconds
    popup.after(30000, popup.destroy)
    popup.bind("<c>", lambda e: popup.destroy()) #escape picture
    popup.bind("<Tab>",lambda e: popup.destroy())  # escape picture
    popup.bind("<Escape>", lambda e: popup.destroy())  # escape picture
def schedule_popup(image_path, interval=60000):
    # Show the image popup
    show_image_popup(image_path)
    # Reschedule to show the popup
    root.after(interval, schedule_popup, image_path, interval)


root = tk.Tk()
root.withdraw()
# Path to image
image_path = "C:/ProgramData/Microsoft/Diagnosis/cat.png"

# Start the cycle to show the image for 30 seconds, then wait 30 seconds before showing again
schedule_popup(image_path, 60000)

root.mainloop()
