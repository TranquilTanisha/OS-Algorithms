print("Best Fit")
mem=[int(x) for x in input("Enter the available memory: ").split()]    
burst=[int(x) for x in input("Enter the burst time of the processes:").split()]
m=len(mem)
n=len(burst)
    
print("Available memory: ")
print(mem)
print("Burst time: ")
print(burst)
print()
allocation=[-1]*n

for i in range(n):
    diff=[]
    for j in range(m):
        if burst[i]<=mem[j]:
            diff.append(abs(mem[j]-burst[i]))
        else:
            diff.append(999)
    # print(diff)
    id=diff.index(min(diff))
    # print(id)
    mem[id]-=burst[i]
    allocation[i]=id+1

print(allocation)