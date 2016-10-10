#Import the Modules 
import sys 
import random

ans =True

while ans:
	quetion = input("Ask the 8 ball a quetios:(press enter to quit)")
	
	answers = random.randint(1,8)
	
	if quetion =="":
	   sys.exit()
	
	elif answers == 1:
	   print ("It is certain")
	 
	elif answers == 2:
	   print ("Outlook Good")
	
	elif answers == 3:
	   print ("You may rely on it")
	
	elif answers == 4:
	   print ("Ask again Later")
	
	elif answers == 5:
	   print ("Concentrate and ask again")
	
	elif answers == 6:
	   print ("Reply hazy,try again")
	   
	elif answers == 7:
	   print ("My Reply is no")
	   
	elif answers == 8:
	   print ("My sources say no")