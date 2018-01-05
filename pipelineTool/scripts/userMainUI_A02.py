
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
        self.setupUi(self)

        parent = self.centralwidget
        
        self.buildUI = buildUI.buildUI(parent)   #call buildUI class
        projectCount = 10
        
        
        self.projectTable = self.buildUI.createTable(parent,'projectTable',[10, 50, 200, 200],projectCount,32,2,[30,150])  #build project Table
                                        # createTable(self,parent,tableName,size,rowCount,rowSize,columnCount,columnSize)
       # self.assetTable = self.buildUI.createTable(parent,'assetTable',[220, 50, 200, 250],30,25,2,[30,200])  #build project Table

        #self.addUIButton(parent)


        self.addProjectItemButton(projectCount)
        self.addProjectItemButtonLabel(projectCount)
        #print self.projectButtonLabelAList


    ### event-driven
    def mouseMoveEvent(self, e):

        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        print text
        
        
    def buttonClick(self): 
        print self.sender().text()
        print self.sender().pos()
        index = self.projectTable.indexAt(self.sender().pos())
        print index.row(),index.column()
    ### event-driven
            

        
    

    def addUIButton(self,parent):  # �إ�project �ﶵ button
        self.pushProjectButtonA = self.buildUI.projectButtonA(parent,'projectButtonA',[10,10,30,30],"C:/alphaOnly/github/pipelineTool/UI/label_G2.png","C:/alphaOnly/github/pipelineTool/UI/label_G2_2.png",[30,30],True)
        self.pushProjectButtonB = self.buildUI.projectButtonA(parent,'projectButtonA',[40,10,30,30],"C:/alphaOnly/github/pipelineTool/UI/label_G2.png","C:/alphaOnly/github/pipelineTool/UI/label_G2_2.png",[30,30],True)
        self.pushProjectButtonC = self.buildUI.projectButtonA(parent,'projectButtonA',[70,10,30,30],"C:/alphaOnly/github/pipelineTool/UI/label_G2.png","C:/alphaOnly/github/pipelineTool/UI/label_G2_2.png",[30,30],True)
        
        #self.pushProjectButtonA.clicked.connect(self.rrr)
        
        
        
    def rrr(self):
        print 'asdsd'
        #print self.buildUI.exportButtonText
        print self.projectTable.cellWidget(3,0).text()
        
        

        
    def addProjectItemButton(self,projectCount): # �إߩҦ� projectTable �Ĥ@�C���� pushButton
        parent = self.projectTable

        for i in range(0,projectCount):

            projectButtonLabelA = self.buildUI.projectButtonB(parent,('a'+str(i)),('a'+str(i)),True,True,False,[200,200,200],[0,0,0],[200,255,200],[0,0,0],[100,100,100])

            self.projectTable.setCellWidget(i,0,projectButtonLabelA)
            #projectButtonLabelA.clicked.connect(lambda:self.buttonClick(projectButtonLabelA))
            projectButtonLabelA.clicked.connect(self.buttonClick)


        
    def addProjectItemButtonLabel(self,projectCount): # �إߩҦ� projectTable �Ĥ@�C���� pushButton
        parent = self.projectTable

        for i in range(0,projectCount):

            projectButtonLabelA = self.buildUI.projectButtonB(parent,('a'+str(i)),('a'+str(i)),True,False,True,[200,200,200],[200,0,0],[200,255,200],[0,0,0],[100,100,100])

            self.projectTable.setCellWidget(i,1,projectButtonLabelA)
            #projectButtonLabelA.clicked.connect(lambda:self.buttonClick(projectButtonLabelA))
            projectButtonLabelA.clicked.connect(self.buttonClick)

    
            




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

