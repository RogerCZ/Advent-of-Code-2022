

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


def day2():
    file = open("inputs/day2_1.txt", "r")
    total_part1 = 0
    total_part2 = 0
    for line in file.readlines():
        opponent = line[0]
        me = line[-2]
        match opponent:
            case "A":
                match me:
                    case "X":
                        total_part1 += 1 + 3
                        total_part2 += 3 + 0
                    case "Y":
                        total_part1 += 2 + 6
                        total_part2 += 1 + 3
                    case "Z":
                        total_part1 += 3 + 0
                        total_part2 += 2 + 6
            case "B":
                match me:
                    case "X":
                        total_part1 += 1 + 0
                        total_part2 += 1 + 0
                    case "Y":
                        total_part1 += 2 + 3
                        total_part2 += 2 + 3
                    case "Z":
                        total_part1 += 3 + 6
                        total_part2 += 3 + 6
            case "C":
                match me:
                    case "X":
                        total_part1 += 1 + 6
                        total_part2 += 2 + 0
                    case "Y":
                        total_part1 += 2 + 0
                        total_part2 += 3 + 3
                    case "Z":
                        total_part1 += 3 + 3
                        total_part2 += 1 + 6
    print("Part 1 total score: " + str(total_part1))
    print("Part 2 total score: " + str(total_part2))

# day1()
day2()
