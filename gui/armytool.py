import sys

from collections import deque
from PyQt5.QtCore import Qt, QItemSelectionModel, QItemSelection
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, \
    QLabel, QVBoxLayout, QHBoxLayout, QWidget, qApp, QListView, QSplitter, QStackedWidget, QFrame, QGroupBox, \
    QFormLayout, QLineEdit, QComboBox, QSpinBox, QTreeView, QAbstractItemView

from rester import Rester, APIEnum
from editwidgets import EditWidget, EquipmentEdit, get_edit_widget


class TreeItem(QStandardItem):

    def __init__(self, data: dict, typ: str, parent=False):
        super(TreeItem, self).__init__(data['name'])
        self.data_dict = data
        self.is_parent = parent
        self.typ = typ

    def get_data_dict(self):
        return self.data_dict


class EditScreen(QWidget):

    def __init__(self, rester: Rester):
        super(EditScreen, self).__init__()
        self.last_item_type = ''

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
        self.tree.setSortingEnabled(False)
        self.tree.expandAll()
        self.tree.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tree.selectionModel().selectionChanged.connect(self.item_selected)

        self.init_ui()

    def init_ui(self):
        hbox = QHBoxLayout()

        vbox = QVBoxLayout()
        left_layout = QFormLayout()
        tree_group_box = QGroupBox()
        self.search_field = QLineEdit()
        # self.search_field.editingFinished.connect(self.search_field_changed)
        self.search_field.textEdited.connect(self.search_field_changed)
        left_layout.addRow(QLabel('Search:'), self.search_field)
        tree_group_box.setLayout(left_layout)

        vbox.addWidget(tree_group_box)
        vbox.addWidget(self.tree)

        gb = QGroupBox()
        gb.setLayout(vbox)

        self.splitter = QSplitter()
        self.splitter.addWidget(gb)

        self.ew = EquipmentEdit()
        self.splitter.addWidget(self.ew)

        hbox.addWidget(self.splitter)

        self.setLayout(hbox)

    def import_data(self, data, root=None):

        self.model.setRowCount(0)
        if root is None:
            root = self.model.invisibleRootItem()
        for key, value_list in data.items():
            parent = TreeItem({'name': key}, '', parent=True)
            parent.setEditable(False)
            root.appendRow([parent])
            for value in value_list:
                parent.appendRow([TreeItem(value, key)])

    def search_field_changed(self):
        term = self.search_field.text()
        data = {}
        for key, value_list in self.data.items():
            li = []
            for value in value_list:
                for k in value.keys():
                    if term in k:
                        li.append(value)
            data[key] = li

        self.import_data(data)

    def item_selected(self):
        indexes = self.tree.selectedIndexes()
        selected = indexes[0]

        item = self.model.itemFromIndex(selected)

        if item.is_parent:
            return

        #if item.typ != self.last_item_type:
        self.ew.hide()
        self.ew.destroy()
        self.ew = get_edit_widget(item.typ, self.data)
        self.splitter.addWidget(self.ew)

        self.last_item_type = item.typ

        data_dict = item.get_data_dict()
        self.ew.load_data(data_dict)



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
