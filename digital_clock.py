import tkinter as tk
import time
import random
from PIL import Image, ImageTk  # Importing Pillow for image handling

# Step 1: Create the main window
root = tk.Tk()
root.title("Jagruthi's Cute Digital Clock")

# Apply a cute, girly style to the window
root.configure(bg="#FFEBF0")  # Light pink background color for the window
root.geometry("800x500")      # Set a larger size for a more spacious layout

# List of Taylor Swift quotes
quotes = [
    "Just be yourself, there is no one better.",
    "People haven’t always been there for me, but music always has.",
    "In a relationship, each person should support the other; they should lift each other up.",
    "No matter what happens in life, be good to people. Being good to people is a wonderful legacy to leave behind.",
    "You are not the opinion of someone who doesn’t know you.",
    "The words you stop yourself from saying are the ones that will haunt you the longest.",
    "I think fearless is having fears but jumping anyway.",
    "There’s a fire inside of you that can’t help but shine through."
]

# Step 2: Load, resize, and convert the bow and glitter images
# Replace with your bow and glitter image paths
bow_image = Image.open("bow.png")
bow_image = bow_image.resize((50, 50), Image.LANCZOS)  # Resize to 50x50 pixels
bow_photo = ImageTk.PhotoImage(bow_image)

glitter_image = Image.open("glitter.png")
glitter_image = glitter_image.resize((100, 100), Image.LANCZOS)  # Resize to 100x100 pixels
glitter_photo = ImageTk.PhotoImage(glitter_image)

# Step 3: Define the function to update the time
def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

# Step 4: Define a function to update the quote
def update_quote():
    quote = random.choice(quotes)
    quote_label.config(text=quote)
    quote_label.after(5000, update_quote)  # Update every 5000 milliseconds (5 seconds)

# Step 5: Create a label to display your name
name_label = tk.Label(
    root,
    text="Welcome to Jagruthi's Clock!",
    font=("Comic Sans MS", 20, "bold"),  # Use a playful font
    bg="#FFEBF0",                        # Match the background color
    fg="#FF69B4"                         # Hot pink text color
)
name_label.pack(pady=10)  # Add some padding at the top

# Step 6: Create a label to display the time with a cute style
clock_label = tk.Label(
    root,
    font=("Comic Sans MS", 60, "bold"),  # Playful and bold font
    bg="#FFEBF0",                        # Background color matching the window
    fg="#DB7093",                        # Pale violet red color for the text
    padx=20,                             # Padding around the text
    pady=20                              # Padding around the text
)
clock_label.pack(anchor='center')

# Step 7: Create a label to display Taylor Swift quotes
quote_label = tk.Label(
    root,
    font=("Comic Sans MS", 15, "italic"),  # Italic font for quotes
    bg="#FFEBF0",                          # Background color matching the window
    fg="#8A2BE2",                          # Blue violet color for the text
    wraplength=600,                        # Wrap text within 600 pixels
    justify="center"                       # Center-align the text
)
quote_label.pack(pady=20)

# Step 8: Add bow images to the corners
bow_label1 = tk.Label(root, image=bow_photo, bg="#FFEBF0")
bow_label1.place(x=20, y=20)  # Place the bow in the top-left corner

bow_label2 = tk.Label(root, image=bow_photo, bg="#FFEBF0")
bow_label2.place(x=740, y=20)  # Place the bow in the top-right corner

# Step 9: Add glitter images to enhance the look
glitter_label = tk.Label(root, image=glitter_photo, bg="#FFEBF0")
glitter_label.place(x=350, y=400)  # Place the glitter in the bottom center

# Step 10: Start the clock and quote update
update_time()
update_quote()

# Step 11: Run the application
root.mainloop()
