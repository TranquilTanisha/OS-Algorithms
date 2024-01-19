blocksize=[25,40,100,20,10]
print("Enter the process size")
psize=[int(x) for x in input().split()]
print("Blocksize: ", blocksize)    
print("Process size: ", psize)

m=5
n=len(psize)
allocation=[-1]*n

for i in range(n):
    for j in range(m):
        if (allocation[j]==-1) :
            if psize[i]<=blocksize[j]:
                blocksize[j]-=psize[i]
                allocation[i]=j+1
                break
        
print(allocation)
print(blocksize)