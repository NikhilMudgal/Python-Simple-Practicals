import os
curr_dir=os.getcwd()
L=[]
x=input("Enter the data")
fp=open("Data.txt","w")
fp.write(x)
fp.close()
fp=open("Data.txt")
s=fp.read()
L=s.split()
L.sort()
s=' '.join(L)    
fp.close()
f=open("Sort.txt","w")
f.write(s)
f.close()
path=os.path.join(curr_dir,"Data.txt")
os.remove(path)
os.rename("Sort.txt","Data.txt")
fp=open("Data.txt")
s=fp.read()
print(s)
fp.close()
