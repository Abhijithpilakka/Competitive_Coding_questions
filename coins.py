coins = list(map(int, input().split()))
N = int(input())


ans = [0]

for i in range(1, N+1):
    ans.append('$')
    
    for j in coins:

        if i-j >= 0 and ans[i-j]!='$':
            if ans[i] == '$':
                ans[i] =ans[i-j] + 1
            else:
                ans[i] = min(ans[i-j] + 1, ans[i])

    print(ans)

print(ans[-1])



    

