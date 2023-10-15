n = int(input())
if n >= 100:
    exit()
for i in range(n):
    a = int(input())
    flag = 0
    for j in range(1, a+1):
        if (a%j == 0):
            flag += 1
    
    if(flag == 2):
        print("%d eh primo" %a)
    else:
        print("%d nao eh primo" %a)
        