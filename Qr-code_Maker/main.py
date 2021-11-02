import os
import webbrowser
import cv2
import qrcode
from PyQt5.QtWidgets import *
from PyQt5 import uic


class QrGUI(QMainWindow):
    def __init__(self):
        super(QrGUI, self).__init__()
        uic.loadUi("qecode_widget.ui", self)
        self.show()

        # constant var
        self.DOCS = 'https://github.com/FatinShadab/General-Python-Useages#readme'
        self.Source = 'https://github.com/FatinShadab/General-Python-Useages'

        # buttons
        self.create_button.clicked.connect(self.create_qr)
        self.sacn_button.clicked.connect(self.extract_qcode)
        self.actionclose.triggered.connect(exit)
        self.actiondocs.triggered.connect(lambda: self.user_help(self.DOCS))
        self.actionsource.triggered.connect(lambda: self.user_help(self.Source))

    def custom_error(self, error):
        msg = QMessageBox()
        msg.setText(f"{error}")
        msg.exec_()

    def user_help(self, link):
        webbrowser.open_new_tab(link)

    def create_qr(self):
        if len(self.save_to_area.text()) > 0:
            path = self.save_to_area.text()
        else:
            path = os.getcwd()
        if len(self.format_area.text()) > 0 and len(self.content_area.toPlainText()) > 0:
            qrcode.make(self.content_area.toPlainText()).save(f"{path}/QR-code.{self.format_area.text()}")
        else:
           self.custom_error("Fill up the Fields !")

    def save(self, data):

        img = cv2.imread(self.qrcode_path.text())
        det = cv2.QRCodeDetector()
        val, pts, st_code=det.detectAndDecode(img)

        data = val

        with open(f'QR-code-data.txt', 'w') as f:
            f.write(data)

    def extract_qcode(self):
        if len(self.qrcode_path.text()) > 0:
            try:
                img = cv2.imread(self.qrcode_path.text())
                det = cv2.QRCodeDetector()
                val, pts, st_code=det.detectAndDecode(img)
                
                # area customize
                self.output_area.setEnabled(True)
                self.output_area.setPlainText(val)

                # button customize
                self.save_button.setEnabled(True)
                self.save_button.clicked.connect(self.save)

                self.actionsave.setEnabled(True)
                self.actionsave.triggered.connect(self.save)
                
            except:
                self.custom_error(f"No Qr-Code found at {self.qrcode_path.text()} !")
        else:
            self.custom_error("Please provide the Qr-code path !")


def main():
    app = QApplication([])
    window = QrGUI()
    app.exec_()


if __name__ == "__main__":
    main()