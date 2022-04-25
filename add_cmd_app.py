from PySide2.QtWidgets import QApplication, QFileDialog
from PySide2.QtUiTools import QUiLoader

from CmdAppDatabase import add_to_file

"""
添加 cmd_apppath关联关系的界面
"""

class AddCmd_App:
    def __init__(self):
        self.ui = QUiLoader().load("./ui/add.ui")

        self.ui.pathButton.clicked.connect(self.open_file)
        self.ui.addButton.clicked.connect(self.add)


    # 选择文件
    def open_file(self):
        filePath = QFileDialog.getOpenFileName(self.ui)
        self.ui.pathEdit.setText(filePath[0])
        # print(type(filePath))
        # print(filePath)

    def add(self):
        cmd = self.ui.cmdText.text()
        exe_path = self.ui.pathEdit.text()
        # print(cmd, exe_path)
        add_to_file(cmd, exe_path)


app = QApplication([])
add = AddCmd_App()
add.ui.show()
app.exec_()
