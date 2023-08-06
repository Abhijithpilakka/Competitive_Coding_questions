GF = list(map(int, input().split()))
S = list(map(int, input().split()))

'''
count = 0

for i in GF:
    for j in range(len(S)):
        if i<= S[j]:
            count += 1
            S[j] = 0
            break

print(count)

'''

i = 0
j = 0
n,m = len(GF) , len(S)

count = 0

GF.sort()
S.sort()

while(i<n and j<m):
    if GF[i] <= S[j]:
        count += 1
        i += 1
        j += 1
    else:
        j += 1

print(count)