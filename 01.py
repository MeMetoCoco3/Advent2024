with open("01.txt", "r") as f:
    parsed = [line.strip().split("   ") for line in f if line.strip()]


l0 = sorted(int(x[0]) for x in parsed)
l1 = sorted(int(x[1]) for x in parsed)

print(sum([abs(x[0] - x[1]) for x in zip(l0, l1)]))

similarityList = []
for i in l0:
    similarityList.append(l1.count(i) * i)

print(sum(similarityList))
