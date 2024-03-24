# [controlador_principal.py]

import os
from PyQt5 import QtWidgets, QtGui
from views.vista_principal import Ui_MainWindow
from models.modelo_principal import modelo_principal
from models.tools.txt_parser import leer_archivo_txt
from models.tools.temporizador import Temporizador
from views.sm_dialog_clean import Ui_Dialog as sm_dialog_clean

debug = True


def print_debug(message):
    new_message = "controlador_principal.py: " + message
    if debug:
        print(new_message)


class controlador_principal:
    # Funcion para inicializar
    def cargar(self, main_window):
        self.modelo = modelo_principal()

        self.MainWindow = main_window
        self.MainWindow.setMinimumSize(self.MainWindow.minimumSizeHint())
        self.MainWindow.setMaximumSize(16777215, 16777215)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.ui.lbl_optimalidad.setText("")
        self.ui.box_algoritmo.setCurrentIndex(0)
        self.modelo.set_algoritmo('exhaustivo')

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

    def block_focus(self):
        self.MainWindow.setEnabled(False)
        self.ui.centralwidget.setEnabled(False)
        self.ui.centralwidget.setVisible(False)
        self.MainWindow.setFixedSize(self.MainWindow.size())

    def unblock_focus(self):
        self.MainWindow.setMinimumSize(self.MainWindow.minimumSizeHint())
        self.MainWindow.setMaximumSize(16777215, 16777215)
        self.MainWindow.setEnabled(True)
        self.ui.centralwidget.setEnabled(True)
        self.ui.centralwidget.setVisible(True)

    def mostrar_dialogo(self, titulo, mensaje):
        self.block_focus()
        Temporizador.iniciar(1)

        new_dialog = QtWidgets.QDialog()
        new_ui = sm_dialog_clean()
        new_ui.setupUi(new_dialog)
        new_dialog.setModal(True)
        new_dialog.show()
        new_ui.lbl_title.setText(titulo)
        new_ui.lbl_body.setText(mensaje)

        new_dialog.exec()

        self.unblock_focus()

    # Funciones específicas

    def cargar_archivo(self):
        self.ui.lbl_optimalidad.setText("")
        self.block_focus()
        Temporizador.iniciar(1)
        parsed = leer_archivo_txt()

        if parsed == None:
            print_debug(
                "No se ha seleccionado ningún archivo, la finca no cambia en modelo")
            self.unblock_focus()
            return None

        finca = parsed[0]
        txt = parsed[1]
        self.modelo.set_finca(finca)

        finca_str = str(self.modelo.get_finca())
        txt_str = str(txt)
        self.ui.txtE_entrada.setText(
            f"=== Interpretacion ===\nFinca: {finca_str} \n\n=== Archivo cargado ===\n{txt_str}")

        self.ui.txtE_salida.setText("")
        self.unblock_focus()

    def cambiar_algoritmo(self):
        self.ui.lbl_optimalidad.setText("")
        indice_actual = self.ui.box_algoritmo.currentIndex()
        if indice_actual == 0:
            self.modelo.set_algoritmo('exhaustivo')
        elif indice_actual == 1:
            print_debug(
                "He cambiado el algoritmo a voraz, si ha creado un algoritmo dinamico no olvide cambiar esta parte")
            self.modelo.set_algoritmo('voraz')
        elif indice_actual == 2:
            self.modelo.set_algoritmo('voraz')

        self.ui.txtE_salida.setText("")

        print_debug("ItemComboBox is {}. {}".format(
            self.ui.box_algoritmo.currentIndex(),
            self.ui.box_algoritmo.currentText()))

    def iniciar(self):
        if self.modelo.get_finca() == None:
            titulo = "Error"
            mensaje = "Debe cargar un archivo antes de iniciar el algoritmo"
            self.mostrar_dialogo(titulo, mensaje)
            print_debug(
                "No se pudo iniciar, el modelo no tiene una finca cargada.")
            return None

        self.resultado = self.modelo.iniciar()
        resultado_str = str(self.resultado)
        preview = self.modelo.prev_prog_exportable(self.resultado)

        self.ui.txtE_salida.setText(
            f"=== Interpretacion ===\nProgramación óptima {resultado_str} \n\n=== Archivo exportable ===\n{preview}")

        if str(self.modelo.get_algoritmo()) == "exhaustivo":
            self.ui.lbl_optimalidad.setText("Es óptima")
        else:
            self.ui.lbl_optimalidad.setText("No asegura la óptima")

        print_debug("El resultado del algoritmo es {}".format(
            str(self.resultado)))

    def exportar(self):
        self.block_focus()
        Temporizador.iniciar(1)

        if self.modelo.get_resultado() == None:
            titulo = "Error"
            mensaje = "No es posible exportar un archivo si el algoritmo no se ha ejecutado"
            self.mostrar_dialogo(titulo, mensaje)

            print_debug(
                "No es posible exportar un archivo si el algoritmo no se ha ejecutado")
            self.unblock_focus()
            return None

        ruta_archivo = self.modelo.exportar()
        if ruta_archivo == None or ruta_archivo == "()":
            print_debug(
                "Algo falló o se canceló la exportación, obtuve ruta None.")
        else:
            titulo = "Atención"
            mensaje = "Se ha exportado el archivo en la ruta:\n'{}'".format(
                str(ruta_archivo))
            self.mostrar_dialogo(titulo, mensaje)
            print_debug(
                "Se ha exportado el archivo en la ruta '{}'".format(str(ruta_archivo)))

        self.unblock_focus()

    def mostrar_sobre_nosotros(self):
        from controllers.controlador_sobre_nosotros import controlador_sobre_nosotros
        self.controlador_sobre_nosotros = controlador_sobre_nosotros()
        self.controlador_sobre_nosotros.mostrar(self.MainWindow)
