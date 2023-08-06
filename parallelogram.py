# lexicographycally smaller - coordinate which has smallest x. if x are same, then smallest y
# map function - apply a function in an iterable object
# split - split the string 

A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))
C = tuple(map(int,input().split()))

D1 = [A[0] + C[0] - B[0], A[1] + C[1] - B[1]]
D2 = [A[0] + B[0] - C[0] , A[1] + B[1] - C[1]]
D3 = [B[0] + C[0] - A[0] , B[1] + C[1] - A[1]]

print (min(D1,D2,D3))
