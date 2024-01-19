# blocksize=[25,40,100,20,10]
blocksize=[100,50,30, 120, 35]
print("Enter the processes separated by spaces")
psize=[int(x) for x in input().split()]
print("Blocksize: ", blocksize)    
print("Process size: ", psize)

m=5
n=len(psize)
allocation=[-1]*n

for i in range(n):
    for j in range(m):
        if psize[i]<=blocksize[j]:
            blocksize[j]-=psize[i]
            allocation[i]=j+1
            break
        
print(allocation)
print(blocksize)