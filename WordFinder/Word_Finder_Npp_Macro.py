import re
import os
import sys
from Npp import *

src  =  "D:/Vignesh/Software/Pythonscripts/Word_Finder/Word_To_Find.txt"

def  Search_Npp(searchtext) :
    stg_file = open(src,"r")
    find_str = stg_file.read()
    notepad.messageBox(find_str)

if __name__ == '__main__':
   Search_Npp()