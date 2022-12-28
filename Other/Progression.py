n = list(map(int, input().split()))

k = 0
for i in range(len(n) - 1):
    if (n[i+1] - n[i]) == (n[1] - n[0]):
        k += 1
if k == len(n)-1:
    print('Yes')
else:
    print('No')
