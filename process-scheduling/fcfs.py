comb={}
ct=[]
wt=[]
tat=[]
atat=0
awt=0

n=int(input("Enter the no of processes: "))
print("Enter arrival time and burst time of process ")
for i in range(n):
    a,b=map(int, input().split())
    comb[i]=[a, b]

seq=sorted(comb.items(), key=lambda x: x[1])
s=[]
for i in seq:
    s.append([i[0], i[1]])

order=[]
t=s[0][1][0] #arrival time of first process
for i in range(n):
    if s[i][1][0]<=t:
        t+=s[i][1][1]
    else:
        t=s[i][1][0]
        t+=s[i][1][1]
    ct.append(t)
    tat.append(ct[i]-s[i][1][0])
    wt.append(tat[i]-s[i][1][1])
    order.append("P"+str(s[i][0]+1))
    
print("Completion time: ",ct)
print("Turn around time: ", tat)
print("Waiting time ", wt)

atat=sum(tat)/n
awt=sum(wt)/n

print("Avg TAT: ", atat)
print("Avg wt: ", awt)
print(order)