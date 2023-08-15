import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Componentes')
ventana.iconbitmap('icono.ico')

#Width es la cantidad de caracteres q ocupa la caja de texto
#entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*')
#Definimos una variable q podremos modificar posteriormente (set), leer(get)
#Etiqueta (label)
etiqueta1 = tk.Label(ventana, text='Aqui se mostrara el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)
entrada_var1 = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)
#state =tk.DISABLED deshabilita
entrada1.grid(row=0, column= 0)
#insert agrega un texto
#entrada1.insert(0, 'Introduce una cadena')
#entrada1.insert(tk.END, '.')
#entrada1.config(state='readonly')

def enviar():
    #Recuperamos la info a patir de la variable asocioada
    boton1.config(text=entrada_var1.get())
    #Modificacion utilizamos la variable de texto y el metodo set
    #entrada_var1.set('Cambio...')
    #Recuperamos la informacion
    print(entrada_var1.get())
    print(entrada1.get())
    #Modificamos el texto del label
    etiqueta1.config(text=entrada_var1.get())
    #Messagebox (cajas mensajes
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Mensaje informativo', mensaje1 + 'Informativo')
        #messagebox.showerror('Mensaje error', mensaje1 + 'Error')
        #messagebox.showwarning('Mensaje de alerta', mensaje1 + 'Alerta')

def salir():
    ventana.quit()
    ventana.destroy()
    print('Salimos...')
    sys.exit()


def crear_menu():
    #Configurar el menu principal
    menu_principal = Menu(ventana)
    #tearoff = False no separar el menu de la interface para evitar q se separe
    submenu_archivo = Menu(menu_principal, tearoff=False)
    #Agregamos una nueva opción al menu de archivo
    submenu_archivo.add_command(label='Nuevo')
    #Se puede agregar un separador
    submenu_archivo.add_separator()
    #Agregamos la opcion de salir
    submenu_archivo.add_command(label='Salir', command=salir)
    #Agregamos el submenu al menu principal
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
    submenu_ayuda = Menu(menu_principal, tearoff=0)
    #Agregamos una nueva opcion al submenu
    submenu_ayuda.add_command(label='Acerca de...')
    #Agegamos al menu principal el nuevo submenu
    menu_principal.add_cascade(menu = submenu_ayuda, label='Ayuda')
    #Mostrarmos el menu en la ventana principal
    ventana.config(menu=menu_principal)


#Creamos un boton
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

crear_menu()

ventana.mainloop()
