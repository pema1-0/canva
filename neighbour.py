import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Build My House")
window.geometry("600x400")

# Title
title = tk.Label(
    window,
    text="My Neighbourhood",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

# Area where the houses will be shown
area = tk.Frame(window, width=500, height=220, bg="lightgreen")
area.pack(pady=10)

# Friend's existing house
friend_house = tk.Label(
    area,
    text="🏠\nFriend's House",
    font=("Arial", 14),
    bg="lightyellow",
    padx=20,
    pady=20
)
friend_house.place(x=280, y=60)


# Function to build my house
def build_house():
    my_house = tk.Label(
        area,
        text="🏠\nMy House",
        font=("Arial", 14),
        bg="lightblue",
        padx=20,
        pady=20
    )
    
    # Place my house near my friend's house
    my_house.place(x=100, y=60)


# Button
build_button = tk.Button(
    window,
    text="Build My House",
    font=("Arial", 12),
    command=build_house
)
build_button.pack(pady=15)

# Run the program
window.mainloop()