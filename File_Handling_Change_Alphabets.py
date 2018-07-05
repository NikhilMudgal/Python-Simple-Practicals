fp=open("rename.txt",'w')
x=input("Enter the content of the file")
fp.write(x)
fp.close()
fp=open("rename.txt")
s=fp.read()
new=str()
for item in s:
    if(item=='a'):
        new+='d'
    elif(item=='b'):
        new+='e'
    elif(item=='c'):
        new+='f'
    else:
        new+=item
print(new)
fp.close()
