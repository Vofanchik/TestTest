from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QLineEdit, QDialogButtonBox, QPushButton, QTableWidgetItem, QLabel

from UI_files.MainWindow import Ui_MainWindow
tests = []


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.CreateTestButton.clicked.connect(self.on_create_test_button)

    def on_create_test_button(self):
        dlg = QDialog()
        dlg_layout = QtWidgets.QVBoxLayout()
        name = QLineEdit()
        dlg_layout.addWidget(name)
        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.accepted.connect(dlg.accept)
        buttonBox.rejected.connect(dlg.reject)
        dlg_layout.addWidget(buttonBox)
        dlg.setWindowTitle('Введите название теста')
        dlg.setLayout(dlg_layout)
        dlg.setGeometry(500, 500, 500, 50)

        if dlg.exec():
            tests.append(name.text())
            questions = self.add_questions()
            print(questions)
            self.update_table()

    def update_table(self):
        table = self.ui.tableAllTests
        table.setColumnCount(1)
        # table.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('Название'))
        table.horizontalHeader().setVisible(False)
        table.horizontalHeader().setStretchLastSection(True)
        for co, it in enumerate(tests):
            table.setRowCount(co + 1)
            table.setItem(co, 0, QTableWidgetItem(str(it)))

    def add_questions(self):
        def next_question():
            one_question = {'question': name.text(),
                            'variants': [i.text() for i in variants]}
            test_with_questions.append(one_question)
            name.clear()
            [i.clear() for i in variants]

        def add_variant():
            new_line = QLineEdit()
            dlg_layout.insertWidget(len(variants) + 3, new_line)
            variants.append(new_line)

        test_with_questions = []
        variants = []
        dlg = QDialog()
        dlg_layout = QtWidgets.QVBoxLayout()
        name = QLineEdit()
        dlg_layout.addWidget(QLabel('Вопрос'))
        dlg_layout.addWidget(name)
        next_button = QPushButton('Следующий')
        first_variant = QLineEdit()
        dlg_layout.addWidget(QLabel('Варианты'))
        dlg_layout.addWidget(first_variant)
        variants.append(first_variant)
        add_variant_button = QPushButton('Ещё вариант')
        dlg_layout.addWidget(add_variant_button)
        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.addButton(next_button, QDialogButtonBox.ActionRole)
        buttonBox.accepted.connect(lambda : [next_question(), dlg.close()])
        buttonBox.rejected.connect(dlg.reject)

        buttonBox.accepted.connect(next_question)
        add_variant_button.clicked.connect(add_variant)
        next_button.clicked.connect(next_question)
        dlg_layout.addWidget(buttonBox)
        dlg.setWindowTitle('Введите вопрос')
        dlg.setLayout(dlg_layout)
        dlg.setGeometry(500, 500, 500, 50)

        dlg.exec()
        with open("questions.txt", "w") as my_file:
            my_file.writelines(str(test_with_questions))
        return test_with_questions



