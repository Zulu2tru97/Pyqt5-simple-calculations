import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip, QMessageBox, QGroupBox, QButtonGroup
from PyQt5.QtWidgets import QWidget, QAction, QMenu, QMenuBar, QStatusBar, QLineEdit, QFormLayout
from PyQt5.QtWidgets import QSpinBox, QTextEdit, QLayout, QLabel, QBoxLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QCoreApplication, QDateTime
from PyQt5.QtGui import QIcon, QPixmap 
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NT2
from matplotlib.figure import Figure
from mpl_toolkits import mplot3d

#***********************# Classes #***********************#

#class vector -- like 3d vector update to 4d
class vector(): #ray make take in a line or make same thing a line could be vector not directed
    def __init__(self, i=0.0, j=0.0, k=0.0):
        self.xcomp = np.array([0,i])
        self.ycomp = np.array([0,j])
        self.zcomp = np.array([0,k])
        
        self.Comp = [self.xcomp,self.ycomp,self.zcomp]
    # def __init__(self, scalar=0): #make self.setScalar retScalar
        # self.scalar = scalar

    def makeNeg(self):  
        self.xcomp *= -1
        self.ycomp *= -1
        self.zcomp *= -1
        return self

    def toStr(self):
        result = str(self.xcomp[1]) + ',' + str(self.ycomp[1]) + ',' + str(self.zcomp[1]) 
        return result

class morphEius():
    def __init__(self):
        super().__init__()

#*************************# ***FUNCTIONS*** #*************************#

# add vectors # returns list of vector and vector string#  
def add(v1 = vector(), v2= vector()):                                   #@illCode**#
    v3 = vector(v1.xcomp[1]+v2.xcomp[1] , v1.ycomp[1]+v2.ycomp[1] , v1.zcomp[1]+v2.zcomp[1])
    return v3

# cross product # returns list of vector and vector string#
def cross(v1 = vector(), v2 = vector()):
    xi = v1.ycomp[1]*v2.zcomp[1]-v1.zcomp[1]*v2.ycomp[1]
    yi = v1.zcomp[1]*v2.xcomp[1]-v1.xcomp[1]*v2.zcomp[1]
    zi = v1.xcomp[1]*v2.ycomp[1]-v1.ycomp[1]*v2.xcomp[1] 
                            #@illCode**#
    criss = vector(xi,yi,zi)
    return criss

# dot product # returns list of vector and vector string#       
def dot(v1 = vector(), v2 = vector()): 
    scalar = vector(v1.xcomp[1]*v2.xcomp[1] + v1.ycomp[1]*v2.ycomp[1] + v1.zcomp[1]*v2.zcomp[1])#/(1-2)
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

    print(v,v.xcomp[1],v.toStr())
    return v


#***********************# Widgets #*******************#

#canvas figure canvas for matplotlib
class Canvas(FigureCanvas):
    def __init__(self,parent=None ,width=5,height=5,dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.ax = self.figure.add_subplot(111, projection = '3d')
        _ = self.ax.set_xlabel('X-SIDE')
        _ = self.ax.set_ylabel('Y-LIED')
        _ = self.ax.set_zlabel('Z-RIDE')
        
    #/****** Make array of differnt x's ys etc...******/

        # self.plot()


    def plot(self,X=np.zeros(2),Y=np.zeros(2),Z =np.zeros(2),color = 'red',legend = 'vector'):
        # self.update()
        self.ax.plot3D(X,Y,Z,color = color,label = legend)
        self.ax.legend()

    def plotSurf(self,X=np.zeros(2),Y=np.zeros(2),Z =np.zeros(2),color = 'red',legend = 'vector'):
        # self.update()
        self.ax.plot_Surface(X,Y,Z,color = color, label = legend)

    def clear(self):
        self.ax = self.figure.add_subplot(111, projection = '3d')

    
        
#calcWidget class for normal or vec calculations
class CalcWid(QWidget):
    def __init__(self):
        super().__init__()
        self.createForm()
        self.createFormButtons()

        self.tite = "TAXI-free rides to the bank"
        self.top = 100
        self.left = 100
        self.wdth = 900
        self.hght = 900
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
       #canvas for matplot lib
        self.canvas = Canvas(self)
        tb = NT2(self.canvas,self)
        self.layout.addWidget(tb)
        self.layout.addRow(self.canvas)

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
        addresult =QLineEdit(added+'>')
        self.layout.addRow(QLabel("Aresult: <"),addresult )
        print(addresult)

       #draw results on canvas
        self.canvas.plot(V1.xcomp,V1.ycomp,V1.zcomp,'orange','first')
        self.canvas.plot(V2.xcomp,V2.ycomp,V2.zcomp,'blue','second')
        self.canvas.plot(result.xcomp,result.ycomp,result.zcomp,'red','add <'+added + '>')

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
        subresult = QLineEdit('<'+ subbed+'>')
        self.layout.addRow(QLabel("Bresult: "),subresult)
        print(subresult)

        #draw results on canvas 
        self.canvas.plot(V1.xcomp,V1.ycomp,V1.zcomp,'orange','first')
        self.canvas.plot(V2.xcomp,V2.ycomp,V2.zcomp,'blue','second')
        self.canvas.plot(result.xcomp,result.ycomp,result.zcomp,'green','sub <'+subbed+'>')

        self.updateStats()

    def crsClick(self):        
        flag = 'c'        
        tmpstr1 = self.v1Box.text()
        tmpstr2 = self.v2Box.text()
        V1 = strParse2vec(tmpstr1)
        V2 = strParse2vec(tmpstr2)
        result = cross(V1,V2)
        crsresult = QLineEdit('<'+ result.toStr() + '>')
        self.layout.addRow(QLabel("Cresult: "),crsresult)
        print(crsresult)


       #draw results on canvas
        self.canvas.plot(V1.xcomp,V1.ycomp,V1.zcomp,'orange','first')
        self.canvas.plot(V2.xcomp,V2.ycomp,V2.zcomp,'blue','second')
        self.canvas.plot(result.xcomp,result.ycomp,result.zcomp,'red','cross <'+result.toStr())


        self.updateStats()

            #make list for all old make object that hold list for 

    def dotClick(self):  
        flag = 'd'        
        tmpstr1 = self.v1Box.text()
        tmpstr2 = self.v2Box.text()
        V1 = strParse2vec(tmpstr1)
        V2 = strParse2vec(tmpstr2)
        result = dot(V1,V2)
        dotresult =QLineEdit('<'+ str(result.xcomp[1])+ '>')
        self.layout.addRow(QLabel("Dresult: "),dotresult)
        print(dotresult)

       #draw results on canvas
        # self.canvas.ax.plot3D(V1.xcomp,V1.ycomp,V1.zcomp)
        self.canvas.plot(V1.xcomp,V1.ycomp,V1.zcomp,'orange','first')
        self.canvas.plot(V2.xcomp,V2.ycomp,V2.zcomp,'blue','second')
        self.canvas.plot(result.xcomp,result.ycomp,result.zcomp,'red','dot <'+result.toStr()+'>')


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

#Main window -- make update in updateWindow
class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createForm()
        self.createButts()
        
        self.tite = "TAXI-free rides to the bank"
        self.top = 100
        self.left = 100
        self.wdth = 900
        self.hght = 900
    
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
 #/**********************Reset Please 2 mainwid and Change taxWid to surfWid*/ 
        calwid = CalcWid()    
        self.setCentralWidget(calwid)
        
    #make whole window into widget an swith widget
        self.startWin()
    
    def startWin(self):
     #menubar contains file
        mainMenu = self.menuBar() 
      #filemenu on main menu 
        fle = mainMenu.addMenu("File")
       #clear button for file menu
        clrButton = QAction(QIcon(""), 'Clear',self)
        clrButton.setShortcut("Ctrl+R")
        clrButton.setStatusTip("All Facts Doe")
        clrButton.triggered.connect(self.calcbuttonClicked)
        fle.addAction(clrButton)
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
        # taxButton = QPushButton(QIcon('pics\icons\BB8BW.jpg'),"taxit")
        # taxButton.setShortcut("Ctrl+t")
        # taxButton.setStatusTip("banking")
        # taxButton.clicked.connect(self.taxbuttonClicked)

        # layout = QHBoxLayout()
        # layout.addWidget(taxButton)
        # layout.addWidget(calcButton)
        # self.buttBox.setLayout(layout)

    def updateStats(self):
        date = QDateTime().currentDateTime().toLocalTime().toString()
        dateUtc = QDateTime().currentDateTimeUtc()

        stats = self.statusBar()
        stats.showMessage(date)

    def calcbuttonClicked(self):
        calcWid = CalcWid()
        self.swtchMainWid(calcWid)
        self.updateStats()

    # def taxbuttonClicked(self):
        # taxWid = TaxWid()
        # self.swtchMainWid(taxWid)
        # self.updateStats()

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
