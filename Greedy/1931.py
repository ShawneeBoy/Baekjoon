# 2021. 05.05
# Attempts: 3
# Solve time: 20min

n = int(input())

data = []

for i in range(n):
    start, end = map(int, input().split())
    data.append((start, end))

# Sort by start time
data.sort(key = lambda a : a[0])
# Sort by end time
data.sort(key = lambda a : a[1])

#print(data)

end = 0
count = 0
for conf in data:
    if(conf[0] >= end):
        end = conf[1]
        count += 1
#        print(conf) # debug

print(count)

