import os
from os.path import join,getsize

os.system("cls")
print (("-"*80))
print ("OS Walk Program")
print (("-"*80))
print ("""

""")

print ("Root prints out directories only from what you have specified")
print (("-"*70))

print ("Dirs prints out sub directories from root")
print (("-"*70))

print ("Files prints out  all files from root and directories")
print (("-"*70))

print ("This program will do an os walk on the folder you specify")
print (("-"*70))

path = input("Specify the foolder you want to perform an 'os.walk' on: >>")

for root,dirs,files in os.walk(path):
   print ((root))
   print (("---------"))
   print ((dirs))
   print (("---------"))
   print ((files))
   print (("---------"))
   print  (sum([getsize(join(root,name)) for name in files]))
   print (("bytes in", len(files),"non-directory files"))