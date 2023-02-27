version = list(map(int, input().split(".")))
n1 = version[0]
n2 = version[1]
n3 = version[2]
n3 += 1
if n3 == 10:
    n3 = 0
    n2 += 1
if n2 == 10:
    n2 = 0
    n1 += 1
print(f"{n1}.{n2}.{n3}")