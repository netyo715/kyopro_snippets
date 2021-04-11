name = input("name: ")
prefix = input("prefix: ")
description = input("description: ")
print("body: ")

body = []
while True:
    s = input()
    if s == "end":
        break
    body.append(s)

with open(f"snippets_{name}", mode="w") as f:
    f.write(f'"{name}":'+"{\n")
    f.write(f'\t"prefix": "{prefix}",\n')
    frow = body[0].replace("    ", "\\t")
    f.write(f'\t"body":["{frow}",')
    for row in body[1:]:
        rrow = row.replace("    ", "\\t")
        #print(f"\"{o}\",")
        f.write(f'\n\t\t\t"{rrow}",')
    f.write("],\n")
    f.write(f'\t"description": "{description}"\n')
    f.write("}\n")