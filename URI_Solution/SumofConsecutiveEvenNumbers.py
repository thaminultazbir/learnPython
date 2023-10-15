while True:
    a = int(input())
    if a == 0:
        break
    else:
        if (a%2 == 0):
            c = 0
            for j in range(5):
                c = c+a
                a = a+2
            print(c)
        
        else:
            a += 1
            c = 0
            for j in range(5):
                c+=a
                a+=2
            print(c)