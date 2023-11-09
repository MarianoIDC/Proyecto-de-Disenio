import tkinter as tk

from UI import run_pso

selected_value_1 = ""
selected_value_2 = ""
selected_value_3 = ""
def close_window():
    selected_value_1= iterations.get()
    selected_value_2= size.get()
    selected_value_3= drones.get()
    root.destroy()
    run_pso(int(selected_value_1), int(selected_value_2), int(selected_value_3))

# def get_values():
#     global selected_value_1 
#     global selected_value_2 
#     global selected_value_3 

#     selected_value_1 
#     selected_value_2 
#     selected_value_3 

# Create the main window
root = tk.Tk()
root.title("Swarm Intelligence")
root.geometry("200x200")

text_dron = tk.Label(root, text="Iterations: ")
text_dron.grid(column=0, row=1)

text_map = tk.Label(root, text="Map size: ")
text_map.grid(column=0, row=3)

text_iterations = tk.Label(root, text="Dron Amount: ")
text_iterations.grid(column=0, row=5)

# Create Entry widgets
iterations = tk.Entry(root)
iterations.grid(column=0, row=2)
size = tk.Entry(root)
size.grid(column=0, row=4)
drones = tk.Entry(root)
drones.grid(column=0, row=6)

# Create a button to trigger value retrieval
get_values_button = tk.Button(root, text="Run", command=close_window)
get_values_button.grid(column=0, row=7)


# Start the Tkinter main loop
root.mainloop()