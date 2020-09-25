l = []
while True:
    s = input()
    if s == "end":
        break
    l.append(s)

for s in l:
    o = s.replace("    ", "\\t")
    print(f"\"{o}\",")