#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# $ sudo add-apt-repository ppa:deadsnakes/ppa
# $ sudo apt-get update
# $ sudo apt-get install python3.8 python3-tk

import tkinter as tk
from tkinter import *
from tkinter import ttk, font
import getpass

class Hamming_interface(Tk):
    def __init__(self):
        super().__init__()
        self.raiz = self
        self.raiz.title("Graphic Hamming")
        self.set_raiz_elements(self.raiz)
        self.place_raiz_and_its_elements(self.raiz)

        self.banner_holder = ttk.Frame(self.raiz)
        self.set_banner(self.banner_holder)
        self.place_banner(self.banner_holder)
        self.login_holder = ttk.Frame(self.raiz, borderwidth=2,relief="raised", padding=(10, 10))
        self.set_login_elements(self.login_holder)
        self.place_login_holder_and_its_elements(self.login_holder)


    def set_raiz_elements(self, raiz):
        # en este caso no tiene nada para añadir
        pass
    def place_raiz_and_its_elements(self, raiz):
        # Para conseguir que la cuadricula y los widgets se
        # adapten al contenedor, si se amplia o reduce el tamaño
        # de la ventana, es necesario definir la opción 'sticky'.
        # Cuando un widget se ubica en el grid se coloca en el
        # centro de su celda o cuadro. Con 'sticky' se
        # establece el comportamiendo 'pegajoso' que tendrá el
        # widget dentro de su celda, cuando se modifique la
        # dimensión de la ventana. Para ello, se utilizan para
        # expresar sus valores los puntos cardinales: N (Norte),
        # S (Sur), (E) Este y (W) Oeste, que incluso se pueden
        # utilizar de forma combinada. El widget se quedará
        # 'pegado' a los lados de su celda en las direcciones
        # que se indiquen. cuando la ventana cambie de tamaño.
        # Pero con definir la opción 'sticky' no es suficiente:
        # hay activar esta propiedad más adelante.

        # en este caso no tiene nada para colocar

        # Para conseguir que la cuadricula y los widgets se
        # adapten al contenedor, si se amplia o reduce el tamaño
        # de la ventana, es necesario definir la opción 'sticky'.
        # Cuando un widget se ubica en el grid se coloca en el
        # centro de su celda o cuadro. Con 'sticky' se
        # establece el comportamiendo 'pegajoso' que tendrá el
        # widget dentro de su celda, cuando se modifique la
        # dimensión de la ventana. Para ello, se utilizan para
        # expresar sus valores los puntos cardinales: N (Norte),
        # S (Sur), (E) Este y (W) Oeste, que incluso se pueden
        # utilizar de forma combinada. El widget se quedará
        # 'pegado' a los lados de su celda en las direcciones
        # que se indiquen. cuando la ventana cambie de tamaño.
        # Pero con definir la opción 'sticky' no es suficiente:
        # hay activar esta propiedad más adelante.

        self.raiz.columnconfigure(0, weight=1)
        self.raiz.rowconfigure(0, weight=1)


    def set_banner(self,banner_holder):
        self.banner = tk.PhotoImage(file="sample.png")
        self.ic_pack = tk.Label(banner_holder, image=self.banner)
        self.ic_pack.grid()
    def place_banner (self,banner_holder):
        # Para conseguir que la cuadricula y los widgets se
        # adapten al contenedor, si se amplia o reduce el tamaño
        # de la ventana, es necesario definir la opción 'sticky'.
        # Cuando un widget se ubica en el grid se coloca en el
        # centro de su celda o cuadro. Con 'sticky' se
        # establece el comportamiendo 'pegajoso' que tendrá el
        # widget dentro de su celda, cuando se modifique la
        # dimensión de la ventana. Para ello, se utilizan para
        # expresar sus valores los puntos cardinales: N (Norte),
        # S (Sur), (E) Este y (W) Oeste, que incluso se pueden
        # utilizar de forma combinada. El widget se quedará
        # 'pegado' a los lados de su celda en las direcciones
        # que se indiquen. cuando la ventana cambie de tamaño.
        # Pero con definir la opción 'sticky' no es suficiente:
        # hay activar esta propiedad más adelante.
        banner_holder.grid(column=0, row=0, padx=5, pady=5,sticky=(N, S, E, W))
        # A continuación, se activa la propiedad de expandirse
        # o contraerse definida antes con la opción
        # 'sticky' del método grid().
        # La activación se hace por contenedores y por filas
        # y columnas asignando un peso a la opción 'weight'.
        # Esta opción asigna un peso (relativo) que se utiliza
        # para distribuir el espacio adicional entre columnas
        # y/o filas. Cuando se expanda la ventana, una columna
        # o fila con un peso 2 crecerá dos veces más rápido
        # que una columna (o fila) con peso 1. El valor
        # predeterminado es 0 que significa que la columna o
        # o fila no crecerá nada en absoluto.
        # Lo habitual es asignar pesos a filas o columnas donde
        # hay celdas con widgets.
        banner_holder.columnconfigure(0, weight=1)
        banner_holder.rowconfigure(0, weight=1)


    def set_login_elements(self, login_holder):
        fuente = font.Font(weight='bold')
        #self.user_label = ttk.Label(login_holder, text="Usuario:",font=fuente, padding=(5, 5))
        #self.passwd_label = ttk.Label(login_holder, text="Contraseña:",font=fuente, padding=(5, 5))
        self.usuario = tk.StringVar()
        self.clave = tk.StringVar()
        self.usuario.set(getpass.getuser())

        self.user_entry = ttk.Entry(login_holder, textvariable=self.usuario,
                                width=30)
        self.passwd_entry = ttk.Entry(login_holder, textvariable=self.clave,
                                show="*", width=30)
        self.separ1 = ttk.Separator(login_holder, orient=HORIZONTAL)
        self.accept_button = ttk.Button(login_holder, text="Aceptar",
                                 padding=(5, 5), command=self.aceptar)
        self.cancel_button = ttk.Button(login_holder, text="Cancelar",
                                 padding=(5, 5), command=quit)
    def place_login_holder_and_its_elements(self, login_holder):
        # Para conseguir que la cuadricula y los widgets se
        # adapten al contenedor, si se amplia o reduce el tamaño
        # de la ventana, es necesario definir la opción 'sticky'.
        # Cuando un widget se ubica en el grid se coloca en el
        # centro de su celda o cuadro. Con 'sticky' se
        # establece el comportamiendo 'pegajoso' que tendrá el
        # widget dentro de su celda, cuando se modifique la
        # dimensión de la ventana. Para ello, se utilizan para
        # expresar sus valores los puntos cardinales: N (Norte),
        # S (Sur), (E) Este y (W) Oeste, que incluso se pueden
        # utilizar de forma combinada. El widget se quedará
        # 'pegado' a los lados de su celda en las direcciones
        # que se indiquen. cuando la ventana cambie de tamaño.
        # Pero con definir la opción 'sticky' no es suficiente:
        # hay activar esta propiedad más adelante.

        login_holder.grid(column=0, row=1, padx=5, pady=5,
                               sticky=(N, S, E, W))
        #self.user_label.grid(column=0, row=0,sticky=(N, S, E, W))
        #self.user_entry.grid(column=1, row=0, columnspan=2,sticky=(E, W))
        #self.passwd_label.grid(column=0, row=1,sticky=(N, S, E, W))
        self.passwd_entry.grid(column=1, row=1,sticky=(E, W))
        self.separ1.grid(column=0, row=3, columnspan=3, pady=5,sticky=(N, S, E, W))
        self.accept_button.grid(column=1, row=4, padx=5,sticky=(W))
        self.cancel_button.grid(column=1, row=4, padx=5, sticky=(E))
        # Para conseguir que la cuadricula y los widgets se
        # adapten al contenedor, si se amplia o reduce el tamaño
        # de la ventana, es necesario definir la opción 'sticky'.
        # Cuando un widget se ubica en el grid se coloca en el
        # centro de su celda o cuadro. Con 'sticky' se
        # establece el comportamiendo 'pegajoso' que tendrá el
        # widget dentro de su celda, cuando se modifique la
        # dimensión de la ventana. Para ello, se utilizan para
        # expresar sus valores los puntos cardinales: N (Norte),
        # S (Sur), (E) Este y (W) Oeste, que incluso se pueden
        # utilizar de forma combinada. El widget se quedará
        # 'pegado' a los lados de su celda en las direcciones
        # que se indiquen. cuando la ventana cambie de tamaño.
        # Pero con definir la opción 'sticky' no es suficiente:
        # hay activar esta propiedad más adelante.

        login_holder.columnconfigure(0, weight=1)
        login_holder.rowconfigure(0, weight=1)

        login_holder.columnconfigure(1, weight=1)
        login_holder.rowconfigure(1, weight=1)

        login_holder.columnconfigure(2, weight=1)
        login_holder.rowconfigure(4, weight=1)

        # Establece el foco en la caja de entrada de la
        # contraseña.

        self.passwd_entry.focus_set()

    def aceptar(self):
        if self.clave.get() == 'tkinter':
            print("Acceso permitido")
            print("Usuario:   ", self.user_entry.get())
            print("Contraseña:", self.passwd_entry.get())
        else:
            print("Acceso denegado")
            self.clave.set("")
            self.passwd_entry.delete(0, 'end')
            self.passwd_entry.focus_set()










def main():
    mi_app = Hamming_interface()
    mi_app.mainloop()
    return 0


if __name__ == '__main__':
    main()
