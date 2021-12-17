from PyQt5 import uic
from PyQt5.QtWidgets import *

from Manager import MANAGER


class PassManagerGUI(QMainWindow):
    def __init__(self):
        super(PassManagerGUI, self).__init__()
        self.manager = MANAGER()
        uic.loadUi("passManagerUi.ui", self)
        self.show()

        self.login_status = [False, 0]

        # creation and authentication buttons
        self.createButton.clicked.connect(self.create_new_manager)
        self.unlockButton.clicked.connect(self.unlock_all)

        # DB action buttons
        self.insertButton.clicked.connect(self.insert_to_db)
        self.updateButton.clicked.connect(self.update_db_data)
        self.deleteButton.clicked.connect(self.delete_db_data)
        self.dbLoadButton.clicked.connect(self.fill_table_data)


    def create_new_manager(self):
        self.manager.format_db()
        self.manager.entry_new_data('master_pwd', self.createInput.text())
        self.login_status = [True, self.createInput.text()]
        self.UserToolbox.setEnabled(True)
        self.dbLoadButton.setEnabled(True)
        self.DbTableWidget.setEnabled(True)
        
    def unlock_all(self):
        if self.manager.db.is_master_pwd(self.unlockInput.text()):
            self.login_status = [True, self.unlockInput.text()]
            self.UserToolbox.setEnabled(True)
            self.dbLoadButton.setEnabled(True)
            self.DbTableWidget.setEnabled(True)
            
    def insert_to_db(self):
        if self.login_status[0]:
            self.manager.entry_new_data(self.insertAppInput.text(), self.insertPassInput.text())

    def update_db_data(self):
        if self.login_status[0]:
            self.manager.update_entry_data(self.login_status[1], self.updateAppInput.text(), self.updatePassInput.text())

    def delete_db_data(self):
        if self.login_status[0]:
            self.manager.del_entry_data(self.login_status[1], self.deleteAppInput.text())

    def fill_table_data(self):
        if self.login_status[0]:
            data = self.manager.read_entry_data(self.login_status[1])
            row_idx = 1
            self.DbTableWidget.setRowCount(len(data.keys())+1)
            for key in data.keys():
                self.DbTableWidget.setItem(row_idx, 0, QTableWidgetItem(str(key)))
                self.DbTableWidget.setItem(row_idx, 1, QTableWidgetItem(str(data[key])))
                row_idx += 1
        self.DbTableWidget.horizontalHeader().setStretchLastSection(True)
        self.DbTableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)



def main():
    app = QApplication([])
    window = PassManagerGUI()
    app.exec_()


if __name__ == "__main__":
    main()