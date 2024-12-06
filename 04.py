with open("04.txt") as f:
    test = [line.strip() for line in f.readlines() if line.strip()]
print(test[0])
print(test[-1])

# First Answer
directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
count = 0
for row in range(len(test)):
    for col in range(len(test[0])):
        for dx, dy in directions:
            if 0 <= row + dx * 3 < len(test) and 0 <= col + dy * 3 < len(test[0]):
                try:
                    if (
                        test[row][col] == "X"
                        and test[row + dx][col + dy] == "M"
                        and test[row + dx * 2][col + dy * 2] == "A"
                        and test[row + dx * 3][col + dy * 3] == "S"
                    ):
                        count += 1
                except IndexError:
                    pass
print(count)
# Second Answer
count = 0
edges = ["MAS", "SAM"]
for row in range(len(test)):
    for col in range(len(test[0])):
        if test[row][col] != "A":
            continue

        if (
            0 <= row - 1 < len(test)
            and 0 <= row + 1 < len(test)
            and 0 <= col - 1 < len(test[0])
            and 0 <= col + 1 < len(test[0])
        ):
            bl = test[row - 1][col - 1]
            tr = test[row + 1][col + 1]
            br = test[row - 1][col + 1]
            tl = test[row + 1][col - 1]
            sortedLetters = sorted([bl, tr, br, tl])
            if sortedLetters == ["M", "M", "S", "S"] and bl != tr:
                count += 1
print(count)
