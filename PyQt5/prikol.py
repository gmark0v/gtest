from PyQt5.QtWidgets import QApplication 
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtWidgets import QLabel
#прога
test_proga = QApplication([])
wind_os = QWidget()
wind_os.resize(1280, 720)
#объекты
pov1 = QPushButton(wind_os)
pov2 = QPushButton(wind_os)
pov3 = QPushButton(wind_os)
pov4 = QPushButton(wind_os)
pov5 = QPushButton(wind_os)
pov6 = QPushButton(wind_os)
lis1 = QListWidget(wind_os)
lis2 = QListWidget(wind_os)
txt = QLabel(wind_os)
#текста
pov1.setText("Проверка1")
txt.move(100,50)
txt.setText("проверка")
pov2.setText("Проверка2")
lis1.move(720,0)
pov3.setText("Проверка3")
pov1.move(850,210)
pov2.move(720,210)
pov3.move(785,255)
pov4.setText("Проверка4")
lis2.move(720,300)
pov5.setText("Проверка5")
pov4.move(850,510)
pov5.move(720,510)
pov6.move(785,555)
pov6.setText("Проверка6")

#конец
wind_os.show()
test_proga.exec_()