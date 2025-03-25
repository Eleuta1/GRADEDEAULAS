import sys
from PyQt5.QtWidgets import QApplication
from views.login_view import LoginView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = LoginView()
    janela.show()
    sys.exit(app.exec_())