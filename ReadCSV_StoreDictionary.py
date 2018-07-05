L=[]
record={}
csvfile=open("python.csv")
for item in csvfile:
    L.append(item.rstrip().split(','))
c=len(L)
for i in range(0,c):
    record[L[i][0]]=L[i][1:]
for x,y in record.items():
    print(x+str(y))
