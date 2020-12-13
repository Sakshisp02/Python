#-#-# Question1 -: Write a prog in python for opening a file and writing "Hey i am Saurabh Pawar" and close it,
# and read it back again and then append something data to it and close it ?

print("File Handling")

abc=open("Sakshi.txt",'w')
abc.write("Hey Guys, I am Sakshi Pawar \n")
abc.close()

#Append Operation
abc=open("Sakshi.txt",'a')
abc.write("I am amazing \n")
abc.close()
