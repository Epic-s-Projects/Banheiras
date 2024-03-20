from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo de Abas com PyQt")

        # Cria o widget de abas
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Cria a primeira aba
        self.tab1 = QWidget()
        self.tabs.addTab(self.tab1, "Aba 1")
        layout1 = QVBoxLayout()
        label1 = QLabel("Conteúdo da Aba 1")
        layout1.addWidget(label1)
        self.tab1.setLayout(layout1)

        # Cria a segunda aba
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab2, "Aba 2")
        layout2 = QVBoxLayout()
        label2 = QLabel("Conteúdo da Aba 2")
        layout2.addWidget(label2)
        self.tab2.setLayout(layout2)

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
