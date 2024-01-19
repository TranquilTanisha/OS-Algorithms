def fcfs():
    total_seek=0
    for i in range(n):
        if i==0:
            total_seek+=abs(head-rq[i])
        else:
            total_seek+=abs(rq[i]-rq[i-1])
    print("Total seek= ",total_seek)

print("FCFS Disk Scheduling Algorithm")
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

fcfs()
