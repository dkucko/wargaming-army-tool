from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QGroupBox, QFormLayout, QVBoxLayout, QLineEdit, QSpinBox, QLabel, QPushButton, \
    QComboBox, QHBoxLayout


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
        self.pk = data['id']


class ModelEdit(EditWidget):

    def __init__(self, data):
        super(ModelEdit, self).__init__()
        self.name_edit = QLineEdit()
        self.equipment_edit_list = [QComboBox()]
        self.items = [e['name'] for e in data['Equipment']]
        self.equipment_edit_list[0].addItems(self.items)

        self.form_group_layout.addRow(QLabel('Name:'), self.name_edit)
        addButton = QPushButton('Add Equipment Slot')
        addButton.clicked.connect(self.add_equipment)
        for ee in self.equipment_edit_list:
            self.form_group_layout.addRow(QLabel('Equipment:'), ee)
        # TODO: Find better position for button
        self.form_group_layout.addRow(QLabel(), addButton)

    def load_data(self, data):
        self.name_edit.setText(str(data['name']))
        self.pk = data['id']
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

    def add_equipment(self):
        cb = QComboBox()
        cb.addItems(self.items)
        self.equipment_edit_list.append(cb)
        index = self.form_group_layout.rowCount() - 2
        self.form_group_layout.insertRow(index, QLabel('Add. Equipment:'), cb)


class UnitEdit(EditWidget):

    def __init__(self, data):
        super(UnitEdit, self).__init__()
        self.name_edit = QLineEdit()
        self.model_edit_list = [(QComboBox(), QSpinBox())]
        self.unit_type_edit = QComboBox()
        self.might_edit = QSpinBox()
        self.unit_types = [ut['name'] for ut in data['Unit types']]
        self.unit_type_edit.addItems(self.unit_types)
        self.items = [m['name'] for m in data['Models']]
        self.model_edit_list[0][0].addItems(self.items)
        add_button = QPushButton('Add Model')
        add_button.clicked.connect(self.add_model)

        self.form_group_layout.addRow(QLabel('Name:'), self.name_edit)
        self.form_group_layout.addRow(QLabel('Unit type:'), self.unit_type_edit)
        self.form_group_layout.addRow(QLabel('Might:'), self.might_edit)
        for cb, sb in self.model_edit_list:
            hbox = QHBoxLayout()
            hbox.addWidget(cb)
            hbox.addWidget(sb)
            self.form_group_layout.addRow(QLabel('Model:'), hbox)
        self.form_group_layout.addRow(QLabel(), add_button)

    def load_data(self, data):
        self.pk = data['id']
        self.name_edit.setText(data['name'])
        self.might_edit.setValue(data['might'])
        ut_index = self.unit_type_edit.findText(data['unit_type'])
        if ut_index >= 0:
            self.unit_type_edit.setCurrentIndex(ut_index)
        for i, v in enumerate(data['models']):
            m, c = v
            try:
                self.model_edit_list[i]
            except IndexError:
                cb = QComboBox()
                cb.addItems(self.items)
                sb = QSpinBox()
                self.model_edit_list.append((cb, sb))
                hbox = QHBoxLayout()
                hbox.addWidget(cb)
                hbox.addWidget(sb)
                self.form_group_layout.addRow(QLabel('Model:'), hbox)
            index = self.model_edit_list[i][0].findText(m)
            if index >= 0:
                self.model_edit_list[i][0].setCurrentIndex(index)
            self.model_edit_list[i][1].setValue(c)

        self.init_ui()

    def add_model(self):
        cb = QComboBox()
        cb.addItems(self.items)
        sb = QSpinBox()
        self.model_edit_list.append((cb, sb))
        hbox = QHBoxLayout()
        hbox.addWidget(cb)
        hbox.addWidget(sb)
        self.form_group_layout.insertRow(self.form_group_layout.rowCount() - 2, QLabel('Model:'), hbox)


def get_edit_widget(typ, data):
    if typ == 'Models':
        return ModelEdit(data)
    elif typ == 'Equipment' or typ == 'Model types':
        return EquipmentEdit()
    elif typ == 'Units':
        return UnitEdit(data)
