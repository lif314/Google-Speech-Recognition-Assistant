from PySide2.QtWidgets import QFileDialog
from PySide2.QtUiTools import QUiLoader

from cmdAppDatabase import add_to_file

"""
添加 cmd_apppath关联关系的界面
"""

class AddView:
    def __init__(self):
        self.ui = QUiLoader().load("./ui/add.ui")

        self.ui.pathButton.clicked.connect(self.open_file)
        self.ui.addButton.clicked.connect(self.add)
        # self.ui.returnButton.clicked.connect(self.to_main_view)


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

    # def to_main_view(self):
    #     self.mainui = MainView()
    #     self.mainui.ui.show()
    #     self.ui.close()

# app = QApplication([])
# add = AddCmd_App()
# add.ui.show()
# app.exec_()
