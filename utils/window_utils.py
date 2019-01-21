from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QDialog
from PyQt5.QtGui import QPixmap


SCREEN_RESOLUTION = {}


def export_file(window, export_data):
    try:
        formats = "Excel (*.xls);;CSV (*.csv)"
        file_dailog = QtWidgets.QFileDialog(window)
        file = file_dailog.getSaveFileName(window, "Save File", filter=formats)
        file_path = file[0]
        file_format = file[1]
        if file_path:
            import pandas as pd
            if type(export_data) == list:
                df = pd.DataFrame(export_data)
            else:
                df = pd.DataFrame({k: ([v] if type(v) is int else v) for k, v in export_data.items() })
            if file_format == 'Excel (*.xls)':
                file_extension = '.xls'
                if not file_path.endswith(file_extension):
                    file_path += file_extension
                writer = pd.ExcelWriter(file_path)
                df.to_excel(writer, 'Sheet1', index=False)
                writer.save()
            elif file_format == 'CSV (*.csv)':
                file_extension = '.csv'
                if not file_path.endswith(file_extension):
                    file_path += file_extension
                    df.to_csv(file_path, sep='\t', encoding='utf-8')
            QtWidgets.QMessageBox.about(window, "info", "Exported data successfully !!!")
    except Exception as ex:
        QtWidgets.QMessageBox.about(window, "Error", str(ex))


def get_resolution_ratio(win_width, win_height):
    width = SCREEN_RESOLUTION["width"]
    height = SCREEN_RESOLUTION["height"]
    width_ratio: float = width / win_width - 0.2
    height_ratio: float = height / win_height - 0.2
    return width_ratio, height_ratio


def ImageWindow(win, image_path=None):
    self = QDialog(parent=win)
    self.title = 'Attachment'
    self.left = 10
    self.top = 10
    self.width = 600
    self.height = 450

    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)

    # Create widget
    label = QLabel(self)
    pixmap = QPixmap(image_path)
    label.setPixmap(pixmap)
    self.resize(pixmap.width(), pixmap.height())

    self.show()
