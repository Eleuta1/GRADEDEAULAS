import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'controllers')))

from PyQt5.QtCore import QCoreApplication, QEvent, Qt  # Certifique-se de que os imports estão corretos para QCoreApplication, QEvent, e Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from controllers.auth import AuthController  # Certifique-se de que está importando a classe AuthController corretamente
from views.main_window import MainWindow
from PyQt5.QtWidgets import QApplication

class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tela de Login")
        self.setFixedSize(800, 600)
        self.centralizar_janela()

        self.initUI()

    def initUI(self):
        widget = QWidget()
        layout = QVBoxLayout()

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)  # Ajusta o espaçamento entre os elementos do layout

        # Criando as labels e centralizando-as
        self.label_user = QLabel("Usuário:")
        self.label_user.setAlignment(Qt.AlignCenter)  # Centraliza a label
        self.input_user = QLineEdit()
        self.input_user.setFixedSize(250, 25)

        self.label_password = QLabel("Senha:")
        self.label_password.setAlignment(Qt.AlignCenter)  # Centraliza a label
        self.input_password = QLineEdit()
        self.input_password.setFixedSize(250, 25)
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setMaxLength(20)  # Limita a quantidade de caracteres permitidos no campo de senha

        self.btn_login = QPushButton("Entrar")
        self.btn_login.setFixedSize(100, 25)
        self.btn_login.clicked.connect(self.check_credentials)
        
        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_cancelar.setFixedSize(100, 25)  # Ajusta o tamanho do botão cancelar
        self.btn_cancelar.clicked.connect(self.close)

        # Centralizando as labels e os campos em layouts horizontais
        label_layout_user = QVBoxLayout()
        label_layout_user.addWidget(self.label_user)
        label_layout_user.setAlignment(Qt.AlignCenter)  # Centraliza a label

        label_layout_password = QVBoxLayout()
        label_layout_password.addWidget(self.label_password)
        label_layout_password.setAlignment(Qt.AlignCenter)  # Centraliza a label

        # Centralizando o botão "Entrar"
        button_layout_login = QVBoxLayout()
        button_layout_login.addWidget(self.btn_login)
        button_layout_login.setAlignment(Qt.AlignCenter)  # Centraliza o botão

        # Centralizando o botão "Cancelar"
        button_layout_cancel = QVBoxLayout()
        button_layout_cancel.addWidget(self.btn_cancelar)
        button_layout_cancel.setAlignment(Qt.AlignCenter)  # Centraliza o botão

        # Adicionando widgets ao layout principal
        layout.addLayout(label_layout_user)
        layout.addWidget(self.input_user)
        layout.addLayout(label_layout_password)
        layout.addWidget(self.input_password)
        layout.addLayout(button_layout_login)  # Adiciona o botão "Entrar" centralizado
        layout.addLayout(button_layout_cancel)  # Adiciona o botão "Cancelar" centralizado

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def centralizar_janela(self):
        janela = self.frameGeometry()
        centro_tela = QApplication.desktop().screenGeometry().center()
        janela.moveCenter(centro_tela)
        self.move(janela.topLeft())

    def check_credentials(self):
        usuario = self.input_user.text()
        senha = self.input_password.text()

        # Chamar a função de autenticação da classe AuthController
        if AuthController.autenticar_usuario(usuario, senha):
            self.sucesso_login()
        else:
            self.falha_login()

    def sucesso_login(self):
        QMessageBox.information(self, "Login", "Login bem-sucedido!")
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()  # Fechar a tela de login após login bem-sucedido (se desejado)

    def falha_login(self):
        QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos!")
        self.input_password.clear()  # Limpa o campo de senha para o próximo login
