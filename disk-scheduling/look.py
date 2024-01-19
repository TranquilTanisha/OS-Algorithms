def look():
    total_seek=0
    id=rq.index(head)
    t1=rq[0:id]
    t2=rq[id+1:n+1]
    print(t1)
    print(t2)
    if dir=="higher":
        for i in range(len(t2)):
            if i==0:
                total_seek+=abs(head-t2[i])
            else:
                total_seek+=abs(t2[i]-t2[i-1])

        t1.reverse()
        
        for i in range(len(t1)):
            if i==0:
                total_seek+=abs(t2[len(t2)-1]-t1[i])
            else:
                total_seek+=abs(t1[i]-t1[i-1])
    else:
        t1.reverse()
        for i in range(len(t1)):
            if i==0:
                total_seek+=abs(head-t1[i])
            else:
                total_seek+=abs(t1[i]-t1[i-1])

        for i in range(len(t2)):
            if i==0:
                total_seek+=abs(t1[len(t1)-1]-t2[i])
            else:
                total_seek+=abs(t2[i]-t2[i-1])
    print("Total seek= ", total_seek)

print("LOOK Disk Scheduling Algorithm")
r=[int(x) for x in input("Enter the range: ").split()]
n=int(input("Enter the number of requests: "))
rq=[int(x) for x in input("Enter the requests: ").split()]
head=int(input("Enter the head position: "))
dir=input("Enter the direction (higher/lower): ")

print("Range: ")
print(r)
print("Requests: ")
print(rq)
print("Head position: ")
print(head)
print("Direction: ")
print(dir)

rq.append(head)
rq.sort()
print(rq)

look()