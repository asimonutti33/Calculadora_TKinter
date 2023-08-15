import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.config(width=300, height=200)
# Crear caja de texto.
entry = ttk.Entry()
# Posicionarla en la ventana.
entry.place(x=50, y=50)
root.mainloop()