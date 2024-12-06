with open("044.txt") as f:
    test = [line.strip() for line in f.readlines()[:-1] if line.strip()]

directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
directions2 = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

count = 0

# First Answer
for row in range(len(test)):
    for col in range(len(test[0])):
        for dx, dy in directions:
            if 0 <= row + dx * 3 < len(test) and 0 <= col + dy * 3 < len(test[0]):
                if (
                    test[row][col] == "X"
                    and test[row + dx][col + dy] == "M"
                    and test[row + dx * 2][col + dy * 2] == "A"
                    and test[row + dx * 3][col + dy * 3] == "S"
                ):
                    count += 1
print(count)
count = 0
# Second Answer
edges = ["MAS", "SAM"]
for row in range(len(test)):
    for col in range(len(test[0])):
        if test[row][col] != "A":
            continue

        if (
            0 <= row - 1
            and row + 1 < len(test)
            and 0 <= col - 1
            and col + 1 < len(test[0])
        ):
            diagonal1 = test[row - 1][col - 1] + test[row][col] + test[row + 1][col + 1]
            diagonal2 = test[row - 1][col + 1] + test[row][col] + test[row + 1][col - 1]
            if (diagonal1 == "MAS" or diagonal1 == "SAM") and (
                diagonal2 == "MAS" or diagonal2 == "SAM"
            ):
                count += 1


print(count)
