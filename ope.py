#to open a file on the server
#To open the file, use the built-in open() function.
#The open() function returns a file object, which has a read() method for reading the content of the file.
#ex
f = open("demofile.txt")
print(f.read())
#If the file is located in a different location, you will have to specify the file path, like this:
f = open("D:\\myfiles\welcome.txt")
print(f.read())
#Using the with statement
#You can also use the with statement when opening a file
with open("demofile.txt") as f:
  print(f.read())


#closing files
#It is a good practice to always close the file when you are done with it.
#Close the file when you are finished with it:
f = open("demofile.txt")
print(f.readline())
f.close()

#Read Only Parts of the File
#By default the read() method returns the whole text, but you can also specify how many characters you want to return
#ex:Return the 5 first characters of the file:
with open("demofile.txt") as f:
  print(f.read(5))

#Read Lines
#You can return one line by using the readline() method:
with open("demofile.txt") as f:
  print(f.readline())
  
#By calling readline() two times, you can read the two first lines
with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())
  
#By looping through the lines of the file, you can read the whole file, line by line:
with open("demofile.txt") as f:
  for x in f:
    print(x)
