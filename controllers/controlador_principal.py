# controlador_principal.py

import os
from PyQt5 import QtWidgets, QtGui
from views.vista_principal import Ui_MainWindow
from models.modelo_principal import modelo_principal
from views.sm_dialog_clean import Ui_Dialog as sm_dialog_clean


class controlador_principal:
    # Funcion para inicializar (general)
    def cargar(self, main_window):
        self.modelo = modelo_principal()
        self.MainWindow = main_window
        self.MainWindow.setMinimumSize(self.MainWindow.minimumSizeHint())
        self.MainWindow.setMaximumSize(16777215, 16777215)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        # Listeners específicos
        self.ui.btn_cargarArchivo.clicked.connect(self.cargar_archivo)
        self.ui.box_algoritmo.currentIndexChanged.connect(
            self.cambiar_algoritmo)
        self.ui.btn_iniciar.clicked.connect(self.iniciar)
        self.ui.btn_exportar.clicked.connect(self.exportar)
        self.ui.btn_sobre.clicked.connect(self.mostrar_sobre_nosotros)

    # Funciones de ventana
    def mostrar(self, main_window):
        self.cargar(main_window)
        self.MainWindow.show()

    def block_focus(self, window):
        self.MainWindow.setEnabled(False)
        self.MainWindow.setFixedSize(window.size())

    def unblock_focus(self):
        self.MainWindow.setMinimumSize(self.MainWindow.minimumSizeHint())
        self.MainWindow.setMaximumSize(16777215, 16777215)
        self.MainWindow.setEnabled(True)

    # Funciones específicas
    def cargar_archivo(self):
        print("Ha presionado el boton para cargar archivos")

    def cambiar_algoritmo(self):
        indice_actual = self.ui.box_algoritmo.currentIndex()
        contenido_actual = self.ui.box_algoritmo.currentText()
        print("Índice seleccionado:", indice_actual)
        print("Contenido seleccionado:", contenido_actual)

    def iniciar(self):
        print("Ha presionado el boton para iniciar el algorirmo")

    def exportar(self):
        print("Ha presionado el boton para exportar el archivo")

    def mostrar_sobre_nosotros(self):
        from controllers.controlador_sobre_nosotros import controlador_sobre_nosotros
        self.controlador_sobre_nosotros = controlador_sobre_nosotros()
        self.controlador_sobre_nosotros.mostrar(self.MainWindow)
