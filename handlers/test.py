n = int(input())
for i in range(n * 2):
    s1 = input().split()
    s2 = input().split()
    a = set(s1)
    b = set(s2)
    m = (a | b) - (a & b)
    print(' '.join(m))