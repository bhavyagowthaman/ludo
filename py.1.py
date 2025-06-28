Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import tkinter as tk
... import random
... 
... # Main window
... root = tk.Tk()
... root.title("Ludo Game - Project Presentation")
... root.geometry("600x700")
... root.configure(bg="white")
... 
... # Canvas to draw board
... canvas = tk.Canvas(root, width=600, height=600, bg='white')
... canvas.pack()
... 
... # Draw simplified Ludo Board
... def draw_board():
...     canvas.create_rectangle(0, 0, 600, 600, fill='white')
...     canvas.create_rectangle(0, 0, 200, 200, fill='green')   # Green base
...     canvas.create_rectangle(400, 0, 600, 200, fill='red')   # Red base
...     canvas.create_rectangle(0, 400, 200, 600, fill='yellow') # Yellow base
...     canvas.create_rectangle(400, 400, 600, 600, fill='blue') # Blue base
...     canvas.create_rectangle(200, 200, 400, 400, fill='white') # Center
... 
...     canvas.create_text(300, 300, text="LUDO", font=('Arial', 30, 'bold'), fill="black")
... 
... draw_board()
... 
... # Dice label
... dice_label = tk.Label(root, text="Roll the Dice", font=('Arial', 20), bg="white")
... dice_label.pack(pady=20)
... 
... # Function to roll dice
... def roll_dice():
...     dice_value = random.randint(1, 6)
...     dice_label.config(text=f"Dice Rolled: {dice_value}")
... 
... # Roll Dice Button
... roll_button = tk.Button(root, text="Roll Dice 🎲", font=('Arial', 16), command=roll_dice)
... roll_button.pack()
... 
... # Exit Button
... exit_button = tk.Button(root, text="Exit", font=('Arial', 14), bg='red', fg='white', command=root.quit)
... exit_button.pack(pady=10)
... 
