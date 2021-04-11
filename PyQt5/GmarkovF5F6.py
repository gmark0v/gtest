from PyQt5.QtWidgets import QApplication 
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QListWidget
import json
#
test_proga = QApplication([])
wind_os = QWidget()
wind_os.resize(1280, 720)
wind_os.setWindowTitle("Заметочки!")
#
#p1 = QPushButton(wind_os)
#p1.setText("Сохранить")
#p1.move(10,310)
#p2 = QPushButton(wind_os)
#p2.setText("Загрузить")
#p2.move(100,310)
#
pov1 = QPushButton(wind_os)
pov2 = QPushButton(wind_os)
pov3 = QPushButton(wind_os)
pov4 = QPushButton(wind_os)
pov5 = QPushButton(wind_os)
pov6 = QPushButton(wind_os)
lis1 = QListWidget(wind_os)
lis2 = QListWidget(wind_os)
txt = QTextEdit(wind_os)
#
pov1.setText("Загрузить")
txt.move(100,50)
txt.setText("Проверка")
pov2.setText("Сохранить")
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
#
#w1 = QListWidget(wind_os)
#w1.move(10, 10)
#w1.resize(200,290)
#текстовое поле
#o0 = QTextEdit(wind_os)
#o0.resize(200,290)
#o0.move(230,10)
#with open ("prikolbac.txt", "a") as file:
    #coolguy = input("1: ")
    #notguy = input("2: ")
    #file.write("\n" +coolguy)
    #file.write("\n" +notguy)
    #data = file.read()
    #print(data)
#
def s6():
    global slovar
    s = lis1.currentItem().text()
    bb = txt.toPlainText()
    slovar[s]["text"] = bb
    with open ('prikol.json', "w", encoding="utf-8") as gson:
        json.dump(slovar,gson)
    print(slovar)
pov2.clicked.connect(s6)
#
def f5(item):
    s = item.text()
    if s in slovar:
        txt.setText(slovar[s]["text"])
lis1.itemClicked.connect(f5)
#
with open ('prikol.json', "r", encoding="utf-8") as gson:
    b = json.load(gson)
    slovar = dict(b)
#
for i in slovar:
    lis1.addItem(i)
#
wind_os.show()
test_proga.exec_()