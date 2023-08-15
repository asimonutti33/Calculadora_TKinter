import tkinter as tk

def iniciar_sesion():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()

    if usuario == "usuario1" and contrasena == "contrasena1":
        mensaje_label.config(text="Inicio de sesión exitoso")
    else:
        mensaje_label.config(text="Nombre de usuario o contraseña incorrectos")

root = tk.Tk()
root.title("Inicio de Sesión")

usuario_label = tk.Label(root, text="Nombre de Usuario")
usuario_entry = tk.Entry(root)

contrasena_label = tk.Label(root, text="Contraseña")
contrasena_entry = tk.Entry(root, show="*")

boton_iniciar_sesion = tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion)

mensaje_label = tk.Label(root, text="")

usuario_label.grid(row=0, column=0)
usuario_entry.grid(row=0, column=1)

contrasena_label.grid(row=1, column=0)
contrasena_entry.grid(row=1, column=1)

boton_iniciar_sesion.grid(row=2, column=0, columnspan=2)

mensaje_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
