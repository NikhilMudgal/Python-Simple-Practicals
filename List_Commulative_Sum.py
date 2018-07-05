def cum_sum(x):
    sum=0
    L1=[]
    if isinstance(x,list):
        c=len(x)
        for j in range(0,c):
            sum+=x[j]
            L1.append(sum)
    print(L1)
L=[]
print("Enter the no. of elements to be taken in a list")
x=int(input())
for i in range(0,x):
    y=int(input())
    L.append(y)
cum_sum(L)
