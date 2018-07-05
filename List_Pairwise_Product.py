L=[]
L1=[]
L2=[]
sum=0
print('Enter the elements of the first list')
for i in range(0,5):
    a=int(input());
    L.append(a)
print(L)
print('Enter the elements of the second list')
for i in range(0,5):
    a=int(input());
    L1.append(a)
print(L1)    
for i in range(0,5):
    L2.append(L[i]*L1[i])
for i in range(0,5):
    sum+=L2[i]
print(sum)
