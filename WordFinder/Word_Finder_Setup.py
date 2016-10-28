import sys
import os
import re
import shutil


from PyQt4 import QtCore, QtGui,uic

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here,'Word_Finder.ui')
nppmacro = os.path.join(here,'Word_Finder_Npp_Macro.py')
form_class = uic.loadUiType(filename)[0]

def  checkNppMacro():
    
    dst =   "C:/Users/bnlvija/AppData/Roaming/Notepad++/plugins/Config/PythonScript/scripts"
    
    if not os.path.isfile(os.path.join(dst,'Word_Finder_Npp_Macro.py')):
    
        shutil.copy2(nppmacro,'C:/Users/bnlvija/AppData/Roaming/Notepad++/plugins/Config/PythonScript/scripts')
        print("Macro Check : Npp Macro Added")
        
    else:
    
        print("Macro Check : Npp macro Already Exists")


class  cl_Word_Finder (QtGui.QMainWindow,form_class):
    
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.bt_file_dialog.clicked.connect(self.getSearchLocation)
        self.bt_find.clicked.connect(self.findFirstInstance)
        self.bt_find_all.clicked.connect(self.findAllInstances)
        
    def getSearchLocation(self):
        self.searchlocation= QtGui.QFileDialog(self)
        self.le_location.setText(self.searchlocation.getExistingDirectory())
        
    def findFirstInstance(self):     
        self.rowcount = 0
        self.colid =0
        
        if len(self.le_find_value.text() )==0 or len(self.le_location.text()) == 0 :
            self.errormsg = QtGui.QMessageBox(self)
            self.errormsg.warning(self,"Message","Value or Location is Empty")
            self.show()
        else:
            if  "Text Files" in self.cb_find_filters.currentText():
                
                self.stg_text_file = open(os.path.join(here,'Word_To_Find.txt'),"w")
                self.stg_text_file.write(self.le_find_value.displayText())
                self.stg_text_file.close()
                
                self.searchfile(fext = [".txt" ], searchapp ="Notepad++")                            
            
            elif "Open Office" in self.cb_find_filters.currentText():
                self.searchfile(fext = [".odt",".odf","odg",".odp",".ods"],searchapp = "OOSDK")
                
            elif "Microsoft Office" in self.cb_find_filters.currentText():
                self.searchfile(fext = [".doc",".docx",".xls",".xlsx",".ppt",".pptx"], searchapp= "Pydocx")
            
            else:
                 self.searchfile(fext = [".txt",".odt",".odf","odg",".odp",".ods",".doc",".docx",".xls",".xlsx",".ppt",".pptx"],searchapp = "Corresponding")
         
    def findAllInstances(self):
        print("Find All Instances")
    
    def searchfile(self,fext,searchapp):
        self.cleartable()
        for root, dirs, files in os.walk(self.le_location.text()):
                     for file in files:
                        if file.endswith(tuple(fext)):
                            self.rowPosition = self.table_Results.rowCount()
                            self.table_Results.insertRow(self.rowPosition)
                            self.table_Results.setItem(self.rowPosition,0,QtGui.QTableWidgetItem(file))
                            self.table_Results.setItem(self.rowPosition,1,QtGui.QTableWidgetItem(os.path.join(root,file)))
        
        print(searchapp)
        return
    
    def cleartable(self):
        while (self.table_Results.rowCount() > 0) :
            self.table_Results.removeRow(0)
        
if __name__ == "__main__":
    checkNppMacro()
    app = QtGui.QApplication(sys.argv)
    myapp = cl_Word_Finder(None)
    myapp.show()
    sys.exit(app.exec_())