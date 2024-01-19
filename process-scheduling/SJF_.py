comb={}# to store arrival time and burst time of process
wt={}
tat={}
ct={}
atat=0
awt=0

n=int(input("Enter the no of processes: "))
print("Enter arrival time and burst time of process ")
for i in range(n):
    a,b=map(int, input().split())
    comb[i]=[a, b]

seq=sorted(comb.items(), key=lambda x: x[1]) #sorts the dictionary by value, at,bt
s=[]
for i in seq:
    s.append([i[0], i[1]])
print(s)#converted to list

order=[]
t=s[0][1][0]
for i in s:
    if i[1][0]>t:
        t=i[1][0]
    else:
        t+=i[1][1]
        order.append("P"+str(i[0]+1))

    ct[i[0]]=t
    tat[i[0]]=ct[i[0]]-i[1][0]
    wt[i[0]]= tat[i[0]]-i[1][1]

print("Completion time: ",sorted(ct.items(), key=lambda x: x[0])) #sorts by key
print("Turn around time: ", sorted(tat.items(), key=lambda x: x[0]))
print("Waiting time: ", sorted(wt.items(), key=lambda x: x[0]))

atat=sum(tat.values())/n
awt=sum(wt.values())/n

print("Average turn around time: ", atat)
print("Average waiting time: ", awt)
print(order)