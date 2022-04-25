from PySide2.QtWidgets import QApplication

from addView import AddView

from mainView import MainView


class AsrView:
    def __init__(self):
        self.addView = AddView()
        self.mainView = MainView()

        self.addView.ui.returnButton.clicked.connect(self.to_main)
        self.mainView.ui.addButton.clicked.connect(self.to_add)

    def to_main(self):
        self.addView.ui.close()
        self.mainView.ui.show()

    def to_add(self):
        self.addView.ui.show()




app = QApplication([])
view = AsrView()
view.mainView.ui.show()
app.exec_()
