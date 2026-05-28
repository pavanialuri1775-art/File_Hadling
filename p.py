#1 Read and print the entire file
with open("practice.txt","r") as f:
    print(f.read())
    
#2 Count total characters in the file
with open("practice.txt","r") as f:
    data=f.read()
    print(len(data))
    
#3 Count total words in the file
with open("practice.txt","r") as f:
    data=f.read()
    words=data.split()
    print(len(words))
    
#4 Count total lines in the file
with open("python.txt","r") as f:
    lines=f.readlines()
    print(len(lines))
    
#5 Count total vowels in the file
with open("python.txt","r") as f:
    data=f.read()
    vowels="aeiouAEIOU"
    count=0
    for ch in data:
        if ch in vowels:
            count+=1
    print("total count:",count)
    
#6 Print each line separately using loop
with open("practice.txt","r") as f:
    lines=f.readlines()
    for line in lines:
        print(line.strip())
        
#7 Append this line to the file
with open("practice.txt","a") as f:
    f.write("Consistency makes learning stronger")
    
#8
#Search whether word "Python" exists in file
with open("practice.txt","r") as f:
    data = f.read()
    if "Python" in data:
        print("Word Found")
    else:
        print("Word Not Found")
