a = list(input().split())
a = [int(i) for i in a]
k = int(input())
if k > 0:
    k%=len(a)
    for i in range(len(a) - k, len(a)):
        print(a[i], end=" ")
    for i in range(len(a) - k):
        print(a[i], end=" ")
else:
    k = abs(k)
    k%=len(a)
    for i in range(k, len(a)):
        print(a[i], end=" ")
    for i in range(k):
        print(a[i], end=" ")