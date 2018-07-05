import os
fp=open("change.txt","w")
x=input("Enter the data")
fp.write(x)
fp.close()
curr_dir=os.getcwd()
for item in os.listdir(curr_dir):
    path=os.path.join(curr_dir,item)
    if(os.path.isfile(item)):
        fp=open(path,'r')
        y=fp.read()
        if "Hello" in y:
            a=os.chdir("D:\Python")
            f=open("new.txt",'w')
            f.write("Hello")
            print("New directory created")  
            f.close()
    else:
        continue
fp.close()            
os.chdir(curr_dir)        
