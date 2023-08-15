import tkinter as tk
from tkinter import ttk, messagebox

class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()


        #ventana principal
        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('icono.ico')
        self.resizable(0,0)

        #Configuracion del grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self._crear_componentes()

    #Definir el metodo crear_componentes
    def _crear_componentes(self):

        #usuario
        usuario_etiqueta = ttk.Label(self, text='Usuario: ')
        usuario_etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.usuario_entrada = ttk.Entry(self)
        self.usuario_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        #Password
        password_etiqueta = ttk.Label(self, text='Password:')
        password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.password_entrada = ttk.Entry(self, show='*')
        self.password_entrada.grid(row=1, column=1, sticky=tk.W, pady=5, padx=5)


        #def login
        login_boton = ttk.Button(self, text='Login', command=_login)
        login_boton.grid(row=3, column=0, columnspan=2)

#Boton Login
def _login(self):
    messagebox.showinfo('Datos Login: ' ,
                        f'usuario: {self.usuario_entrada.get()}, password:{self.password_entrada.get()}')


#Ejecutar ventana
if __name__ == '__main__':
    login_ventana = LoginVentana()
    login_ventana.mainloop()
