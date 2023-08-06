# Given the arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits. we are given two arrays that represents the arrival and departure times of trains that stop.

# input arr[] = {9:00, 9:40, 9:50, 11:00,15:00, 18:00}  dep[] = {9:10, 12:00, 11:20, 11:30,19:00, 20:00}

# output 3

arr = list(map(int, input().split()))
dep = list(map(int, input().split()))

count = 1
counts = []

for i in range(1, len(arr)):
    count = 0
    for j in range(1, len(arr)):
        if arr[j] < dep[j-i] and arr[j] > arr[j-i]:
            count += 1
    counts.append(int(count))

print(max(counts))
