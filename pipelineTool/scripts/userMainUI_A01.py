
from PySide2 import QtCore, QtGui, QtWidgets
import buildUI
reload(buildUI)
import random 
import testWindowUI
reload(testWindowUI)

 
testWindowUI = testWindowUI.testWindowUI
setupUi = testWindowUI.setupUi
#import datetime

#import json

#import postgreSQLCall



#import postgreSQLCall

#reload(postgreSQLCall)a

# self.centralwidget = QtWidgets.QWidget(MainWindow)
# self.centralwidget.setObjectName("centralwidget")


    

class mod_MainWindow(QtWidgets.QMainWindow, testWindowUI):
   
    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)
        #print self.centralwidget
       

        
        #print      def addNameCard(self,nameCardPosition,name,dept,sec,specA,specB):

        
        parent = self.centralwidget
        
        self.buildUI = buildUI.buildUI(parent)   #call buildUI class
        #projectButtonA(self,buttonName,position,iconPath,iconSize)
        projectCount = 10
        self.projectTable = self.buildUI.createTable(parent,'projectTable',[10, 50, 200, 200],projectCount,32,2,[30,150])  #build project Table
                                        # createTable(self,parent,tableName,size,rowCount,rowSize,columnCount,columnSize)
        self.assetTable = self.buildUI.createTable(parent,'assetTable',[220, 50, 200, 250],30,25,2,[30,200])  #build project Table

        self.addUIButton(parent)


        self.addProjectItemButton(projectCount)
        #print self.projectButtonLabelAList


    ### event-driven
    def mouseMoveEvent(self, e):

        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        print text
    
    def buttonClicked(self):
      
        sender = self.sender()
        print sender.text()
        
    

    def addUIButton(self,parent):  # 建立project 選項 button
        self.pushProjectButtonA = self.buildUI.projectButtonA(parent,'projectButtonA',[10,10,30,30],"C:/alphaOnly/github/pipelineTool/UI/label_G2.png","C:/alphaOnly/github/pipelineTool/UI/label_G2_2.png",[30,30],True)
        self.pushProjectButtonB = self.buildUI.projectButtonA(parent,'projectButtonA',[40,10,30,30],"C:/alphaOnly/github/pipelineTool/UI/label_G2.png","C:/alphaOnly/github/pipelineTool/UI/label_G2_2.png",[30,30],True)
        self.pushProjectButtonC = self.buildUI.projectButtonA(parent,'projectButtonA',[70,10,30,30],"C:/alphaOnly/github/pipelineTool/UI/label_G2.png","C:/alphaOnly/github/pipelineTool/UI/label_G2_2.png",[30,30],True)
        
        #self.pushProjectButtonA.clicked.connect(self.rrr)
        
        
        
    def rrr(self):
        print 'asdsd'
        #print self.buildUI.exportButtonText
        print self.projectTable.cellWidget(3,0).text()
        
        
    def addProjectItemButton(self,projectCount):
        parent = self.projectTable
        self.projectButtonLabelAList = []  # 建立所有 projectTable 第一列中的 pushButton
        for i in range(0,projectCount):
            #self.addbuttonC(i)
            self.projectButtonLabelA = self.buildUI.projectButtonB(self.projectTable,('a'+str(i)))
            self.projectButtonLabelAList.append(self.projectButtonLabelA)
            self.projectTable.setCellWidget(i,0,self.projectButtonLabelA)
  
        
    def addProjectItemButtonB(self,projectCount): # 建立 table中建立 project的 label
        parent = self.projectTable
        #projectButtonLabelAList = []
        #print type(parent)
        for i in range(0,projectCount):
            #projectButtonCheck = self.buildUI.projectButtonA('','projectButtonCheck',[0,0,30,30],"C:/alphaOnly/github/pipelineTool/UI/label_G2.png","C:/alphaOnly/github/pipelineTool/UI/label_G2_2.png",[30,30],True)
          #  print type(pushButton)
           #projectButtonLabel = self.buildUI.projectButtonA('','projectButtonLabel',[0,0,30,30],"C:/alphaOnly/github/pipelineTool/UI/label_G2.png","C:/alphaOnly/github/pipelineTool/UI/label_G2_2.png",[30,30],False)
            projectButtonLabelA = self.buildUI.projectButtonB(parent,('a'+str(i)),('a'+str(i)),True,[200,200,200],[0,0,0],[200,255,200],[0,0,0],[100,100,100])
            #print projectButtonLabelA,type(projectButtonLabelA),projectButtonLabelA.text()
            #rojectButtonLabelAList.append(projectButtonLabelA)
            self.projectTable.setCellWidget(i,0,projectButtonLabelA)
            projectButtonLabelA.clicked.connect(lambda:self.ccc(projectButtonLabelA))
            #print projectButtonLabelA.focusWidget()
            #projectButtonLabelA.clicked.connect(self.ddd)
            #projectButtonLabelB = self.buildUI.projectButtonB(parent,('b'+str(i)),False,[80,80,80],[255,255,255],[255,0,0],[255,255,255],[100,100,100])

            #self.projectTable.setCellWidget(i,1,projectButtonLabelB)
        #print projectButtonLabelAList
        
       # for i in projectButtonLabelAList:
        #    print i.text()
        #    i.clicked.connect(lambda:self.ccc(i))
        #projectButtonB(self,parent,buttonName,buttonText,checkAble,buttonBGColor,buttonTextColor,buttonCheckBGColor,buttonCheckTextColor,buttonHoverColor):
    def addbuttonC(self,i):
        parent = self.projectTable
        projectButtonC = QtWidgets.QPushButton(parent)
        projectButtonC.setText('a'+str(i))
        projectButtonC.setCheckable(True)
        projectButtonC.setObjectName('a'+ str(i))
        self.projectTable.setCellWidget(i,0,projectButtonC)
        projectButtonC.clicked.connect(lambda:self.ccc(projectButtonC))
    
    def addButton(self,i,parent):
        
        print i
        #print 
        pushButton = self.buildUI.projectButtonA(parent,'projectButtonA',[0,0,30,30],"C:/alphaOnly/github/pipelineTool/UI/label_G2.png","C:/alphaOnly/github/pipelineTool/UI/label_G2_2.png",[30,30])


        self.tableWidget.setCellWidget(i,0,pushButton)

        pushButton.setText(str(i))
        pushButton.clicked.connect(lambda:self.ccc(pushButton))
    
            
    def ccc(self,button): 
        print 'adssad'
        clicked = QtWidgets.QApplication.focusWidget()
        index = self.projectTable.indexAt(clicked.pos())
        #print self.projectTable.currentItem().text()
        #print index.row(),index.column()
        print button.text()
        
        


    def bbb(self):
        print 'asdsad'
        clicked = QtWidgets.QApplication.focusWidget()
        index = self.projectTable.indexAt(clicked.pos())
        #print self.projectTable.currentItem().text()
        print index.row(),index.column()
        
    def addNameCardTest(self):
        
        for i in range(0,10):
            name = "alpha"
            dept = "3D"
            sec = "animation"
            specA = "work on"
            #random(0,255)
            baseColor = (random.randint(20,200),random.randint(20,200),random.randint(20,200))
            buttonAColor = (random.randint(0,10),random.randint(0,10),random.randint(240,255))
            buttonBColor = (random.randint(90,100),random.randint(90,100),random.randint(0,255))
            labelAColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            labelBColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            labelCColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            labelDColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            labelEColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            progressBarValue = random.randint(0,100)
            self.buildUI.addSmallNameCard((0,i*56,271,56),name,dept,sec,specA,
                                          baseColor,buttonAColor,buttonBColor,
                                          labelAColor,labelBColor,labelCColor,labelDColor,labelEColor,
                                          progressBarValue)
            
            


        #for i in range(0,5):
            #self.buildUI.addButton('asdsad',[(i*100), 160, 75, 23])
        #self.buildUI.addLabel((220, 160, 75, 23))
        #self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton.setGeometry(QtCore.QRect(220, 160, 75, 23))
        #self.pushButton.setObjectName("pushButton")
        
        #self.centralwidget = QtWidgets.QWidget(MainWindow)
        #self.centralwidget.setObjectName("centralwidget")
        #self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton.setGeometry(QtCore.QRect(220, 160, 75, 23))
        #self.pushButton.setObjectName("pushButton")
            

def testUImain():
    global ui
    #app == None
    app = QtWidgets.QApplication.instance()
    if app == None: app = QtWidgets.QApplication(sys.argv)
    try:
        ui.close()
        ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()
 
if __name__ == '__main__':
    testUImain()

