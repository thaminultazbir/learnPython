age = 0
count = 0
while True:
    n = int(input())

    if(n < 0):
        break
    else:
        age += n
        count += 1

print("%0.2f" % (age/count))