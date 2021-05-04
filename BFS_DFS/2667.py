# # 2021.05.04
# Attempts: 1
# Solve Time: ~40 min?

n = int(input())

data = []

for i in range(n):
    data.append(list(map(int, input())))   

#define DFS function
def dfs(x, y):
    if(x<0 or x>=n or y<0 or y>=n):
        return 0 # end case
    
    if(data[x][y] == 0): 
        return 0 # end case
    
    else:
        data[x][y] = 0
        # Recursively calculate number of cells visited. End case is all dfs calls return 0. Else, they will return default cellcount (1), or more.
        cellcount = 1
        cellcount += dfs(x-1, y)
        cellcount += dfs(x+1, y)
        cellcount += dfs(x, y+1)
        cellcount += dfs(x, y-1)
    return cellcount

cellSizes = []
count = 0

for i in range(n):
    for j in range(n):
        currCount = dfs(i, j)
        if(currCount > 0):
            cellSizes.append(currCount)
            count += 1

cellSizes.sort()

print(count)
for i in cellSizes:
    print(i)




