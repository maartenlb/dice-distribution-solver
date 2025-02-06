import tkinter as tk
from tkinter import ttk
import ast
from dice_math import find_optimal_dice

def submit():
    mean = mean_var.get()
    std_dev_input = std_var.get()
    std_dev = float(std_dev_input) if std_dev_input else None
    selected_dice = [int(dice[1:]) for dice, var in dice_vars.items() if var.get()]
    custom_dice_input = custom_dice_var.get()
    if custom_dice_input:
        try:
            custom_dice = ast.literal_eval(custom_dice_input)
            if isinstance(custom_dice, list) and all(isinstance(i, int) for i in custom_dice):
                selected_dice.extend(custom_dice)
            else:
                raise ValueError
        except (ValueError, SyntaxError):
            result_label.config(text="Invalid custom dice list. Please enter a list of integers.")
            return

    # Call find_optimal_dice function
    top_matches = find_optimal_dice(mean, std_dev, selected_dice)

    # Display the results
    if top_matches:
        result_text = "\nTop Matches:\n"
        for i, (distance, num_dice, state) in enumerate(top_matches, 1):
            result_text += f"Match {i}: {state}, Distance={distance:.2f}, Num Dice={num_dice}\n"
        result_label.config(text=result_text)
    else:
        result_label.config(text="No matches found.")

root = tk.Tk()
root.title("Optimal Dice Distribution Finder")

# Mean input
tk.Label(root, text="Mean:").grid(row=0, column=0, sticky="w")
mean_var = tk.DoubleVar()
tk.Entry(root, textvariable=mean_var).grid(row=0, column=1)

# Standard deviation input
tk.Label(root, text="Standard Deviation (leave blank for no STD):").grid(row=1, column=0, sticky="w")
std_var = tk.StringVar()
tk.Entry(root, textvariable=std_var).grid(row=1, column=1)

# Dice selection
tk.Label(root, text="Select Dice:").grid(row=2, column=0, sticky="w")
dice_types = ['d2', 'd4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']
dice_vars = {}
for i, dice in enumerate(dice_types):
    var = tk.BooleanVar(value=(dice in ['d6', 'd20']))  # Default select d6 and d20
    tk.Checkbutton(root, text=dice, variable=var).grid(row=3 + i // 4, column=i % 4, sticky="w")
    dice_vars[dice] = var

# Custom dice input
tk.Label(root, text="Custom Dice (e.g., [3, 5, 7]):").grid(row=5, column=0, sticky="w")
custom_dice_var = tk.StringVar()
tk.Entry(root, textvariable=custom_dice_var).grid(row=5, column=1)

# Submit button
tk.Button(root, text="Submit", command=submit).grid(row=6, column=0, columnspan=2)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2)

root.mainloop()