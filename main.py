from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *

class Ui_Login(object):
    global cipher, p_cipher
    def Correct(self):
        global cipher, p_cipher
        cipher = ''
        p_cipher = ''
        def encryption(text):
            # Выбрать два простых различных числа
            p, q = 89, 107
            # Вычислить произведение
            n = p * q
            # Вычислить функцию Эйлера
            fi = (p - 1) * (q - 1)
            # Выбрать открытую экспоненту
            en = 3

            # Вычислить шифротекст
            def encrypt(val):
                cypher = (val ** en) % n
                return (cypher)

            # Итоговая функция шифрования
            def rsa_encrypt(text):
                global cipher,p_cipher
                global encrypte
                encrypte = []
                for i in range(len(text)):
                    encrypte.append(encrypt(ord(text[i])))
                return encrypte
            global cipher, p_cipher
            cipher = rsa_encrypt(text)
            cipher = ' '.join(map(str, cipher))
            p_cipher = rsa_encrypt(text)
            p_cipher = ' '.join(map(str, p_cipher))

        u_ind = 0
        p_ind = 0
        encryption(self.lineEdit.text())
        word = cipher

        with open(r'src/username.txt', 'r') as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                line = ('\n'.join(filter(bool, line.split('\n'))))
                u_ind += 1
                if (word == line):
                    self.u_ind = u_ind
                    break
                if ((self.lineEdit_2.text() == "") or (self.lineEdit.text() == "")):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Поле Username или Password не может быть пустым")
                    msg.setWindowTitle("Пустое поле")
                    msg.exec_()
                    break

        encryption(self.lineEdit_2.text())
        p_word = p_cipher

        with open(r'src/password.txt', 'r') as fp:
            # read all lines in a list
            p_lines = fp.readlines()
            for p_line in p_lines:
                p_line = ('\n'.join(filter(bool, p_line.split('\n'))))
                p_ind += 1
                if (p_word == p_line):
                    self.p_ind = p_ind

                    if self.p_ind == self.u_ind:
                        break

                if ((self.lineEdit_2.text() == "") or (self.lineEdit.text() == "")):
                    break

        try:
            if (p_word == p_line) and (word == line):
                print()
        except:
            line = ""
            p_line = ""
        if (p_word == p_line) and (word == line):
            if ((p_ind == u_ind) and ((p_ind or u_ind) != 0)):
                global Username
                Username = cipher
                LoginForm.close()
                LK.show()
                self.instance = Ui_LK()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(
                    "Вы успешно вошли")
                msg.setWindowTitle("Успешный вход")
                msg.exec_()
                li.label_12.setText("Username: " + ui.lineEdit.text())
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Такой Username или Password не существует")
                msg.setWindowTitle("Неправильные данные")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Такой Username или Password не существует")
            msg.setWindowTitle("Неправильные данные")
            msg.exec_()

    def encryptUser(self):
        global cipher,p_cipher
        cipher = ''
        p_cipher = ''
        def encryption(text):
            global cipher, p_cipher
            # Выбрать два простых различных числа
            p, q = 89, 107
            # Вычислить произведение
            n = p * q
            # Вычислить функцию Эйлера
            fi = (p - 1) * (q - 1)
            # Выбрать открытую экспоненту
            en = 3

            # Вычислить шифротекст
            def encrypt(val):
                cypher = (val ** en) % n
                return (cypher)

            # Итоговая функция шифрования
            def rsa_encrypt(text):
                global encrypte
                encrypte = []
                for i in range(len(text)):
                    encrypte.append(encrypt(ord(text[i])))
                return encrypte
            cipher = rsa_encrypt(text)
            cipher = ' '.join(map(str, cipher))
            p_cipher = rsa_encrypt(text)
            p_cipher = ' '.join(map(str, p_cipher))
        encryption(self.lineEdit.text())
        word = cipher

        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "" :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(
                "Присутствуют пустые поля")
            msg.setWindowTitle("Неправильные данные")
            msg.exec_()
        else:
            with open(r'src/username.txt', 'r') as fp:
                # read all lines in a list
                lines = fp.readlines()
                for line in lines:
                    line = ('\n'.join(filter(bool, line.split('\n'))))
                    if word == line:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText(
                            "Такой пользователь уже существует")
                        msg.setWindowTitle("Неправильные данные")
                        msg.exec_()
                        break
                else:

                    with open("src/username.txt", 'a', encoding='utf-8') as file:
                        file.write(f'{cipher}\n')
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText("Вы успешно зарегистрировались")
                        msg.setWindowTitle("Успешная регистрация")
                        msg.exec_()


            encryption(self.lineEdit_2.text())
            p_word = ' '.join(map(str, p_cipher))
            with open(r'src/password.txt', 'r') as fp_file:
                # read all lines in a list
                p_lines = fp_file.readlines()
                for p_line in p_lines:
                    p_line = ('\n'.join(filter(bool, p_line.split('\n'))))
                    if word == line or word == "" or self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
                        break;
                else:

                    with open("src/password.txt", 'a', encoding='utf-8') as p_file:
                        p_file.write(f'{p_cipher}\n')
            return cipher



    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(1120, 880)
        LoginForm.setStyleSheet("background-color: rgb(163, 170, 27);\n"
"border-radius: 10px;")
        self.label = QtWidgets.QLabel(LoginForm)
        self.label.setGeometry(QtCore.QRect(530, 130, 91, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("src/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(LoginForm)
        self.frame.setGeometry(QtCore.QRect(280, 270, 600, 511))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(90, 50, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setMouseTracking(False)
        self.label_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setAcceptDrops(False)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setIndent(25)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(90, 160, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setStyleSheet("background-color: rgb(204, 204, 204);\n"
"padding-left: 8px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 220, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_2.setStyleSheet("background-color: rgb(204, 204, 204);\n"
"padding-left: 8px;\n"
"\n"
"")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 370, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(211, 155, 12);")
        self.pushButton.setObjectName("pushButton")
#################################Button Event#######################
        self.pushButton.clicked.connect(self.encryptUser)
####################################################################
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 300, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(211, 155, 12);")
        self.pushButton_2.setObjectName("pushButton_2")
#################################Button Event#######################
        self.pushButton_2.clicked.connect(self.Correct)
####################################################################
        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "LoginForm"))
        self.label_2.setText(_translate("LoginForm", "    Авторизация"))
        self.lineEdit.setPlaceholderText(_translate("LoginForm", "Имя пользователя"))
        self.lineEdit_2.setPlaceholderText(_translate("LoginForm", "Пароль"))
        self.pushButton.setText(_translate("LoginForm", "Зарегистрироваться"))
        self.pushButton_2.setText(_translate("LoginForm", "Войти"))

############################Другой класс###########################################

class Ui_LK(object):
    global vvod, vivod,vv
    def enc(self):
        global vvod, vivod,vv
        def encryption(text):
            global vvod, vivod,vv
            # Выбрать два простых различных числа
            p, q = 89, 107
            # Вычислить произведение
            n = p * q
            # Вычислить функцию Эйлера
            fi = (p - 1) * (q - 1)
            # Выбрать открытую экспоненту
            en = 3

            # Вычислить секретную экспоненту
            def dec_key(en):
                i = 2
                while i < 20:
                    formula = (1 + fi * i) % en
                    dec = int((1 + fi * i) / en)
                    if (formula == 0 and dec != en):
                        return (dec)
                    i = i + 1

            dec = dec_key(en)

            # Вычислить шифротекст
            def encrypt(val):
                cypher = (val ** en) % n
                return (cypher)

            # Вычислить исходное сообщение
            def decrypt(val):
                decr = (val ** dec) % n
                return (decr)

            # Итоговая функция шифрования
            def rsa_encrypt(text):
                global encrypte
                encrypte = []
                for i in range(len(text)):
                    encrypte.append(encrypt(ord(text[i])))
                return encrypte

            # Итоговая функция дешифрования
            def rsa_decrypt(encrypt_result):
                decrypte = []
                for i in range(len(encrypt_result)):
                    decrypte.append(chr(decrypt(encrypte[i])))
                decrypte = ''.join(decrypte)
                return decrypte

            vvod = rsa_encrypt(text)
            vvod = ' '.join(map(str, vvod))
            vv = rsa_encrypt(text)

        encryption(self.lineEdit.text())
        self.lineEdit_2.setText(vvod)
    def dec(self):
        global vvod, vivod,vv
        def encryption(text):
            global vvod, vivod,vv
            # Выбрать два простых различных числа
            p, q = 89, 107
            # Вычислить произведение
            n = p * q
            # Вычислить функцию Эйлера
            fi = (p - 1) * (q - 1)
            # Выбрать открытую экспоненту
            en = 3

            # Вычислить секретную экспоненту
            def dec_key(en):
                i = 2
                while i < 20:
                    formula = (1 + fi * i) % en
                    dec = int((1 + fi * i) / en)
                    if (formula == 0 and dec != en):
                        return (dec)
                    i = i + 1

            dec = dec_key(en)

            # Вычислить шифротекст
            def encrypt(val):
                cypher = (val ** en) % n
                return (cypher)

            # Вычислить исходное сообщение
            def decrypt(val):
                decr = (val ** dec) % n
                return (decr)

            # Итоговая функция шифрования
            def rsa_encrypt(text):
                global encrypte
                encrypte = []
                for i in range(len(text)):
                    encrypte.append(encrypt(ord(text[i])))
                return encrypte

            # Итоговая функция дешифрования
            def rsa_decrypt(encrypt_result):
                decrypte = []
                for i in range(len(encrypt_result)):
                    decrypte.append(chr(decrypt(encrypte[i])))
                decrypte = ''.join(decrypte)
                return decrypte

            vivod = rsa_decrypt(vv)
            vivod = ''.join(map(str, vivod))

        encryption(self.lineEdit.text())
        self.lineEdit_2.setText(vivod)

    def ToLoginForm(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Вы действительно хотите вернуться на главную страницу? Ваши данные не будут сохранены")
        msg.setWindowTitle("Выход")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
        result = msg.standardButton(msg.clickedButton())
        if result == 1024:
            LK.close()
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            LoginForm.show()
    def setupUi(self, LK):
        LK.setObjectName("LK")
        LK.resize(750, 550)
        LK.setStyleSheet("background-color: rgb(163, 170, 27);\n"
"\n"
"border-radius: 10px;")
        self.lineEdit_2 = QtWidgets.QLineEdit(LK)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 370, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(106, 94, 0);\n"
"padding-left: 8px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(LK)
        self.pushButton.setGeometry(QtCore.QRect(100, 230, 180, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
#######################################################################################################################################
        self.pushButton.clicked.connect(self.enc)
#######################################################################################################################################
        self.pushButton_2 = QtWidgets.QPushButton(LK)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 230, 180, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
#######################################################################################################################################
        self.pushButton_2.clicked.connect(self.dec)
#######################################################################################################################################
        self.lineEdit = QtWidgets.QLineEdit(LK)
        self.lineEdit.setGeometry(QtCore.QRect(50, 110, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(106, 94, 0);\n"
"padding-left: 8px;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(LK)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 490, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
##########################################################################################
        self.pushButton_3.clicked.connect(self.ToLoginForm)
##########################################################################################
        self.label_12 = QtWidgets.QLabel(LK)
        self.label_12.setGeometry(QtCore.QRect(50, 20, 701, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255,255,255);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(LK)
        self.label_13.setGeometry(QtCore.QRect(60, 320, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255,255,255);")
        self.label_13.setObjectName("label_13")

        self.retranslateUi(LK)
        QtCore.QMetaObject.connectSlotsByName(LK)

    def retranslateUi(self, LK):
        _translate = QtCore.QCoreApplication.translate
        LK.setWindowTitle(_translate("LK", "LK"))
        self.pushButton.setText(_translate("LK", "Зашифровать"))
        self.pushButton_2.setText(_translate("LK", "Расшифровать"))
        self.pushButton_3.setText(_translate("LK", "Выход"))
        self.label_12.setText(_translate("LK", "Username: "))
        self.label_13.setText(_translate("Dialog", "Результат:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QDialog()
    LK = QtWidgets.QDialog()
    ui = Ui_Login()
    li = Ui_LK()
    ui.setupUi(LoginForm)
    li.setupUi(LK)
    LoginForm.show()
    sys.exit(app.exec_())