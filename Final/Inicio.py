import tkinter as tk
from tkinter import ttk
from UI import run_pso

selected_value_1 = ""
selected_value_2 = ""
selected_value_3 = ""
selected_value_4 = ""

def close_window():
    root.destroy()
    run_pso(int(selected_value_1), int(selected_value_3), int(selected_value_2))


# Create the main application window
root = tk.Tk()
root.title("Swarm Intelligence")
root.geometry("200x200")

text_dron = tk.Label(root, text="Dron amount: ")
text_dron.grid(column=0, row=1)

text_map = tk.Label(root, text="Map size: ")
text_map.grid(column=0, row=3)

text_iterations = tk.Label(root, text="Iterations: ")
text_iterations.grid(column=0, row=5)

text_alg = tk.Label(root, text="Algorithm: ")
text_alg.grid(column=0, row=7)

# Create a list of options for each dropdown
options_1 = ["10", "25", "50"]
options_2 = ["50", "100", "150"]
options_3 = ["100", "500", "1000"]
options_4 = ["PSO", "Cukoo"]

# Create StringVars to store the selected options
selected_option_1 = tk.StringVar()
selected_option_2 = tk.StringVar()
selected_option_3 = tk.StringVar()
selected_option_4 = tk.StringVar()

# Create the first Combobox (Dropdown) widget
dropdown_1 = ttk.Combobox(root, textvariable=selected_option_1, values=options_1)
dropdown_1.grid(column=0, row=2)

# Create the second Combobox (Dropdown) widget
dropdown_2 = ttk.Combobox(root, textvariable=selected_option_2, values=options_2)
dropdown_2.grid(column=0, row=4)

# Create the third Combobox (Dropdown) widget
dropdown_3 = ttk.Combobox(root, textvariable=selected_option_3, values=options_3)
dropdown_3.grid(column=0, row=6)

# Create the fourth Combobox (Dropdown) widget
dropdown_4 = ttk.Combobox(root, textvariable=selected_option_4, values=options_4)
dropdown_4.grid(column=0, row=8)

# Function to be called when an option is selected
def on_select(event):
    global selected_value_1 
    global selected_value_2 
    global selected_value_3 
    global selected_value_4

    selected_value_1 = selected_option_1.get()
    selected_value_2 = selected_option_2.get()
    selected_value_3 = selected_option_3.get()
    selected_value_4 = selected_option_4.get()

    print("Selected Option 1:", selected_value_1)
    print("Selected Option 2:", selected_value_2)
    print("Selected Option 3:", selected_value_3)
    print("Selected Option 3:", selected_value_4)

# Bind the function to the Combobox event for all three dropdowns
dropdown_1.bind("<<ComboboxSelected>>", on_select)
dropdown_2.bind("<<ComboboxSelected>>", on_select)
dropdown_3.bind("<<ComboboxSelected>>", on_select)
dropdown_4.bind("<<ComboboxSelected>>", on_select)

# Set initial selections for each dropdown
selected_option_1.set(options_1[0])
selected_option_2.set(options_2[0])
selected_option_3.set(options_3[0])

btn_close = tk.Button(root, text="Run", command=close_window)
btn_close.grid(column=0, row=9)

# Start the Tkinter main loop
root.mainloop()