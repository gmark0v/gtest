from PyQt5.QtWidgets import QApplication 
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
#прога
test_proga = QApplication([])
wind_os = QWidget()
wind_os.resize(480, 240)
#объекты
pov1 = QPushButton(wind_os)
#текста
pov1.setText("Проверка1")
#конец
wind_os.show()
test_proga.exec_()