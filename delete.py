#Delete a File
#To delete a file, we must import the OS module, and run its os.remove() function
#Remove the file "demofile.txt"
import os
os.remove("demofile.txt")

#Check if File exist
#To avoid getting an error, we might want to check if the file exists before we try to delete it
#Check if file exists, then delete it:
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
    
#Delete Folder
#To delete an entire folder, use the os.rmdir() method
#ex:Remove the folder "myfolder"
import os
os.rmdir("myfolder")

