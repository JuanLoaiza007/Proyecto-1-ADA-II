# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ihuntgore/Escritorio/proyectos/ada/Proyecto-1-ADA-II/views/vista_principal.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("/*\n"
" *\n"
" *  Simple Stylesheet inspired on Bootstrap for Qt Designer / Qt Creator \n"
" *  File: bootstylesheet.css\n"
" *  Author: JuanLoaiza007\n"
" *  Version: 1.1.1\n"
" *\n"
" */\n"
"\n"
"/*  # Español\n"
" *  Instrucciones para aplicar en Qt Designer / Qt Creator\n"
" *  1. Busque la vista de Inspector de objetos >> Objeto >> \"MainWindow\".\n"
" *  2. Dale clic derecho a \"MainWindow\" y seleccione \"Cambiar HojaDeEstilos\" o algo similar.\n"
" *  3. Pegue el contenido de este archivo ahí.\n"
" *  4. De clic en Aplicar y Aceptar.\n"
" *  5. Para aplicar los estilos seleccione un objeto, en el Editor de Propiedades agregue un Filtro tipo cadena de texto y nombrelo \"class\".\n"
" *  6. En el Editor de Propiedades habrá una seccion nueva llamada \"Propiedades dinámicas\" y una propiedad llamada \"class\", en la casilla de la derecha aplique todos los estilos que desee, eg. \"btn btn-outline-primary br-4\". \n"
" */\n"
"\n"
"/*  # English\n"
" *  Instructions to apply in Qt Designer / Qt Creator\n"
" *  1. Keep an eye on the Object Inspector >> Object >> \"MainWindow\".\n"
" *  2. Right click on \"MainWindow\" and select \"Change StyleSheet\" or something similar.\n"
" *  3. Paste the content of this file there.\n"
" *  4. Click Apply and Accept.\n"
" *  5. To apply the styles, select an object, in the Properties Editor add a Text String Filter and name it \"class\".\n"
" *  6. In the Property Editor there will be a new section called \"Dynamic Properties\" and a property called \"class\", in the box on the right apply all the styles you want, eg. \"btn btn-outline-primary br-4\". \n"
" */\n"
"\n"
"QMainWindow {\n"
"  font-family: \"sans-serif\";\n"
"}\n"
"\n"
"/* Border Settings */\n"
"/* Border Side Weight */\n"
".nb {\n"
"  border: 0px solid;\n"
"}\n"
".b-st-1 {\n"
"  border-top: 1px solid;\n"
"}\n"
".b-sb-1 {\n"
"  border-bottom: 1px solid;\n"
"}\n"
".b-sl-1 {\n"
"  border-left: 1px solid;\n"
"}\n"
".b-sr-1 {\n"
"  border-right: 1px solid;\n"
"}\n"
".b-st-2 {\n"
"  border-top: 2px solid;\n"
"}\n"
".b-sb-2 {\n"
"  border-bottom: 2px solid;\n"
"}\n"
".b-sl-2 {\n"
"  border-left: 2px solid;\n"
"}\n"
".b-sr-2 {\n"
"  border-right: 2px solid;\n"
"}\n"
".b-st-3 {\n"
"  border-top: 3px solid;\n"
"}\n"
".b-sb-3 {\n"
"  border-bottom: 3px solid;\n"
"}\n"
".b-sl-3 {\n"
"  border-left: 3px solid;\n"
"}\n"
".b-sr-3 {\n"
"  border-right: 3px solid;\n"
"}\n"
".b-st-4 {\n"
"  border-top: 4px solid;\n"
"}\n"
".b-sb-4 {\n"
"  border-bottom: 4px solid;\n"
"}\n"
".b-sl-4 {\n"
"  border-left: 4px solid;\n"
"}\n"
".b-sr-4 {\n"
"  border-right: 4px solid;\n"
"}\n"
"\n"
"/* Radius */\n"
".br-1 {\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
".br-2 {\n"
"  border-radius: 15px;\n"
"}\n"
"\n"
".br-3 {\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
".br-4 {\n"
"  border-radius: 25px;\n"
"}\n"
"\n"
"/* Background colors */\n"
".background-white {\n"
"  background-color: white;\n"
"}\n"
".background-light {\n"
"  background-color: #f8f9fa;\n"
"}\n"
".background-black {\n"
"  background-color: black;\n"
"}\n"
".background-primary {\n"
"  background-color: #0d6efd;\n"
"}\n"
".background-success {\n"
"  background-color: #198754;\n"
"}\n"
".background-warning {\n"
"  background-color: #ffc720;\n"
"}\n"
".background-danger {\n"
"  background-color: #dc3545;\n"
"}\n"
"\n"
"/* Colors */\n"
".color-white {\n"
"  color: white;\n"
"}\n"
".color-light {\n"
"  color: #f8f9fa;\n"
"}\n"
".color-black {\n"
"  color: black;\n"
"}\n"
".color-primary {\n"
"  color: #0d6efd;\n"
"}\n"
".color-success {\n"
"  color: #198754;\n"
"}\n"
".color-warning {\n"
"  color: #ffc720;\n"
"}\n"
".color-danger {\n"
"  color: #dc3545;\n"
"}\n"
"\n"
"/* Buttons */\n"
"QPushButton {\n"
"  font-weight: 500;\n"
"  color: white;\n"
"  background-color: gray;\n"
"  padding: 6px 12px;\n"
"  font-size: 18px;\n"
"  border-radius: 10px;\n"
"  border: 1px solid;\n"
"}\n"
"\n"
".btn {\n"
"  font-weight: 500;\n"
"  color: white;\n"
"  background-color: gray;\n"
"  padding: 6px 12px;\n"
"  font-size: 18px;\n"
"  border-radius: 10px;\n"
"  border: 1px solid;\n"
"}\n"
"\n"
".btn-primary {\n"
"  color: #fff;\n"
"  background-color: #0d6efd;\n"
"  border-color: #0d6efd;\n"
"}\n"
".btn-primary:hover {\n"
"  color: #fff;\n"
"  background-color: #0b5ed7;\n"
"  border-color: #0a58ca;\n"
"}\n"
"\n"
".btn-secondary {\n"
"  color: #fff;\n"
"  background-color: #6c757d;\n"
"  border-color: #6c757d;\n"
"}\n"
".btn-secondary:hover {\n"
"  color: #fff;\n"
"  background-color: #5c636a;\n"
"  border-color: #565e64;\n"
"}\n"
"\n"
".btn-success {\n"
"  color: #fff;\n"
"  background-color: #198754;\n"
"  border-color: #198754;\n"
"}\n"
".btn-success:hover {\n"
"  color: #fff;\n"
"  background-color: #157347;\n"
"  border-color: #146c43;\n"
"}\n"
"\n"
".btn-warning {\n"
"  color: #000;\n"
"  background-color: #ffc107;\n"
"  border-color: #ffc107;\n"
"}\n"
".btn-warning:hover {\n"
"  color: #000;\n"
"  background-color: #ffca2c;\n"
"  border-color: #ffc720;\n"
"}\n"
"\n"
".btn-danger {\n"
"  color: #fff;\n"
"  background-color: #dc3545;\n"
"  border-color: #dc3545;\n"
"}\n"
".btn-danger:hover {\n"
"  color: #fff;\n"
"  background-color: #bb2d3b;\n"
"  border-color: #b02a37;\n"
"}\n"
"\n"
".btn-light {\n"
"  color: #000;\n"
"  background-color: #f8f9fa;\n"
"  border-color: #f8f9fa;\n"
"}\n"
".btn-light:hover {\n"
"  color: #000;\n"
"  background-color: #f9fafb;\n"
"  border-color: #f9fafb;\n"
"}\n"
"\n"
".btn-dark {\n"
"  color: #fff;\n"
"  background-color: #212529;\n"
"  border-color: #212529;\n"
"}\n"
".btn-dark:hover {\n"
"  color: #fff;\n"
"  background-color: #1c1f23;\n"
"  border-color: #1a1e21;\n"
"}\n"
"\n"
".btn-outline-primary {\n"
"  background-color: white;\n"
"  color: #0d6efd;\n"
"  border-color: #0d6efd;\n"
"}\n"
".btn-outline-primary:hover {\n"
"  color: #fff;\n"
"  background-color: #0d6efd;\n"
"  border-color: #0d6efd;\n"
"}\n"
"\n"
".btn-outline-secondary {\n"
"  background-color: white;\n"
"  color: #6c757d;\n"
"  border-color: #6c757d;\n"
"}\n"
".btn-outline-secondary:hover {\n"
"  color: #fff;\n"
"  background-color: #6c757d;\n"
"  border-color: #6c757d;\n"
"}\n"
"\n"
".btn-outline-success {\n"
"  background-color: white;\n"
"  color: #198754;\n"
"  border-color: #198754;\n"
"}\n"
".btn-outline-success:hover {\n"
"  color: #fff;\n"
"  background-color: #198754;\n"
"  border-color: #198754;\n"
"}\n"
"\n"
".btn-outline-info {\n"
"  background-color: white;\n"
"  color: #0dcaf0;\n"
"  border-color: #0dcaf0;\n"
"}\n"
".btn-outline-info:hover {\n"
"  color: #000;\n"
"  background-color: #0dcaf0;\n"
"}\n"
"\n"
".btn-outline-warning {\n"
"  background-color: white;\n"
"  color: #ffc107;\n"
"  border-color: #ffc107;\n"
"}\n"
".btn-outline-warning:hover {\n"
"  color: #000;\n"
"  background-color: #ffc107;\n"
"  border-color: #ffc107;\n"
"}\n"
"\n"
".btn-outline-danger {\n"
"  background-color: white;\n"
"  color: #dc3545;\n"
"  border-color: #dc3545;\n"
"}\n"
".btn-outline-danger:hover {\n"
"  color: #fff;\n"
"  background-color: #dc3545;\n"
"  border-color: #dc3545;\n"
"}\n"
"\n"
".btn-outline-light {\n"
"  background-color: #41464b;\n"
"  color: #f8f9fa;\n"
"  border-color: #f8f9fa;\n"
"}\n"
".btn-outline-light:hover {\n"
"  color: #000;\n"
"  background-color: #f8f9fa;\n"
"  border-color: #f8f9fa;\n"
"}\n"
"\n"
".btn-outline-dark {\n"
"  background-color: white;\n"
"  color: #212529;\n"
"  border-color: #212529;\n"
"}\n"
".btn-outline-dark:hover {\n"
"  color: #fff;\n"
"  background-color: #212529;\n"
"  border-color: #212529;\n"
"}\n"
"\n"
".btn-link {\n"
"  background-color: white;\n"
"  font-weight: 400;\n"
"  color: #0d6efd;\n"
"  text-decoration: underline;\n"
"}\n"
".btn-link:hover {\n"
"  color: #0a58ca;\n"
"}\n"
"\n"
"/* Title sizes */\n"
"QLabel {\n"
"  font-size: 22px;\n"
"}\n"
"\n"
".h1 {\n"
"  font-size: 42px;\n"
"}\n"
"\n"
".h2 {\n"
"  font-size: 36px;\n"
"}\n"
"\n"
".h3 {\n"
"  font-size: 32px;\n"
"}\n"
"\n"
".h4 {\n"
"  font-size: 28px;\n"
"}\n"
"\n"
".h5 {\n"
"  font-size: 22px;\n"
"}\n"
"\n"
".h6 {\n"
"  font-size: 18px;\n"
"}\n"
"\n"
"/* Alerts */\n"
".alert {\n"
"  border: 1px solid;\n"
"}\n"
"\n"
".alert-primary {\n"
"  color: #084298;\n"
"  background-color: #cfe2ff;\n"
"  border-color: #b6d4fe;\n"
"}\n"
".alert-secondary {\n"
"  color: #41464b;\n"
"  background-color: #e2e3e5;\n"
"  border-color: #d3d6d8;\n"
"}\n"
".alert-success {\n"
"  color: #0f5132;\n"
"  background-color: #d1e7dd;\n"
"  border-color: #badbcc;\n"
"}\n"
".alert-info {\n"
"  color: #055160;\n"
"  background-color: #cff4fc;\n"
"  border-color: #b6effb;\n"
"}\n"
".alert-warning {\n"
"  color: #664d03;\n"
"  background-color: #fff3cd;\n"
"  border-color: #ffecb5;\n"
"}\n"
".alert-danger {\n"
"  color: #842029;\n"
"  background-color: #f8d7da;\n"
"  border-color: #f5c2c7;\n"
"}\n"
".alert-light {\n"
"  color: #636464;\n"
"  background-color: #fefefe;\n"
"  border-color: #fdfdfe;\n"
"}\n"
".alert-dark {\n"
"  color: #141619;\n"
"  background-color: #d3d3d4;\n"
"  border-color: #bcbebf;\n"
"}\n"
"")
        MainWindow.setProperty("class", "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.head = QtWidgets.QFrame(self.centralwidget)
        self.head.setMinimumSize(QtCore.QSize(800, 100))
        self.head.setMaximumSize(QtCore.QSize(16777215, 150))
        self.head.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.head.setFrameShadow(QtWidgets.QFrame.Raised)
        self.head.setObjectName("head")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.head)
        self.verticalLayout_2.setContentsMargins(10, 5, 10, 5)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.head1 = QtWidgets.QFrame(self.head)
        self.head1.setMinimumSize(QtCore.QSize(780, 40))
        self.head1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.head1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.head1.setObjectName("head1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.head1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_tituloPrograma = QtWidgets.QLabel(self.head1)
        self.lbl_tituloPrograma.setMinimumSize(QtCore.QSize(390, 45))
        self.lbl_tituloPrograma.setMaximumSize(QtCore.QSize(340, 16777215))
        self.lbl_tituloPrograma.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_tituloPrograma.setObjectName("lbl_tituloPrograma")
        self.horizontalLayout_3.addWidget(self.lbl_tituloPrograma)
        self.lbl_archivo_cargado = QtWidgets.QLabel(self.head1)
        self.lbl_archivo_cargado.setMinimumSize(QtCore.QSize(0, 0))
        self.lbl_archivo_cargado.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_archivo_cargado.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_archivo_cargado.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_archivo_cargado.setWordWrap(True)
        self.lbl_archivo_cargado.setObjectName("lbl_archivo_cargado")
        self.horizontalLayout_3.addWidget(self.lbl_archivo_cargado)
        self.btn_cargarArchivo = QtWidgets.QPushButton(self.head1)
        self.btn_cargarArchivo.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_cargarArchivo.setMaximumSize(QtCore.QSize(170, 40))
        self.btn_cargarArchivo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cargarArchivo.setObjectName("btn_cargarArchivo")
        self.horizontalLayout_3.addWidget(self.btn_cargarArchivo)
        self.verticalLayout_2.addWidget(self.head1)
        self.head2 = QtWidgets.QFrame(self.head)
        self.head2.setMinimumSize(QtCore.QSize(780, 30))
        self.head2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.head2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.head2.setObjectName("head2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.head2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.box_algoritmo = QtWidgets.QComboBox(self.head2)
        self.box_algoritmo.setMinimumSize(QtCore.QSize(322, 32))
        self.box_algoritmo.setMaximumSize(QtCore.QSize(380, 16777215))
        self.box_algoritmo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.box_algoritmo.setObjectName("box_algoritmo")
        self.box_algoritmo.addItem("")
        self.box_algoritmo.addItem("")
        self.box_algoritmo.addItem("")
        self.horizontalLayout_4.addWidget(self.box_algoritmo)
        self.btn_iniciar = QtWidgets.QPushButton(self.head2)
        self.btn_iniciar.setMinimumSize(QtCore.QSize(100, 35))
        self.btn_iniciar.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_iniciar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_iniciar.setObjectName("btn_iniciar")
        self.horizontalLayout_4.addWidget(self.btn_iniciar)
        self.right_separator = QtWidgets.QFrame(self.head2)
        self.right_separator.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.right_separator.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_separator.setObjectName("right_separator")
        self.horizontalLayout_4.addWidget(self.right_separator)
        self.verticalLayout_2.addWidget(self.head2)
        self.verticalLayout.addWidget(self.head)
        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setMinimumSize(QtCore.QSize(800, 430))
        self.body.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bodyleft = QtWidgets.QFrame(self.body)
        self.bodyleft.setMinimumSize(QtCore.QSize(380, 0))
        self.bodyleft.setMaximumSize(QtCore.QSize(800, 16777215))
        self.bodyleft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bodyleft.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bodyleft.setObjectName("bodyleft")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.bodyleft)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bodytitle = QtWidgets.QFrame(self.bodyleft)
        self.bodytitle.setMinimumSize(QtCore.QSize(387, 26))
        self.bodytitle.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bodytitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bodytitle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bodytitle.setObjectName("bodytitle")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.bodytitle)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lbl_entrada = QtWidgets.QLabel(self.bodytitle)
        self.lbl_entrada.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_entrada.setObjectName("lbl_entrada")
        self.verticalLayout_7.addWidget(self.lbl_entrada, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.bodytitle)
        self.bodybody = QtWidgets.QFrame(self.bodyleft)
        self.bodybody.setMinimumSize(QtCore.QSize(380, 380))
        self.bodybody.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bodybody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bodybody.setObjectName("bodybody")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.bodybody)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.txtE_entrada = QtWidgets.QTextEdit(self.bodybody)
        self.txtE_entrada.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtE_entrada.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txtE_entrada.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txtE_entrada.setObjectName("txtE_entrada")
        self.horizontalLayout_7.addWidget(self.txtE_entrada)
        self.verticalLayout_3.addWidget(self.bodybody)
        self.horizontalLayout_2.addWidget(self.bodyleft)
        self.bodyright = QtWidgets.QFrame(self.body)
        self.bodyright.setMinimumSize(QtCore.QSize(380, 0))
        self.bodyright.setMaximumSize(QtCore.QSize(800, 16777215))
        self.bodyright.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bodyright.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bodyright.setObjectName("bodyright")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.bodyright)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.bodytitle_2 = QtWidgets.QFrame(self.bodyright)
        self.bodytitle_2.setMinimumSize(QtCore.QSize(387, 26))
        self.bodytitle_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bodytitle_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bodytitle_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bodytitle_2.setObjectName("bodytitle_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.bodytitle_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.bodytitle_2)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addWidget(self.bodytitle_2)
        self.bodybody_2 = QtWidgets.QFrame(self.bodyright)
        self.bodybody_2.setMinimumSize(QtCore.QSize(0, 380))
        self.bodybody_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bodybody_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bodybody_2.setObjectName("bodybody_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.bodybody_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.txtE_salida = QtWidgets.QTextEdit(self.bodybody_2)
        self.txtE_salida.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtE_salida.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtE_salida.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.txtE_salida.setFrameShadow(QtWidgets.QFrame.Plain)
        self.txtE_salida.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txtE_salida.setAcceptRichText(False)
        self.txtE_salida.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txtE_salida.setObjectName("txtE_salida")
        self.horizontalLayout_8.addWidget(self.txtE_salida)
        self.verticalLayout_4.addWidget(self.bodybody_2)
        self.horizontalLayout_2.addWidget(self.bodyright)
        self.verticalLayout.addWidget(self.body)
        self.foot = QtWidgets.QFrame(self.centralwidget)
        self.foot.setMinimumSize(QtCore.QSize(800, 70))
        self.foot.setMaximumSize(QtCore.QSize(16777215, 70))
        self.foot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.foot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.foot.setObjectName("foot")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.foot)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.foot1left = QtWidgets.QFrame(self.foot)
        self.foot1left.setMaximumSize(QtCore.QSize(260, 16777215))
        self.foot1left.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.foot1left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.foot1left.setObjectName("foot1left")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.foot1left)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_sobre = QtWidgets.QPushButton(self.foot1left)
        self.btn_sobre.setMinimumSize(QtCore.QSize(100, 35))
        self.btn_sobre.setMaximumSize(QtCore.QSize(120, 35))
        self.btn_sobre.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sobre.setObjectName("btn_sobre")
        self.verticalLayout_5.addWidget(self.btn_sobre)
        self.horizontalLayout.addWidget(self.foot1left)
        self.foot2center = QtWidgets.QFrame(self.foot)
        self.foot2center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.foot2center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.foot2center.setObjectName("foot2center")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.foot2center)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_exportar = QtWidgets.QPushButton(self.foot2center)
        self.btn_exportar.setMinimumSize(QtCore.QSize(104, 35))
        self.btn_exportar.setMaximumSize(QtCore.QSize(200, 35))
        self.btn_exportar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exportar.setObjectName("btn_exportar")
        self.horizontalLayout_5.addWidget(self.btn_exportar, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.foot2center)
        self.foot3right = QtWidgets.QFrame(self.foot)
        self.foot3right.setMaximumSize(QtCore.QSize(260, 16777215))
        self.foot3right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.foot3right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.foot3right.setObjectName("foot3right")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.foot3right)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbl_optimalidad = QtWidgets.QLabel(self.foot3right)
        self.lbl_optimalidad.setMinimumSize(QtCore.QSize(240, 0))
        self.lbl_optimalidad.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lbl_optimalidad.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_optimalidad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_optimalidad.setObjectName("lbl_optimalidad")
        self.verticalLayout_6.addWidget(self.lbl_optimalidad, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addWidget(self.foot3right)
        self.verticalLayout.addWidget(self.foot)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Riego Optimo"))
        self.centralwidget.setProperty("class", _translate("MainWindow", "background-white"))
        self.lbl_tituloPrograma.setText(_translate("MainWindow", "Proyecto 1 - Riego Óptimo"))
        self.lbl_tituloPrograma.setProperty("class", _translate("MainWindow", "h4 color-primary"))
        self.lbl_archivo_cargado.setText(_translate("MainWindow", "No hay archivo cargado"))
        self.lbl_archivo_cargado.setProperty("class", _translate("MainWindow", "h6 color-danger"))
        self.btn_cargarArchivo.setText(_translate("MainWindow", "Cargar archivo"))
        self.btn_cargarArchivo.setProperty("class", _translate("MainWindow", "btn-primary br-2"))
        self.box_algoritmo.setProperty("class", _translate("MainWindow", "h6"))
        self.box_algoritmo.setItemText(0, _translate("MainWindow", "Fuerza bruta"))
        self.box_algoritmo.setItemText(1, _translate("MainWindow", "Programación Dinámica"))
        self.box_algoritmo.setItemText(2, _translate("MainWindow", "Programación Voraz"))
        self.btn_iniciar.setText(_translate("MainWindow", "Iniciar"))
        self.btn_iniciar.setProperty("class", _translate("MainWindow", "btn-danger br-2"))
        self.bodytitle.setProperty("class", _translate("MainWindow", "b-st-1 b-sb-1 b-sl-1 b-sr-1"))
        self.lbl_entrada.setText(_translate("MainWindow", "Entrada"))
        self.bodybody.setProperty("class", _translate("MainWindow", "b-st-1 b-sb-1 b-sl-1 b-sr-1"))
        self.txtE_entrada.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'San Francisco Text\'; font-size:18px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.txtE_entrada.setPlaceholderText(_translate("MainWindow", "Presione \"Cargar archivo\" para cargar datos de entrada"))
        self.txtE_entrada.setProperty("class", _translate("MainWindow", "h6"))
        self.bodytitle_2.setProperty("class", _translate("MainWindow", "b-st-1 b-sb-1 b-sl-1 b-sr-1"))
        self.label_3.setText(_translate("MainWindow", "Salida"))
        self.bodybody_2.setProperty("class", _translate("MainWindow", "b-st-1 b-sb-1 b-sl-1 b-sr-1"))
        self.txtE_salida.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'San Francisco Text\'; font-size:18px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.txtE_salida.setPlaceholderText(_translate("MainWindow", "Presione \"Iniciar\" para iniciar el algoritmo con la Entrada"))
        self.txtE_salida.setProperty("class", _translate("MainWindow", "h6"))
        self.btn_sobre.setText(_translate("MainWindow", "Sobre"))
        self.btn_sobre.setProperty("class", _translate("MainWindow", "btn-outline-dark br-2"))
        self.btn_exportar.setText(_translate("MainWindow", "Exportar"))
        self.btn_exportar.setProperty("class", _translate("MainWindow", "btn-primary br-2"))
        self.lbl_optimalidad.setText(_translate("MainWindow", "Es optima"))
        self.lbl_optimalidad.setProperty("class", _translate("MainWindow", "color-danger"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
