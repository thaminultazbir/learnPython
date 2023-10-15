n = int(input())
if n >= 100:
    exit()
for i in range(n):
    a = int(input())
    sum = 0
    for j in range(1,a-1):
        if (a%j == 0):
            sum = sum + j
    
    if (sum == a):
        print("%d eh perfeito" %a)
    else:
        print("%d nao eh perfeito" %a)