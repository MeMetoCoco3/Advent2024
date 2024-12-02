import re

pat = r"(do\(\)|don't\(\))|mul\((\d{1,3}),(\d{1,3})\)"


with open("03.txt", "r") as f:
    data = f.read()

g = re.findall(pat, data)


def mul(a, b):
    return int(a) * int(b)


count = 0
do = True
for i in g:
    print(i)
    if i[0] == "do()":
        do = True
        continue
    elif i[0] == "don't()":
        do = False
        continue
    if do:
        res = mul(i[1], i[2])
        count += res

print(count)
