import re
import os
import sys
from Npp import *

src  =  "D:/Vignesh/Software/Pythonscripts/Word_Finder/Word_To_Find.txt"

def  Search_Npp() :
    if  not os.stat(src).st_size ==0:
        stg_file = open(src,'r')
        find_str = stg_file.readline()
        stg_file.close()
        pos = editor.findText(FINDOPTION.WHOLEWORD, 0, editor.getLength(), str(find_str))
        if pos is not None:
            editor.gotoPos(pos[0])      
            stg_file = open(src,"a")
            stg_file.write("\n" + bytes(editor.lineFromPosition(pos[0])))
            stg_file.write("\n" + bytes(editor.getColumn(pos[0])))
            stg_file.write("\n" + bytes(editor.getCurLine()))
            stg_file.close()
        else :
            notepad.messageBox("No Match Found")
    else:
        notepad.messageBox("Search Word File  Empty: No word To search") 
    
if __name__ == '__main__':
   
   Search_Npp()