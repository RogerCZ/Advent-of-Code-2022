

def day1():
    file = open("inputs/day1_1.txt", "r")
    top1 = 0
    top2 = 0
    top3 = 0
    total = 0
    for line in file.readlines():
        if line == "\n":
            if total > top1:
                top3 = top2
                top2 = top1
                top1 = total
            elif total > top2:
                top3 = top2
                top2 = total
            elif total > top3:
                top3 = total
            total = 0
        else:
            total += int(line.strip())
    if total > top1:
        top3 = top2
        top2 = top1
        top1 = total
    elif total > top2:
        top3 = top2
        top2 = total
    elif total > top3:
        top3 = total
    print("Top calories: " + str(top1))
    print("Top 3 calories sum: " + str(top1 + top2 + top3))


day1()
