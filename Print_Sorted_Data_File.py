L=[]
x=input("Enter the data")
L=x.split()
L.sort()
x=' '.join(L)
fp=open("File.txt",'w')
fp.write(x)
fp.close()
fp=open("File.txt")
s=fp.read()
print(s)
