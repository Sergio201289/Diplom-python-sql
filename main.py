
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Station import Ui_Station
from Sensors import Ui_Sensors
from TypeOfSensors import Ui_TypeOfSensors
from AddStation import Ui_AddStation
from AddSensors import Ui_AddSensors
from AddEmployeers import Ui_AddEmployeers
from AddTypeOfSensors import Ui_AddTypeOfSensors
from start import Ui_Start
from Employees import Ui_Employees
from EditStation import Ui_EditStation
from EditTypeOfSensors import Ui_EditTypeOfSensors
from EditSensors import Ui_EditSensors
from EditEmployeers import Ui_EditEmployeers
from Login import Ui_Login

app = QtWidgets.QApplication(sys.argv)

Login = QtWidgets.QMainWindow()
uilogin = Ui_Login()
uilogin.setupUi(Login)
Login.show()

def okbutton():
    if uilogin.lineEdit.text() == "Admin" and uilogin.lineEdit_2.text() == "1q2w3e4r-":
        Login.close()
        start()
    else:
        uilogin.lineEdit.clear()
        uilogin.lineEdit_2.clear()

uilogin.pushButton.clicked.connect(okbutton)

def start():
    # Иницилазация стартового окна
    global Start
    Start = QtWidgets.QMainWindow()
    uistart = Ui_Start()
    uistart.setupUi(Start)
    Start.show()

    # Функция вызова окна Сотрудники
    def openemployees():
        # Инициализация окна сотрудники
        global Employees
        Employees = QtWidgets.QMainWindow()
        uiempl = Ui_Employees()
        uiempl.setupUi(Employees)
        Start.close()
        Employees.show()

        def serialfilter():
            uiempl.serialfilter()

        def lastnamefilter():
            uiempl.lastnamefilter()

        def firstnamefilter():
            uiempl.firstnamefilter()

        def positionfilter():
            uiempl.positionfilter()

        def backbutton():
            Employees.close()
            Start.show()

        def openaddemployees():
            global AddEmployees
            AddEmployees = QtWidgets.QMainWindow()
            uiaddempl = Ui_AddEmployeers()
            uiaddempl.setupUi(AddEmployees)
            AddEmployees.show()

            def okbutton():
                uiaddempl.okbutton()
                uiempl.loadData()
                AddEmployees.close()

            uiaddempl.okButton.clicked.connect(okbutton)

        def openeditemployees():
            try:
                global EditEmployeers
                EditEmployeers = QtWidgets.QMainWindow()
                uieditempl = Ui_EditEmployeers()
                uieditempl.setupUi(EditEmployeers)
                serial = uiempl.tableWidget.item(uiempl.tableWidget.currentRow(), 0).text()
                lastname = uiempl.tableWidget.item(uiempl.tableWidget.currentRow(), 1).text()
                firstname = uiempl.tableWidget.item(uiempl.tableWidget.currentRow(), 2).text()
                position = uiempl.tableWidget.item(uiempl.tableWidget.currentRow(), 3).text()
                uieditempl.lineEdit.setText(serial)
                uieditempl.lineEdit_2.setText(lastname)
                uieditempl.lineEdit_3.setText(firstname)
                uieditempl.lineEdit_4.setText(position)
                EditEmployeers.show()
            except:
                pass

            def okbutton():
                uieditempl.okbutton(serial)
                uiempl.loadData()
                EditEmployeers.close()

            uieditempl.okButton.clicked.connect(okbutton)

        def deletebutton():
            uiempl.deletebutton()
            uiempl.loadData()

        uiempl.BackButton.clicked.connect(backbutton)
        uiempl.AddButton.clicked.connect(openaddemployees)
        uiempl.EditButton.clicked.connect(openeditemployees)
        uiempl.DeleteButton.clicked.connect(deletebutton)
        uiempl.lineEdit.textChanged.connect(serialfilter)
        uiempl.lineEdit_2.textChanged.connect(lastnamefilter)
        uiempl.lineEdit_3.textChanged.connect(firstnamefilter)
        uiempl.lineEdit_4.textChanged.connect(positionfilter)

    # Функция вызова окна Станции
    def openstations():
        # Инициализация окна Станции
        global Station
        Station = QtWidgets.QMainWindow()
        uistat = Ui_Station()
        uistat.setupUi(Station)
        Station.show()
        Start.close()

        def stationfilter():
            uistat.stationfilter()

        def linefilter():
            uistat.linefilter()

        def coordinatesfilter():
            uistat.coordinatesfilter()

        # Функция вернуться назад
        def backbutton():
            Station.close()
            Start.show()

        # Функция Удалить запись класса Станции
        def deletebuton():
            uistat.deletebutton()
            uistat.loadData()

        # Функция вызова окна Добавить станцию
        def openaddstation():
            # Инициализация окна Добавить станцию
            global AddStation
            AddStation = QtWidgets.QMainWindow()
            uiaddstat = Ui_AddStation()
            uiaddstat.setupUi(AddStation)
            AddStation.show()

            # Функция подтверждения Добавления станции
            def okbutton():
                uiaddstat.okbutton()
                uistat.loadData()
                AddStation.close()

            # Обработка сигнала нажатия кнопки OK
            uiaddstat.okButton.clicked.connect(okbutton)

        # функция вызова окна Редактировать станцию
        def openeditstation():
            # Инициализация окна Редактировать станцию
            try:
                global EditStation
                EditStation = QtWidgets.QMainWindow()
                uieditstat = Ui_EditStation()
                uieditstat.setupUi(EditStation)
                station = uistat.tableWidget.item(uistat.tableWidget.currentRow(), 0).text()
                line = uistat.tableWidget.item(uistat.tableWidget.currentRow(), 1).text()
                coordinates = uistat.tableWidget.item(uistat.tableWidget.currentRow(), 2).text()
                uieditstat.lineEdit.setText(station)
                uieditstat.lineEdit_2.setText(line)
                uieditstat.lineEdit_3.setText(coordinates)
                EditStation.show()
            except:
                pass

            # Функция подтверждения Редактирования станции
            def okbutton():
                uieditstat.okbutton(station)
                uistat.loadData()
                EditStation.close()

            # Обработка сигнала нажатия кнопки ОК
            uieditstat.okButton.clicked.connect(okbutton)

        # Функция вызова окна Тип датчика
        def opentypeofsensors():
            # Инициализация окна Тип Датчика
            try:
                global TypeOfSensors
                TypeOfSensors = QtWidgets.QMainWindow()
                uitype = Ui_TypeOfSensors()
                uitype.setupUi(TypeOfSensors)
                station = uistat.tableWidget.item(uistat.tableWidget.currentRow(), 0).text()
                uitype.loaddate(station)
                Station.close()
                TypeOfSensors.show()
            except:
                pass

            # Функция вызова окна Редактирования типа датчика
            def openedittypeofsensors():
                # Инициализация окна Редактирования типа датчика
                try:
                    global EditTypeOfSensors
                    EditTypeOfSensors = QtWidgets.QMainWindow()
                    uiedittype = Ui_EditTypeOfSensors()
                    uiedittype.setupUi(EditTypeOfSensors)
                    purpose = uitype.tableWidget.item(uitype.tableWidget.currentRow(), 0).text()
                    type = uitype.tableWidget.item(uitype.tableWidget.currentRow(), 1).text()
                    volt = uitype.tableWidget.item(uitype.tableWidget.currentRow(), 2).text()
                    station = uitype.tableWidget.item(uitype.tableWidget.currentRow(), 3).text()
                    uiedittype.lineEdit.setText(purpose)
                    uiedittype.lineEdit_2.setText(type)
                    uiedittype.lineEdit_3.setText(volt)
                    uiedittype.lineEdit_4.setText(station)
                    EditTypeOfSensors.show()
                except:
                    pass

                # Функция подтверждения Редактирования типа датчика
                def okbutton():
                    uiedittype.okbutton(type, station)
                    uitype.loaddate(station)
                    EditTypeOfSensors.close()

                # Обработка сигнала нажатия кнопки ОК
                uiedittype.okButton.clicked.connect(okbutton)

            # Функция удаления Типа датчика
            def deletebutton():
                uitype.deletebutton()
                uitype.loaddate(station)

            # Функция вернуться назад
            def backbutton():
                TypeOfSensors.close()
                Station.show()

            # Функция вызова окна Добавления типа датчика
            def openaddtypeofsensors():
                # Инициализация окна Добавления типа датчика
                global AddTypeOfSensors
                AddTypeOfSensors = QtWidgets.QMainWindow()
                uiaddtype = Ui_AddTypeOfSensors()
                uiaddtype.setupUi(AddTypeOfSensors)
                uiaddtype.lineEdit_4.setText(station)
                AddTypeOfSensors.show()

                # Функция подтверждения Добавления типа датчика
                def okbutton():
                    uiaddtype.okbutton()
                    uitype.loaddate(station)
                    AddTypeOfSensors.close()

                # Обработка сигнала нажатия кнопки ОК
                uiaddtype.okButton.clicked.connect(okbutton)

            def purposefilter():
                uitype.purposefilter(station)

            def typefilter():
                uitype.typefilter(station)

            def voltfilter():
                uitype.voltfilter(station)

            def stationfilter():
                uitype.stationfilter(station)

            # Функция вызова окна Датчики
            def opensensors():
                # Инициализация окна датчики
                try:
                    global Sensors
                    Sensors = QtWidgets.QMainWindow()
                    uisens = Ui_Sensors()
                    uisens.setupUi(Sensors)
                    station = uitype.tableWidget.item(uitype.tableWidget.currentRow(), 3).text()
                    print(station)
                    type = uitype.tableWidget.item(uitype.tableWidget.currentRow(), 1).text()
                    print(type)
                    uisens.loaddata(station, type)
                    TypeOfSensors.close()
                    Sensors.show()
                except:
                    pass

                # Функция вызова окна Редактирования датчика
                def openeditsensors():
                    # Инициализация окна Редактирования датчика
                    try:
                        global EditSensors
                        EditSensors = QtWidgets.QMainWindow()
                        uieditsens = Ui_EditSensors()
                        uieditsens.setupUi(EditSensors)
                        serial = uisens.tableWidget.item(uisens.tableWidget.currentRow(), 0).text()
                        readings = uisens.tableWidget.item(uisens.tableWidget.currentRow(), 1).text()
                        normal = uisens.tableWidget.item(uisens.tableWidget.currentRow(), 2).text()
                        status = uisens.tableWidget.item(uisens.tableWidget.currentRow(), 3).text()
                        type = uisens.tableWidget.item(uisens.tableWidget.currentRow(), 4).text()
                        station = uisens.tableWidget.item(uisens.tableWidget.currentRow(), 5).text()
                        uieditsens.lineEdit.setText(serial)
                        uieditsens.lineEdit_2.setText(readings)
                        uieditsens.lineEdit_3.setText(normal)
                        uieditsens.lineEdit_4.setText(status)
                        uieditsens.lineEdit_5.setText(type)
                        uieditsens.lineEdit_6.setText(station)
                        EditSensors.show()
                    except:
                        pass

                    # Функция подтверждения Редактирования датчика
                    def okbutton():
                        uieditsens.okbutton(serial)
                        uisens.loaddata(station, type)
                        EditSensors.close()

                    # Обработка сигнала нажатия кнопки ОК
                    uieditsens.okButton.clicked.connect(okbutton)

                # Функция вернуться назад
                def backbutton():
                    Sensors.close()
                    TypeOfSensors.show()

                def serialfilter():
                    uisens.serialfilter(station, type)

                def readingsfilter():
                    uisens.readingsfilter(station, type)

                def normalfilter():
                    uisens.normalfilter(station, type)

                def statusfilter():
                    uisens.statusfilter(station, type)

                def typefilter():
                    uisens.typefilter(station, type)

                def stationfilter():
                    uisens.stationfilter(station, type)

                # Функция удалить запись класса Датчики
                def deletebutton():
                    uisens.deletebutton()
                    uisens.loaddata(station, type)

                # Функция вызова окна Добавления датчика
                def openaddsensors():
                    # Инициализация окна Добавления датчика
                    global AddSensors
                    AddSensors = QtWidgets.QMainWindow()
                    uiaddsens = Ui_AddSensors()
                    uiaddsens.setupUi(AddSensors)
                    uiaddsens.lineEdit_5.setText(type)
                    uiaddsens.lineEdit_6.setText(station)
                    AddSensors.show()

                    # Функция подтверждения Добавления датчика
                    def okbutton():
                        uiaddsens.okbutton()
                        uisens.loaddata(station, type)
                        AddSensors.close()

                    # Обработка сигнала нажатия кнопки ОК
                    uiaddsens.okButton.clicked.connect(okbutton)

                #Фукция формирования отчета
                def otchet():
                    uisens.otchet(station, type)

                # Обработка сигналов окна Датчики
                uisens.pushButton2.clicked.connect(otchet)
                uisens.AddButton.clicked.connect(openaddsensors)
                uisens.DeleteButton.clicked.connect(deletebutton)
                uisens.BackButton.clicked.connect(backbutton)
                uisens.editButton.clicked.connect(openeditsensors)
                uisens.lineEdit.textChanged.connect(serialfilter)
                uisens.lineEdit_2.textChanged.connect(readingsfilter)
                uisens.lineEdit_3.textChanged.connect(normalfilter)
                uisens.lineEdit_4.textChanged.connect(statusfilter)
                uisens.lineEdit_5.textChanged.connect(typefilter)
                uisens.lineEdit_6.textChanged.connect(stationfilter)

            # Обработка сигалов окна Тип датчиков
            uitype.pushButton3.clicked.connect(opensensors)
            uitype.AddButton.clicked.connect(openaddtypeofsensors)
            uitype.DeleteButton.clicked.connect(deletebutton)
            uitype.BackButton.clicked.connect(backbutton)
            uitype.EditButton.clicked.connect(openedittypeofsensors)
            uitype.lineEdit.textChanged.connect(purposefilter)
            uitype.lineEdit_2.textChanged.connect(typefilter)
            uitype.lineEdit_3.textChanged.connect(voltfilter)
            uitype.lineEdit_4.textChanged.connect(stationfilter)

        # Обработка сигналов окна Станции
        uistat.pushButton1.clicked.connect(opentypeofsensors)
        uistat.addButton.clicked.connect(openaddstation)
        uistat.BackButton.clicked.connect(backbutton)
        uistat.DeleteButton.clicked.connect(deletebuton)
        uistat.EditButton.clicked.connect(openeditstation)
        uistat.lineEdit.textChanged.connect(stationfilter)
        uistat.lineEdit_2.textChanged.connect(linefilter)
        uistat.lineEdit_3.textChanged.connect(coordinatesfilter)

    # Обработка сигналов стартового окна
    uistart.StationButton.clicked.connect(openstations)
    uistart.EmpoyeesButton.clicked.connect(openemployees)

sys.exit(app.exec_())