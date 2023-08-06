N = int(input())
Numbers = list(map(int, input().split()))
K = int(input())


'''
sum = 0
ans = 0

for i in range(N):
    for j in range(N,-1,-1):
        if sum(Numbers[i:j]) == K:
            ans += 1

print(ans)

# More time complexity

'''

counts = {}
sum_ = 0
count = 0

for i in Numbers:
    sum_ += i

    if sum_ == K:
        count += 1
    if sum_ - K in counts:
        count += (counts[sum_-K])
    if sum_ in counts:
        count += 1
    else:
        counts[sum_] = 1

print(count)




