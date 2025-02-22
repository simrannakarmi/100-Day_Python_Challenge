text = input("Enter a String: ").lower()
D = {}

for s in text:
    if s not in D:
        D[s] = 1
    else:
        D[s] += 1
        
print(D)