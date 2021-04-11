from PyQt5.QtWidgets import QApplication 
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QListWidget
#
test_proga = QApplication([])
wind_os = QWidget()
wind_os.resize(350, 300)
wind_os.setWindowTitle("Блокнот")
#
pov1 = QPushButton(wind_os)
pov2 = QPushButton(wind_os)
#lis1 = QListWidget(wind_os)
txt = QTextEdit(wind_os)
#
pov1.setText("Загрузить")
txt.move(10,10)
txt.resize(210, 230)
txt.setText("Проверка")
pov2.setText("Сохранить")
pov1.move(10,250)
pov2.move(100,250)
#lis1.move(720,0)
#
wind_os.show()
test_proga.exec_()