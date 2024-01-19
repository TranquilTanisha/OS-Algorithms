def sstf(head):
    total_seek=0
    dir=""
    for i in range(n):
        id=rq.index(head)
        if id!=0 and id!=n-1:
            if abs(rq[id]-rq[id-1])==abs(rq[id]-rq[id+1]):
                if dir=="right" or dir=="":
                    total_seek+=abs(head-rq[id+1])
                    dir="right"
                    del rq[id]
                    head=rq[id]
                    
                elif dir=="left":
                    total_seek+=abs(head-rq[id-1])
                    dir="left"
                    del rq[id]
                    head=rq[id-1]

            else:
                p=min(abs(head-rq[id-1]), abs(head-rq[id+1]))
                total_seek+=p
                if p==abs(head-rq[id-1]):
                    dir="left"
                    rq.remove(head)
                    head=rq[id-1]
                else:
                    dir="right"    
                    rq.remove(head)
                    head=rq[id]
                    
        elif id==0 :
            temp=rq[1:len(rq)]
            for j in range(len(temp)):
                if j==0:
                    total_seek+=abs(head-temp[j])
                else:
                    total_seek+=abs(temp[j]-temp[j-1])
        else: 
            temp=rq[1:len(rq)]
            temp.reverse()
            for j in range(len(temp)):
                if j==0:
                    total_seek+=abs(head-temp[j])
                else:
                    total_seek+=abs(temp[j]-temp[j-1])
    print("Total seek= ", total_seek)

print("SSTF Disk Scheduling Algorithm")
r=[int(x) for x in input("Enter the range: ").split()]
n=int(input("Enter the number of requests: "))
rq=[int(x) for x in input("Enter the requests: ").split()]
head=int(input("Enter the head position: "))

print("Range: ")
print(r)
print("Requests: ")
print(rq)
print("Head position: ")
print(head)

rq.append(head)
rq.sort()
# print(rq)

sstf(head)