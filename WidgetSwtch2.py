import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip, QMessageBox, QGroupBox, QButtonGroup
from PyQt5.QtWidgets import QWidget, QAction, QMenu, QMenuBar, QStatusBar, QLineEdit, QFormLayout
from PyQt5.QtWidgets import QSpinBox, QTextEdit, QLayout, QLabel, QBoxLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QCoreApplication, QDateTime
from PyQt5.QtGui import QIcon, QPixmap 

#***********************# Classes #***********************#

#class tax -- make update in taxi2
class taxi(): #formula = [A=P(1+r/n)^(nt)]
    def __init__(self,rate,prnc,ntime,time):  #make take in name and file n
        
        self.rate = rate #tax rate float
        self.prnc = prnc #amount in account
        self.ntime = ntime #how often is compounded
        self.time = time #how long has been in account

    def calculate(self):
        #formula = [A=P(1+r/n)^(nt)]
        self.rovern = self.rate/self.ntime
        self.power = self.ntime * self.time
        self.compAmount = self.prnc*pow((1+self.rovern),self.power) 

        return self.compAmount

    def prntToConsole(self):
        print(self.calculate)

#class vector -- like 3d vector update to 4d
class vector(): #ray make take in a line or make same thing a line could be vector not directed
    def __init__(self, i=0.0, j=0.0, k=0.0):
        self.xcomp = i
        self.ycomp = j
        self.zcomp = k

    # def __init__(self, scalar=0): #make self.setScalar retScalar
        # self.scalar = scalar

    def makeNeg(self):  
        self.xcomp *= -1
        self.ycomp *= -1
        self.zcomp *= -1
        return self

    def toStr(self):
        result = str(self.xcomp) + ',' + str(self.ycomp) + ',' + str(self.zcomp) 
        return result


#*************************# ***FUNCTIONS*** #*************************#

# add vectors # returns list of vector and vector string#  
def add(v1 = vector(), v2= vector()):                                   #@illCode**#
    v3 = vector(v1.xcomp+v2.xcomp , v1.ycomp+v2.ycomp , v1.zcomp+v2.zcomp)
    return v3

# cross product # returns list of vector and vector string#
def cross(v1 = vector(), v2 = vector()):
    xi = v1.ycomp*v2.zcomp-v1.zcomp*v2.ycomp
    yi = v1.xcomp*v2.zcomp-v1.zcomp*v2.xcomp
    zi = v1.xcomp*v2.ycomp-v1.ycomp*v2.xcomp 
                            #@illCode**#
    criss = vector(xi,yi,zi)
    return criss

# dot product # returns list of vector and vector string#       
def dot(v1 = vector(), v2 = vector()): 
    scalar = (v1.xcomp*v2.xcomp + v1.ycomp*v2.ycomp + v1.zcomp*v2.zcomp)#/(1-2)
    return scalar

# gcd or lcm flag < 0 #
def gcdOlcm(m,n,flag = 0):
    product = m*n 
    while (n != 0): 
        r = m%n
        m = n
        n = r
        if (r == 1): print('coprimes')
    return m
    
    if flag < 0:
        return product/m

#parse str to vector or number returns vector
def strParse2vec(tmp):
    a = tmp.split(',')
    print(a)
    i=0
    while i in range(len(a)):
        for num in a:
            num = float(num)
        i+=1

    if i == 3:
        v = vector(float(a[i-i]),float(a[i-2]),float(a[i-1]))
    elif i == 2:
        v = vector(float(a[i-i]),float(a[i-1]))
    elif i == 1:
        v = vector(float(a[i-i]))

    print(v,v.xcomp,v.toStr())
    return v


#***********************# Widgets #*******************#

#calcWidget class for normal or vec calculations
class CalcWid(QWidget):
    def __init__(self):
        super().__init__()
        self.createForm()
        self.createFormButtons()

        self.tite = "TAXI-free rides to the bank"
        self.top = 100
        self.left = 100
        self.wdth = 750
        self.hght = 750
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("pics\\artpics\LASTTYME.jpg"))
        self.label.setGeometry(0,0,1000,1000)
        
       #layout for upload default
        mainLay = QVBoxLayout()
                ######****make on StartWid*****###
        mainLay.addWidget(self.formBox)
        mainLay.addWidget(self.buttBox)
        self.setLayout(mainLay)

        self.consumList = []

    def createForm(self):
        self.formBox = QGroupBox("Wheel's UP")
        self.layout = QFormLayout()

       #boxes for setting values
        self.vbox = []
        self.v1Box = QLineEdit("0")
        self.v2Box = QLineEdit("0")

       #labels for the boxes respectively 
        vLabel = QLabel("Vector or Number for vec just put commas inbetween")
        v1Label = QLabel("first")
        v2Label = QLabel("second")
       #put labels and boxes on layout 
        self.layout.addRow(vLabel)
        self.layout.addRow(v1Label, self.v1Box)
        self.layout.addRow(v2Label, self.v2Box)

        self.formBox.setLayout(self.layout)

    def createFormButtons(self):
        self.buttBox = QGroupBox("Green means Go, Red for Reverse")
        bayout = QHBoxLayout()

        add = QPushButton(QIcon("pics\icons\greenStop.jpg"),"add")
        add.clicked.connect(self.addClick)

        sub = QPushButton(QIcon("pics\icons\stormtroopBW.jpg"),"subtract")
        sub.clicked.connect(self.subClick)

        crs = QPushButton(QIcon("pics\icons\greenStop.jpg"),"cross")
        crs.clicked.connect(self.crsClick)

        dot = QPushButton(QIcon("pics\icons\greenStop.jpg"),"dot")
        dot.clicked.connect(self.dotClick)

        bayout.addWidget(add)
        bayout.addWidget(sub)
        bayout.addWidget(crs)
        bayout.addWidget(dot)

        self.buttBox.setLayout(bayout)

    def addClick(self):
        flag = 'a'        
        tmpstr1 = self.v1Box.text()
        tmpstr2 = self.v2Box.text()
        V1 = strParse2vec(tmpstr1)
        V2 = strParse2vec(tmpstr2)
        result = add(V1,V2)
        print(result)
        added = result.toStr()
        addresult =QLineEdit(added)
        self.layout.addRow(QLabel("Aresult: "),addresult )
        print(addresult)
        self.updateStats()
            #make list for all old make object that hold list for 

    def subClick(self):  
        flag = 'b'        
        tmpstr1 = self.v1Box.text()
        tmpstr2 = self.v2Box.text()
        V1 = strParse2vec(tmpstr1)
        V2 = strParse2vec(tmpstr2)
        V2 = V2.makeNeg()
        result = add(V1,V2)
        subbed = result.toStr()
        subresult = QLineEdit(subbed)
        self.layout.addRow(QLabel("Bresult: "),subresult )
        print(subresult)
        self.updateStats()

    def crsClick(self):        
        flag = 'c'        
        tmpstr1 = self.v1Box.text()
        tmpstr2 = self.v2Box.text()
        v1 = strParse2vec(tmpstr1)
        v2 = strParse2vec(tmpstr2)
        crsresult =QLineEdit(cross(v1,v2).toStr())
        self.layout.addRow(QLabel("Cresult: "),crsresult )
        print(crsresult)
        self.updateStats()

            #make list for all old make object that hold list for 

    def dotClick(self):  
        flag = 'd'        
        tmpstr1 = self.v1Box.text()
        tmpstr2 = self.v2Box.text()
        v1 = strParse2vec(tmpstr1)
        v2 = strParse2vec(tmpstr2)
        dotresult =QLineEdit(str(dot(v1,v2)))
        self.layout.addRow(QLabel("Dresult: "),dotresult )
        print(dotresult)
        self.updateStats()

    def updateStats(self):
        date = QDateTime().currentDateTime().toLocalTime().toString()
        dateUtc = QDateTime().currentDateTimeUtc()
        stats = QStatusBar()
        stats.showMessage(date)

    def CloseApp(self):
        reply = QMessageBox.question(self,"Close Message", "Fuck Off or Nah",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit()

#taxWidget for tax ---make update in update form
class TaxWid(QWidget):
    def __init__(self):
        super().__init__()
        self.createForm()
        self.createFormButtons()

        self.tite = "TAXI-free rides to the bank"
        self.top = 100
        self.left = 100
        self.wdth = 750
        self.hght = 750
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("pics\icons\\namiBag2.jpg"))
        self.label.setGeometry(0,0,740,740)

       #layout for upload default
        mainLay = QVBoxLayout()
    ######****make on StartWid*****###
        mainLay.addWidget(self.formBox)
        mainLay.addWidget(self.buttBox)
        self.setLayout(mainLay)

        self.updateStats()

    def createForm(self):
        self.formBox = QGroupBox("Wheel's UP")
        self.layout = QFormLayout()

       #boxes for setting values
        self.rateR = QLineEdit("0")
        self.prncR = QLineEdit("0")
        self.nimeR = QSpinBox()
        self.nimeR.setRange(1,12) #made spinn box update range to 1,2,6,12
        self.timeR = QLineEdit("0")

       #labels for the boxes respectively 
        rateL = QLabel("Rate: ")
        prncL = QLabel("Principal: ")
        nimeL = QLabel("Componded: ")
        timeL = QLabel("Time: ")
       #put labels and boxes on layout 
        self.layout.addRow(rateL, self.rateR)
        self.layout.addRow(prncL, self.prncR)
        self.layout.addRow(nimeL, self.nimeR)
        self.layout.addRow(timeL, self.timeR)
       #putlayouton formbox
        self.formBox.setLayout(self.layout)

    def createFormButtons(self):
        self.buttBox = QGroupBox("Green means Go, Red for Reverse")
        bayout = QHBoxLayout()
        grn = QPushButton(QIcon("pics\icons\greenStop.jpg"),"Green")
        grn.clicked.connect(self.grnClick)

        red = QPushButton(QIcon("pics\icons\stormtroopBW.jpg"),"Red")
        red.clicked.connect(self.redClick)

        bayout.addWidget(grn)
        bayout.addWidget(red)

        self.buttBox.setLayout(bayout)

    def grnClick(self):
        
        self.rate = float(self.rateR.text()) #tax rate float
        self.prnc = float(self.prncR.text()) #amount in account
        self.nime = float(self.nimeR.text()) #how often is compounded
        self.time = float(self.timeR.text()) #how long has been in account

        self.tax = taxi(self.rate,self.prnc,self.nime,self.time)
        self.amount = QLineEdit(str(self.tax.calculate()))
        self.layout.addRow(QLabel("amount: "), self.amount)
        print(self.tax.calculate())
        self.updateStats()

            #make list for all old make object that hold list for 

    def redClick(self):  
        reply = QMessageBox.question(self,"EARASER", "Clear",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.rateR.clear()
            self.prncR.clear()
            self.nimeR.clear()
            self.timeR.clear() 
        self.updateStats()

    def updateStats(self):
        date = QDateTime().currentDateTime().toLocalTime().toString()
        dateUtc = QDateTime().currentDateTimeUtc()
        stats = QStatusBar(self)
        stats.showMessage(date)

    def CloseApp(self):
        reply = QMessageBox.question(self,"Close Message", "Fuck Off or Nah",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit()

#Main window -- make update in updateWindow
class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createForm()
        self.createButts()
        
        self.tite = "TAXI-free rides to the bank"
        self.top = 100
        self.left = 100
        self.wdth = 750
        self.hght = 750
    
        self.setWindowIcon(QIcon("pics\icons\\namiBag.jpg"))


     #make whole window into widget an swith widget
        mainLay = QVBoxLayout()
        mainLay.addWidget(self.formBox)
        mainLay.addWidget(self.buttBox)

        mainWid = QWidget()
        label = QLabel(mainWid)
        label.setPixmap(QPixmap("pics\\artpics\Shaka-Madlooks.jpg"))
        label.setGeometry(0,0,740,740)
        
        mainWid.setLayout(mainLay)
        self.setCentralWidget(mainWid)
        
    #make whole window into widget an swith widget
        self.startWin()
    
    def startWin(self):
     #menubar contains file
        mainMenu = self.menuBar() 
      #filemenu on main menu 
        fle = mainMenu.addMenu("File")
       #exit button for file menu
        exitButton = QAction(QIcon("pics\icons\\falconBW.jpg"), 'Exit',self)
        exitButton.setShortcut("Ctrl+E")
        exitButton.setStatusTip("Fuck Off")
        exitButton.triggered.connect(self.CloseApp)
        fle.addAction(exitButton)
      #helpmenu on main menu
        hlp = mainMenu.addMenu("Help")
       #date button on help menu
        datsButton = QAction(QIcon("pics\icons\\leiaBW.jpg"), 'DATE',self)
        datsButton.setShortcut("Ctrl+W")
        datsButton.setStatusTip("dats")
        datsButton.triggered.connect(self.updateStats)
        hlp.addAction(datsButton)

        vew = mainMenu.addMenu("View")
        backButton = QAction(QIcon("pics\icons\\leiaBW.jpg"), 'Back',self)
        backButton.setShortcut("Ctrl+b")
        backButton.setStatusTip("back to main")
        backButton.triggered.connect(self.backButtonClick)
        vew.addAction(backButton)
        
        
        abt = mainMenu.addMenu("About")
        tellAllbutt = QAction(QIcon("pics\icons\\leiaBW.jpg"), 'tell',self)
        tellAllbutt.setShortcut("Ctrl+R")
        tellAllbutt.setStatusTip("tell")
        tellAllbutt.triggered.connect(self.updateStats)
        abt.addAction(tellAllbutt)

        self.setWindowTitle(self.tite)
        self.setGeometry(self.top,self.left,self.wdth,self.hght)
        self.show()
        self.updateStats()

    def createForm(self):
        self.formBox = QGroupBox("Wheel's UP")
        self.layout = QFormLayout()

    def createButts(self):
     #buttonBox for putting on buttons
        self.buttBox = QGroupBox("buttons")

      #calculation butt for that widget
        calcButton = QPushButton(QIcon('pics\icons\BB8WB.jpg'),"calcit")
        calcButton.setShortcut("Ctrl+c")
        calcButton.setStatusTip("calculation")
        calcButton.clicked.connect(self.calcbuttonClicked)

      #tax butt for that widget
        taxButton = QPushButton(QIcon('pics\icons\BB8BW.jpg'),"taxit")
        taxButton.setShortcut("Ctrl+t")
        taxButton.setStatusTip("banking")
        taxButton.clicked.connect(self.taxbuttonClicked)

        layout = QHBoxLayout()
        layout.addWidget(taxButton)
        layout.addWidget(calcButton)
        self.buttBox.setLayout(layout)

    def updateStats(self):
        date = QDateTime().currentDateTime().toLocalTime().toString()
        dateUtc = QDateTime().currentDateTimeUtc()

        stats = self.statusBar()
        stats.showMessage(date)

    def calcbuttonClicked(self):
        calcWid = CalcWid()
        self.swtchMainWid(calcWid)
        self.updateStats()

    def taxbuttonClicked(self):
        taxWid = TaxWid()
        self.swtchMainWid(taxWid)
        self.updateStats()

    def backButtonClick(self):
        self.createForm()
        self.createButts()
        mainLay = QVBoxLayout()
        mainLay.addWidget(self.formBox)
        mainLay.addWidget(self.buttBox)


        mainWid = QWidget()
        label = QLabel(mainWid)
        label.setPixmap(QPixmap("pics\\artpics\Shaka-Madlooks.jpg"))
        label.setGeometry(0,0,740,740)

        mainWid.setLayout(mainLay)
        self.swtchMainWid(mainWid)
        

    def swtchMainWid(self,widget):
        self.setCentralWidget(widget)
        self.updateStats()

    def CloseApp(self):
        reply = QMessageBox.question(self,"Close Message", "Fuck Off or Nah",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit()




App = QApplication(sys.argv)
win = Win()
sys.exit(App.exec())            