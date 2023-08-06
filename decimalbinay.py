X = int(input())

Binary = []

while X!=1:
    Binary.append(X%2)
    X = int(X/2)

Binary.append(X)

print(Binary[::-1])