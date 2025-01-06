peak = 1000

for a in range(1,1000):
    for b in range(a+1,1000):
        for c in range(b+1,1000):
            if a + b + c == 1000:
                if (a**2) + (b**2) == (c**2):
                    answer = a*b*c
                    print("Answer:",answer)
                    print(f"Numbers : {a},{b},{c}")
                    break


