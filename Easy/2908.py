# 2021. 05. 07
# Attempts: 1
# Solve time: 1 min

a, b = map(str, input().split())

arev = int(a[::-1])
brev = int(b[::-1])

print(arev) if arev>brev else print(brev)