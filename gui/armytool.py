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
        self.data = self.rester.list_request(list(APIEnum))
        self.import_data(self.data)
        self.tree.expandAll()
        self.tree.setSortingEnabled(True)

        self.init_ui()

    def init_ui(self):
        hbox = QHBoxLayout()

        vbox = QVBoxLayout()
        left_layout = QFormLayout()
        tree_group_box = QGroupBox()
        self.search_field = QLineEdit()
        self.search_field.editingFinished.connect(self.search_field_changed)
        # self.search_field.textEdited.connect(self.search_field_changed)
        left_layout.addRow(QLabel('Search:'), self.search_field)
        tree_group_box.setLayout(left_layout)

        vbox.addWidget(tree_group_box)
        vbox.addWidget(self.tree)

        gb = QGroupBox()
        gb.setLayout(vbox)

        splitter = QSplitter()
        splitter.addWidget(gb)

        form_group_box = QGroupBox()
        layout = QFormLayout()
        layout.addRow(QLabel('Name:'), QLineEdit())
        layout.addRow(QLabel('Model Type:'), QComboBox())
        layout.addRow(QLabel('Point Cost:'), QSpinBox())
        form_group_box.setLayout(layout)

        splitter.addWidget(form_group_box)

        hbox.addWidget(splitter)

        self.setLayout(hbox)

    def import_data(self, data, root=None):

        self.model.setRowCount(0)
        if root is None:
            root = self.model.invisibleRootItem()
        for key, value_list in data.items():
            parent = QStandardItem(key)
            parent.setEditable(False)
            root.appendRow([parent])
            for value in value_list:
                for k in value.keys():
                    parent.appendRow([QStandardItem(k)])

    def search_field_changed(self):
        term = self.search_field.text()
        print(term)
        data = {}
        for key, value_list in self.data.items():
            li = []
            for value in value_list:
                for k in value.keys():
                    if term in k:
                        li.append(value)
            data[key] = li

        self.import_data(data)


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
