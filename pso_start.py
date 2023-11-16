"""Module that provide a simple UI to set the simulation variables"""
import tkinter as tk
from UI import run_pso

# selected_value_1 = ""
# selected_value_2 = ""
# selected_value_3 = ""
def run_pso_sim():
    """
        Function that closes the actual window and call for the PSO UI
    """
    selected_value_1= iterations.get()
    selected_value_2= size.get()
    selected_value_3= drones.get()
    root.destroy()
    run_pso(int(selected_value_1), int(selected_value_2), int(selected_value_3))

# Create the main window
root = tk.Tk()
root.title("Swarm Intelligence")
root.geometry("150x200")

#Entry for Iterations
text_dron = tk.Label(root, text="Iterations: ")
text_dron.grid(column=1, row=1)
iterations = tk.Entry(root)
iterations.grid(column=1, row=2)

#Entry for Map Size
text_map = tk.Label(root, text="Map size: ")
text_map.grid(column=1, row=3)
size = tk.Entry(root)
size.grid(column=1, row=4)

#Entry for Dron Amuount
text_iterations = tk.Label(root, text="Dron Amount: ")
text_iterations.grid(column=1, row=5)
drones = tk.Entry(root)
drones.grid(column=1, row=6)

#Button to start the simualtion
get_values_button = tk.Button(root, text="Run", command=run_pso_sim)
get_values_button.grid(column=1, row=7)

# Start the Tkinter main loop
root.mainloop()