n = int(input("Nhập số nguyên dương n: "))
t = n
print(n, "=", end=" ")
i = 2
while t > 1:
    if t % i == 0:
        print(i, end="")
        t //= i
        if t > 1:
            print(".", end="")
    else:
        i += 1