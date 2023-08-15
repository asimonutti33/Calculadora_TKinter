import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

class ComponentesVentana(tk.Tk):
    def __init__(self):

        self.geometry('650x400+500+200')
        self.title('Componentes')
        self.iconbitmap('icono.ico')
        self._crear_tabs()

    def _crear_componentes_tabulador1(tabulador):
        # Agregar una etiqueta y un compponente de entrada
        etiqueta1 = ttk.Label(tabulador, text='Nombre')
        etiqueta1.grid(row=0, column=0, sticky=tk.E)
        entrada1 = ttk.Entry(tabulador, width=30)
        entrada1.grid(row=0, column=1, padx=5, pady=5)

        # Agregamos un boton
        def enviar():
            messagebox.showinfo('Mensaje', f'Nombre: {entrada1.get()}')

        boton1 = ttk.Button(tabulador, text='Enviar', command=enviar)
        boton1.grid(row=1, column=0, columnspan=2)

    def _crear_componentes_tabulador2(tabulador):
        contenido = 'Este es mi texto con el contenido'
        #Creamos el componente de scroll
        scroll = scrolledtext.ScrolledText(tabulador, width=50, height=10, wrap=tk.WORD)
        scroll.insert(tk.INSERT, contenido)
        #MOstramos el componente
        scroll.grid(row=0, column=0)

    def _crear_componentes_tabulador3(tabulador):
        #Creamos una lista usando data list comprehension
        datos = [x+1 for x in range(10)]
        combobox = ttk.Combobox(tabulador, width=15, values=datos)
        combobox.grid(row=0, column=0, padx=10, pady=10)
        #Seleccionamos un elemento x default a mostrar
        combobox.current(5)
        #Agregar un boton para saber q opcion selecciono un usuario
        def mostrar_valor():
            messagebox.showinfo('Valor seleccionado', f'Valor seleccionado: {combobox.get()}')
        boton1 = ttk.Button(tabulador, text='Mostrar valor seleccionado', command=mostrar_valor)
        boton1.grid(row=0, column=1)

    def _crear_componentes_tabulador4(tabulador):
        imagen = tk.PhotoImage(file= 'python-logo.png')
        def mostrar_titulo():
            messagebox.showinfo('Mas info de la imagen', f'Nombre imagen: {imagen.cget("file")}')
        boton_imagen = ttk.Button(tabulador, image=imagen, command=mostrar_titulo)
        boton_imagen.grid(row=0, column=0)

    def _crear_componentes_tabulador5(tabulador):
        #Creamos el componente de barra de progreso
        barra_progreso = ttk.Progressbar(tabulador, orient='horizontal', length=550)
        barra_progreso.grid(row=0, column=0, pady=10, padx=10, columnspan=4)
        #Botones para controlar los eventos de una barra de progreso
        #Metodo para contorlar los eventos de la barra de progreso
        def ejecutar_barra():
            barra_progreso['maximum'] = 100
            for valor in range(101):
                #Mandamos a esperar un poco antes de continuar antes de continuar con la ejecucion de la barra
                sleep(0.05)
                #Incrementamos nuestra barra de progreso
                barra_progreso['value'] = valor
                #Actualizamos nuestra barra progreso
                barra_progreso.update()
            barra_progreso['value'] = 0

        boton_inicio = ttk.Button(tabulador, text='Ejecutar Barra de Progreso', command=ejecutar_barra)
        boton_inicio.grid(row=1, column=0)
        def ejecutar_ciclo():
            barra_progreso.start()
        boton_ciclo = ttk.Button(tabulador, text='Ejecutar ciclo', command=ejecutar_ciclo)
        boton_ciclo.grid(row=1, column=1)
        def detener():
            barra_progreso.stop()
        boton_detener = ttk.Button(tabulador, text='Detener ejecución', command=detener)
        boton_detener.grid(row=1, column=2)
        def detener_despues():
            esperar_ms = 1000
            ventana.after(esperar_ms, barra_progreso.stop())
        boton_despues = ttk.Button(tabulador, text='Detener ejecución', command=detener_despues)
        boton_despues.grid(row=1, column=3)

    def crear_tabs():
        #Creamos un tab control, para ellos usamos la clase de notebook
        control_tabulador = ttk.Notebook(ventana)


        #Agregamos un marco(frame) para agregar dentro del tab y organizar
        tabulador1 = ttk.Frame(control_tabulador)
        #Agregamos el tabulador al control de tabuladores
        control_tabulador.add(tabulador1, text='Tabulador1')
        #Mostramos el tabulador
        control_tabulador.pack(fill='both')
        #Creamos los componentes del tabulador 1
        crear_componentes_tabulador1(tabulador1)

        #Creamos un 2do tabulador:
        tabulador2 = ttk.Labelframe(control_tabulador, text='Contenido')
        control_tabulador.add(tabulador2, text='Tabulador 2')
        #Creamos los componentes del 2do tab
        crear_componentes_tabulador2(tabulador2)
        #Creamos un 3er tab
        tabulador3 = ttk.Frame(control_tabulador)
        control_tabulador.add(tabulador3, text='Tabulador3')
        #Creamos los componentes del 3er tab
        crear_componentes_tabulador3(tabulador3)
        #Crear un cuarto tabulador
        tabulador4 = ttk.Labelframe(control_tabulador, text='Imagen')
        control_tabulador.add(tabulador4, text='Tabulador 4')
        #Creamos los componentes del cuarto tabulador
        crear_componentes_tabulador4(tabulador4)
        #Se crea el 5to tabulador
        tabulador5 = ttk.Labelframe(control_tabulador)
        control_tabulador.add(tabulador5, text='Tabulador 5')
        #Creamos los componentes del quinto tab
        crear_componentes_tabulador5(tabulador5)



ventana.mainloop()