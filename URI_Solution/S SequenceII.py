sum = 0

denominator = 1

for i in range(1, 40):
    if i % 2 == 1:
        neumerator = i
        frac = neumerator / denominator
        denominator = denominator * 2
        sum = sum + frac


print("%0.2f" %sum)
