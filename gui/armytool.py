import sys

from collections import deque
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, \
    QLabel, QVBoxLayout, QHBoxLayout, QWidget, qApp, QListView, QSplitter, QStackedWidget, QFrame, QGroupBox, \
    QFormLayout, QLineEdit, QComboBox, QSpinBox, QTreeView

from rester import Rester, APIEnum


class EditScreen(QWidget):

    def __init__(self, rester: Rester):
        super(EditScreen, self).__init__()
        self.rester = rester
        self.tree = QTreeView()
        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name'])
        self.tree.header().setDefaultSectionSize(200)
        self.tree.setModel(self.model)
        self.import_data()
        self.tree.expandAll()
        self.tree.setSortingEnabled(True)

        self.init_ui()

    def init_ui(self):
        hbox = QHBoxLayout()

        splitter = QSplitter()
        splitter.addWidget(self.tree)

        form_group_box = QGroupBox()
        layout = QFormLayout()
        layout.addRow(QLabel('Name:'), QLineEdit())
        layout.addRow(QLabel('Model Type:'), QComboBox())
        layout.addRow(QLabel('Point Cost:'), QSpinBox())
        form_group_box.setLayout(layout)

        splitter.addWidget(form_group_box)

        hbox.addWidget(splitter)

        self.setLayout(hbox)

    def import_data(self, root=None):

        self.data = self.rester.list_request([APIEnum.MODEL, APIEnum.UNIT])

        self.model.setRowCount(0)
        if root is None:
            root = self.model.invisibleRootItem()
        for key, value_list in self.data.items():
            parent = QStandardItem(key)
            root.appendRow([parent])
            for value in value_list:
                for k in value.keys():
                    parent.appendRow([QStandardItem(k)])


class ArmyTool(QMainWindow):

    def __init__(self):
        super(ArmyTool, self).__init__()
        self.rester = Rester()
        self.init_ui()

    def init_ui(self):
        button = QPushButton('Edit Database')

        button.clicked.connect(self.switch_to_edit_screen)

        widget = QWidget()
        widget.resize(500, 500)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        widget.setLayout(vbox)

        self.setCentralWidget(EditScreen(self.rester))

        self.setGeometry(200, 200, 1024, 768)
        self.setWindowTitle('Armytool')
        self.show()

    def switch_to_edit_screen(self):
        edit = EditScreen(self.rester)
        self.setCentralWidget(edit)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    armytool = ArmyTool()
    sys.exit(app.exec_())
