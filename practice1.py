#Create and Write to a File
with open("student.txt","w") as f:
    f.write("Name:Pavani\n")
    f.write("Age:20")
with open("student.txt","r") as f:
    print(f.read())
    
#Read and print the contents of a file
with open("student.txt","r") as f:
    print(f.read())
    
#3
with open("python.txt","w") as f:
    f.write("Python\n")
    f.write("File Handling\n")

#4
with open("python.txt","a") as f:
    f.write("Learning Python")
with open("python.txt","r") as f:
    print(f.read())
    
#5
with open("python.txt","r") as f:
    data=f.read()
    print(len(data))

#6
with open("python.txt") as f:
    data=f.read()
    words=data.split()
    print("Total words:",len(words))
    
#7
with open("python.txt","r") as f:
   lines=f.readlines()
   print(len(lines))
   
#8
with open("python.txt","r") as f:
    lines=f.readlines()
    for x in lines:
        print(x.strip())
        
#9
with open("python.txt","r") as f:
    data=f.read()
    vowels="aeiouAEIOU"
    count=0
    for ch in data:
        if ch in vowels:
            count+=1
    print("Total vowels:",count)
    
#10
with open("python.txt","r") as f:
    data=f.read()
    words=data.split()
    longest=words[0]
    for word in words:
        if len(word)>len(longest):
            longest=word
    print("longest word:",longest)