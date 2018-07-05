L=[]
L1=[]
x=int(input("How many elements do you want in a list ?"))
for i in range(0,x):
    print("Do you want to enter the sublist or an element ?")
    y=int(input(("Enter 1 For sublist And 0 For element")))
    if(y==1):
        L=[]
        print("Enter the number of elements to be taken in a sublist ")
        z=int(input())
        print("Enter the elements of sublist ")
        for j in range(0,z):
            a=int(input())
            L.append(a)
        L1.append(L)    
    elif(y==0):
        print("Enter the element of the list ")
        q=int(input())
        L1.append(q)
    else:
     print("Wrong choice")    

del L1[0]
del L1[-1]
print(L1)
