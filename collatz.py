def collatz(i):
    print(i)
    while (i!=1):
        if (i%2==0):
            i = i // 2
        else:
            i = i * 3 + 1
        print(i)

def col(i):
    if (i%2==0):
            i = i // 2
    else:
        i = i * 3 + 1
    print(i)
    return i



# collatz()

s = 3
while (s!=1):
    s = col(s)