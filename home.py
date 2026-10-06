import tkinter as tk

root = tk.Tk()

root.title("My Home")

canvas = tk.Canvas(root, width=500, height=350, bg="lightblue")
canvas.pack()

# House body
canvas.create_rectangle(120, 150, 380, 300, fill="light green")

# Roof
canvas.create_polygon(90, 150, 250, 50, 410, 150, fill="brown")

# Door
canvas.create_rectangle(220, 210, 280, 300, fill="lightyellow")

# Left window
canvas.create_rectangle(150, 180, 200, 230, fill="lightblue")

# Right window
canvas.create_rectangle(300, 180, 350, 230, fill="lightblue")

# Ground
canvas.create_line(50, 300, 450, 300, width=4)

# Text
canvas.create_text(250, 325, text="My Home", font=("Arial", 20))

root.mainloop()