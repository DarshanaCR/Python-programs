inp = input().split(" ")
s = int(inp[0])
v1 = int(inp[1])
v2 = int(inp[2])
b1 = 0
b2 = 0

while (s >= v2):
    if s%v1 == 0:
        break
    s -= v2
    b2 += 1

while (s >= v1):
    s -= v1
    b1 +=1

if (s != 0):
    print("Impossible")
else:
    print(b1,b2)
    