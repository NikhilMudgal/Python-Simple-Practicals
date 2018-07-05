def nest_sum(x):
    sum1=0
    sum2=0 
    if isinstance(x,list):
        c=len(x)
        for w in range(0,c):
            sum1+=x[w]
    else:
      sum2+=x      
    return sum1+sum2
L1=[]
L=[]
b=0
print("How many inputs do you want in a list?")
x=int(input())
for i in range(0,x):
    print("Do you want to enter the list or an element ?")
    y=int(input(("Enter 1 For List And 0 For element")))
    if(y==1):
        L=[]
        print("Enter the number of elements to be taken in a sublist ")
        z=int(input())
        print("Enter the elements of sublist ")
        L=[]
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
for g in range(0,x):
     b+=nest_sum(L1[g])
print(b)     
