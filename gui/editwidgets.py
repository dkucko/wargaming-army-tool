from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QGroupBox, QFormLayout, QVBoxLayout, QLineEdit, QSpinBox, QLabel, QPushButton, \
    QComboBox


class EditWidget(QGroupBox):

    def __init__(self):
        super(EditWidget, self).__init__()
        self.form_group_vbox = QVBoxLayout()
        self.form_group_layout = QFormLayout()
        self.saveButton = QPushButton('Save')

    def init_ui(self):
        self.form_group_layout.addRow(self.saveButton)
        self.form_group_vbox.addLayout(self.form_group_layout)
        self.setLayout(self.form_group_vbox)

    def load_data(self, data):
        raise NotImplementedError


class EquipmentEdit(EditWidget):

    def __init__(self):
        super(EquipmentEdit, self).__init__()
        self.name_edit = QLineEdit()
        self.point_cost_edit = QSpinBox()
        self.point_cost_edit.setMaximum(9999)

        self.form_group_layout.addRow(QLabel('Name:'), self.name_edit)
        self.form_group_layout.addRow(QLabel('Point Cost:'), self.point_cost_edit)
        self.init_ui()

    def load_data(self, data):
        self.name_edit.setText(str(data['name']))
        self.point_cost_edit.setValue(data['point_cost'])


class ModelEdit(EditWidget):

    def __init__(self, data):
        super(ModelEdit, self).__init__()
        self.name_edit = QLineEdit()
        self.equipment_edit_list = [QComboBox()]
        self.items = [e['name'] for e in data['Equipment']]
        self.equipment_edit_list[0].addItems(self.items)

        self.form_group_layout.addRow(QLabel('Name:'), self.name_edit)
        for ee in self.equipment_edit_list:
            self.form_group_layout.addRow(QLabel('Equipment:'), ee)

    def load_data(self, data):
        self.name_edit.setText(str(data['name']))
        for i, e in enumerate(data['equipment']):
            try:
                self.equipment_edit_list[i]
            except IndexError:
                cb = QComboBox()
                cb.addItems(self.items)
                self.equipment_edit_list.append(cb)
                self.form_group_layout.addRow(QLabel('Add. Equipment:'), cb)
            index = self.equipment_edit_list[i].findText(e)
            if index >= 0:
                self.equipment_edit_list[i].setCurrentIndex(index)

        self.init_ui()


def get_edit_widget(typ, data):
    if typ == 'Models':
        return ModelEdit(data)
    elif typ == 'Equipment':
        return EquipmentEdit()
