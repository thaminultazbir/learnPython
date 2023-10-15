X = int(input())
Z = 0

while True:
    Z = int(input())
    if(Z > X):
        break

SUM = X
Flag = 1
while (SUM < Z):
    SUM = SUM + X + Flag
    Flag+=1

print(Flag)