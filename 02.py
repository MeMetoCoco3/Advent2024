def check(arr) -> int:
    print(arr)
    asc = False
    desc = False
    safe = -1
    previous_num = arr[0]
    for i, num in enumerate(arr[1:]):
        dif = num - previous_num
        if dif > 0:
            asc = True
        if dif < 0:
            desc = True
        if abs(dif) > 3 or (asc and desc) or dif == 0:
            safe = i
            break
        previous_num = num
    return safe


def check_all(arr):
    for i in range(len(arr)):
        data = arr[:i] + arr[i + 1 :]
        if check(data) == -1:
            return True
    return False


with open("02.txt", "r") as f:
    data = [
        list(map(int, line.strip().split(" ")))
        for line in f.readlines()
        if line.strip()
    ]

count = 0

while data:
    index = check(data[0])
    if index == -1:
        count += 1
    else:
        if check_all(data[0]):
            count += 1
    del data[0]
print(count)
