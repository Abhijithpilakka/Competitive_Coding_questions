N = int(input())
arr = list(map(int,input().split()))

steps = 0
prod = 1
zeroes = 0

for i in arr:
    if i<0:
        steps +=(abs(i)-1)
        prod *= -1
    elif i>0:
        steps += (i-1)
        prod *= 1
    else:
        zeroes +=1

if prod==1 or (prod == -1 and zeroes>0):
    steps += zeroes

elif prod == -1:
    steps += 2

print(steps)