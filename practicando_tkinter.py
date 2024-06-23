# import tkinter as tk

# def saludar():
#     print("¡Hola, mundo!")

# # Crear la ventana principal
# ventana = tk.Tk()
# ventana.title("Mi primera aplicación con Tkinter")

# # Configurar la ventana en pantalla completa
# ventana.attributes('-fullscreen', True)
# ventana.configure(bg='#2A2A2A')

# # Crear un botón
# boton = tk.Button(ventana, text="Saludar", command=saludar)
# boton.pack()

# ventana.bind("<Escape>", lambda event: ventana.attributes("-fullscreen", False))


# # Ejecutar el bucle principal de eventos
# ventana.mainloop()


# # -------------------------------
# import tkinter as tk

# class Aplicacion:
#     def __init__(self, ventana):
#         self.ventana = ventana
#         self.ventana.title("Animación en Tkinter")
        
#         self.mensaje = "Cargando"
#         self.label = tk.Label(ventana, text=self.mensaje)
#         self.label.pack()
        
#         self.animar_mensaje(0)

#     def animar_mensaje(self, contador):
#         puntos = "." * (contador % 6)  # Modifica el número 6 para cambiar la cantidad de puntos
#         self.label.config(text=f"{self.mensaje}{puntos}")
#         self.ventana.after(500, self.animar_mensaje, contador+1)  # Actualiza cada 500ms

# ventana = tk.Tk()
# app = Aplicacion(ventana)
# ventana.mainloop()

