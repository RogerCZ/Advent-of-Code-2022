import itertools
import copy

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


def day3():
    file = open("inputs/day3_1.txt", "r")
    prio_count = 0
    group_prio_count = 0
    group = []
    for line in file.readlines():
        first = line[:- int((len(line) / 2) + 1)]
        second = line[int(len(line) / 2):-1]
        flag = False
        for c1 in first:
            for c2 in second:
                if c1 == c2:
                    if c1.islower():
                        prio = ord(c1) - 96
                    else:
                        prio = ord(c1) - 38
                    prio_count += prio
                    flag = True
                    break
            if flag:
                break
        group.append(line[:-1])
        if len(group) == 3:
            flag = False
            for c1 in group[0]:
                for c2 in group[1]:
                    for c3 in group[2]:
                        if c1 == c2 and c2 == c3:
                            if c1.islower():
                                prio = ord(c1) - 96
                            else:
                                prio = ord(c1) - 38
                            group_prio_count += prio
                            flag = True
                            break
                    if flag:
                        break
                if flag:
                    break
            group.clear()
    print("Part 1 priority count: " + str(prio_count))
    print("Part 2 priority count: " + str(group_prio_count))


def day4():
    file = open("inputs/day4_1.txt", "r")
    complete_overlaps = 0
    partial_overlaps = 0
    for line in file.readlines():
        first_min = int(line[:-1].split(",")[0].split("-")[0])
        first_max = int(line[:-1].split(",")[0].split("-")[1])
        second_min = int(line[:-1].split(",")[1].split("-")[0])
        second_max = int(line[:-1].split(",")[1].split("-")[1])
        # print(first_min, first_max, second_min, second_max)
        if (first_min >= second_min and first_max <= second_max) or (
                second_min >= first_min and second_max <= first_max):
            complete_overlaps += 1
        elif (second_min <= first_min <= second_max) \
                or (second_min <= first_max <= second_max) \
                or (first_min <= second_min <= first_max) \
                or (first_min <= second_max <= first_max):
            partial_overlaps += 1
    print("Number of complete overlaps: " + str(complete_overlaps))
    print("NUmber of all overlaps: " + str(partial_overlaps + complete_overlaps))


def day5():
    file = open("inputs/day5_1.txt", "r")
    stacks = list()
    process = list()
    number_of_stacks = 0
    stack_input = list()
    blank_line = False
    for line in file.readlines():
        if line == "\n":
            blank_line = True
            continue
        if not blank_line:
            stack_input.append(line[:-1])
        else:
            command = list()
            command.append(int(line[:-1].split("move ")[1].split(" from")[0]))
            command.append(int(line[:-1].split("from ")[1].split(" to")[0]))
            command.append(int(line[:-1].split("to ")[1]))
            process.append(command)
    number_of_stacks = int(stack_input.pop().split(" ")[-1])
    for i in range(number_of_stacks):
        stacks.append(list())
    for level in stack_input:
        for i in range(number_of_stacks):
            index = 1 + i * 4
            if index > len(level):
                break
            if level[index] == ' ':
                continue
            stacks[i].append(level[index])
    for i in range(number_of_stacks):
        stacks[i].reverse()
    old_stacks = copy.deepcopy(stacks)
    for p in process:
        for n in range(p[0]):
            stacks[p[2]-1].append(stacks[p[1]-1].pop())
    top_crates = ""
    for stack in stacks:
        top_crates += stack[-1]
    print("Part 1: " + top_crates)
    for p in process:
        old_stacks[p[2]-1] += old_stacks[p[1]-1][-p[0]:]
        del old_stacks[p[1]-1][-p[0]:]
        # print(old_stacks)
    top_crates = ""
    for stack in old_stacks:
        top_crates += stack[-1]
    print("Part 2: " + top_crates)


# day1()
# day2()
# day3()
# day4()
day5()
