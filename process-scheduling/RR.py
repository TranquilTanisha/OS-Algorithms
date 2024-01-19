def ready_queue(max): #adds processes to ready queue
    if max!=n-1:
        for j in range(max+1, n):
            if s[j][1][0]<=t:
                rq.append(s[j])
                max+=1

comb={}
wt={}
tat={}
ct={}
atat=0
awt=0
n=int(input("Enter the no of processes: "))
q=int(input("Enter the time quantum: "))
print("Enter arrival time and burst time of process ")
for i in range(n):
    a,b=map(int, input().split())
    comb[i]=[a, b]

seq=sorted(comb.items(), key=lambda x: x[1])
s=[]
for i in seq:
    s.append([i[0], i[1]])
print(s)

max=0 #keeps count of the last process added to ready queue
order=[]
t=s[0][1][0]
i=0
rq=[]
while True:
    # if i==0:
    #     rq.append(s[i])
    ready_queue(max)
    l=rq[i][0]
    if rq[i][1][1]>q: #burst time>q
        rq[i][1][1]-=q
        t+=q
        order.append("P"+str(l+1))
        ready_queue()
        rq.append(rq[i])
    else:
        t+=rq[i][1][1]
        order.append("P"+str(l+1))
        ready_queue()
        ct[l]=t
        tat[l]=ct[l]-rq[i][1][0]
        wt[l]=tat[l]-rq[i][1][1]
    i+=1
    if i==len(rq):
        break

print("Completion time: ",sorted(ct.items(), key=lambda x: x[0]))   
print("Turn around time: ", sorted(tat.items(), key=lambda x: x[0]))
print("Waiting time: ", sorted(wt.items(), key=lambda x: x[0]))

atat=sum(tat)/n
awt=sum(wt)/n

print("Avg TAT: ", atat)
print("Avg wt: ", awt)
print(order)