import collections
import itertools
import copy
from anytree import Node, RenderTree, find_by_attr, find, PostOrderIter, PreOrderIter
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time
import math
import sys
import ast
import os
import sparse

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
            stacks[p[2] - 1].append(stacks[p[1] - 1].pop())
    top_crates = ""
    for stack in stacks:
        top_crates += stack[-1]
    print("Part 1: " + top_crates)
    for p in process:
        old_stacks[p[2] - 1] += old_stacks[p[1] - 1][-p[0]:]
        del old_stacks[p[1] - 1][-p[0]:]
        # print(old_stacks)
    top_crates = ""
    for stack in old_stacks:
        top_crates += stack[-1]
    print("Part 2: " + top_crates)


def day6():
    file = open("inputs/day6_1.txt", "r")
    line = file.readline()
    index = 0
    marker = list()
    flag_duplicit = False
    for c in line:
        flag_duplicit = False
        if index < 4:
            marker.append(c)
            index += 1
            continue
        for i in range(3):
            for j in range(i + 1, 4):
                if marker[i] == marker[j]:
                    flag_duplicit = True
                    break
            if flag_duplicit:
                break
        if flag_duplicit:
            marker.pop(0)
            marker.append(c)
            index += 1
            continue
        print("Part 1: " + str(index))
        break

    index = 0
    message = list()
    for c in line:
        flag_duplicit = False
        if index < 14:
            message.append(c)
            index += 1
            continue
        for i in range(13):
            for j in range(i + 1, 14):
                if message[i] == message[j]:
                    flag_duplicit = True
                    break
            if flag_duplicit:
                break
        if flag_duplicit:
            message.pop(0)
            message.append(c)
            index += 1
            continue
        print("Part 2: " + str(index))
        break


def day7():
    file = open("inputs/day7_1.txt", "r")
    root = Node("root", size=0)
    current_dir = root
    for line in file.readlines():
        # print(current_dir)
        parts = line[:-1].split(" ")
        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "/":
                    current_dir = root
                elif parts[2] == "..":
                    current_dir = current_dir.parent
                else:
                    current_dir = find(current_dir,
                                       lambda n: n.name == parts[2] and n in current_dir.children,
                                       maxlevel=2)
                    # print(current_dir, parts[2])
        elif parts[0] == "dir":
            Node(parts[1], parent=current_dir, size=0)
        else:
            Node(parts[1], parent=current_dir, size=int(parts[0]))
    for node in PostOrderIter(root):
        if not node.is_root:
            node.parent.size += node.size
    size_sum = 0
    for node in PreOrderIter(root):
        if not node.is_leaf and node.size <= 100000:
            size_sum += node.size
    for pre, fill, node in RenderTree(root):
        print("%s%s %d" % (pre, node.name, node.size))
    print("\nPart 1: " + str(size_sum))
    unused_space = 70000000 - root.size
    required_space = 30000000
    candidate = 0
    for node in PostOrderIter(root):
        if not node.is_leaf and node.size + unused_space >= required_space:
            if node.size < candidate or candidate == 0:
                candidate = node.size
    print("Part 2: " + str(candidate))


def day8():
    file = open("inputs/day8_1.txt", "r")
    mat = list()
    for line in file.readlines():
        arr = list()
        for c in line[:-1]:
            arr.append(int(c))
        mat.append(arr)
    mat = np.array(mat)

    # ax = sns.heatmap(mat, cmap=sns.color_palette("dark:green", as_cmap=True), yticklabels=False, xticklabels=False)
    # plt.show()
    size = mat[0].size
    visible_count = (size + size - 2) * 2
    highest_score = 0
    for y in range(1, size - 1):
        for x in range(1, size - 1):
            visible_flags = [True, True, True, True]
            i = x - 1
            j = y - 1
            partial_score = 0
            score = 1
            while i >= 0:
                if mat[y][x] <= mat[y][i]:
                    visible_flags[0] = False
                    partial_score += 1
                    break
                partial_score += 1
                i -= 1
            score *= partial_score
            partial_score = 0
            i = x + 1
            while i < size:
                if mat[y][x] <= mat[y][i]:
                    visible_flags[1] = False
                    partial_score += 1
                    break
                partial_score += 1
                i += 1
            score *= partial_score
            partial_score = 0
            while j >= 0:
                if mat[y][x] <= mat[j][x]:
                    visible_flags[2] = False
                    partial_score += 1
                    break
                partial_score += 1
                j -= 1
            j = y + 1
            score *= partial_score
            partial_score = 0
            while j < size:
                if mat[y][x] <= mat[j][x]:
                    visible_flags[3] = False
                    partial_score += 1
                    break
                partial_score += 1
                j += 1
            score *= partial_score
            if True in visible_flags:
                visible_count += 1
            if score > highest_score:
                highest_score = score
    print("Part 1: " + str(visible_count))
    print("Part 2: " + str(highest_score))


def day9():
    file = open("inputs/day9_1.txt", "r")
    x = 0
    y = 1
    # head_coords = [0, 0]
    knot_coords = list()
    for a in range(10):
        knot_coords.append([0, 0])
    tail_history = [set(), set()]
    for line in file.readlines():
        direction = line[:-1].split(" ")[0]
        moves = int(line[:-1].split(" ")[1])
        for i in range(moves):

            if direction == "R":
                knot_coords[0][x] += 1
            elif direction == "L":
                knot_coords[0][x] -= 1
            elif direction == "U":
                knot_coords[0][y] += 1
            else:
                knot_coords[0][y] -= 1

            for n in range(1, 10):
                if knot_coords[n - 1][x] == knot_coords[n][x] - 2 and knot_coords[n - 1][y] == knot_coords[n][y]:
                    knot_coords[n][x] -= 1
                elif knot_coords[n - 1][y] == knot_coords[n][y] - 2 and knot_coords[n - 1][x] == knot_coords[n][x]:
                    knot_coords[n][y] -= 1
                elif knot_coords[n - 1][x] == knot_coords[n][x] + 2 and knot_coords[n - 1][y] == knot_coords[n][y]:
                    knot_coords[n][x] += 1
                elif knot_coords[n - 1][y] == knot_coords[n][y] + 2 and knot_coords[n - 1][x] == knot_coords[n][x]:
                    knot_coords[n][y] += 1
                elif knot_coords[n - 1][x] == knot_coords[n][x] - 2 and knot_coords[n - 1][y] == knot_coords[n][y] + 1 \
                        or knot_coords[n - 1][x] == knot_coords[n][x] - 1 and knot_coords[n - 1][y] == knot_coords[n][
                    y] + 2 \
                        or knot_coords[n - 1][x] == knot_coords[n][x] - 2 and knot_coords[n - 1][y] == knot_coords[n][
                    y] + 2:
                    knot_coords[n][x] -= 1
                    knot_coords[n][y] += 1
                elif knot_coords[n - 1][x] == knot_coords[n][x] - 2 and knot_coords[n - 1][y] == knot_coords[n][y] - 1 \
                        or knot_coords[n - 1][x] == knot_coords[n][x] - 1 and knot_coords[n - 1][y] == knot_coords[n][
                    y] - 2 \
                        or knot_coords[n - 1][x] == knot_coords[n][x] - 2 and knot_coords[n - 1][y] == knot_coords[n][
                    y] - 2:
                    knot_coords[n][x] -= 1
                    knot_coords[n][y] -= 1
                elif knot_coords[n - 1][x] == knot_coords[n][x] + 1 and knot_coords[n - 1][y] == knot_coords[n][y] - 2 \
                        or knot_coords[n - 1][x] == knot_coords[n][x] + 2 and knot_coords[n - 1][y] == knot_coords[n][
                    y] - 1 \
                        or knot_coords[n - 1][x] == knot_coords[n][x] + 2 and knot_coords[n - 1][y] == knot_coords[n][
                    y] - 2:
                    knot_coords[n][x] += 1
                    knot_coords[n][y] -= 1
                elif knot_coords[n - 1][x] == knot_coords[n][x] + 2 and knot_coords[n - 1][y] == knot_coords[n][y] + 1 \
                        or knot_coords[n - 1][x] == knot_coords[n][x] + 1 and knot_coords[n - 1][y] == knot_coords[n][
                    y] + 2 \
                        or knot_coords[n - 1][x] == knot_coords[n][x] + 2 and knot_coords[n - 1][y] == knot_coords[n][
                    y] + 2:
                    knot_coords[n][x] += 1
                    knot_coords[n][y] += 1

            tail_history[0].add(str(knot_coords[1][x]) + ";" + str(knot_coords[1][y]))
            tail_history[1].add(str(knot_coords[9][x]) + ";" + str(knot_coords[9][y]))
    print("Part 1: " + str(len(tail_history[0])))
    print("Part 2: " + str(len(tail_history[1])))


def day10():
    file = open("inputs/day10_1.txt", "r")
    x = 1
    cycle = 1
    check_cycle = 20
    check_sum = 0
    pixels = list()
    for line in file.readlines():
        command = line[:-1].split(" ")[0]
        if command == "noop":
            if cycle == check_cycle:
                check_sum += check_cycle * x
                check_cycle += 40
            if cycle == 240:
                print("Part 1: " + str(check_sum))
                # return
            modulo_cycle = (cycle - 1) % 40
            if x == modulo_cycle or x - 1 == modulo_cycle or x + 1 == modulo_cycle:
                pixels.append(1)
            else:
                pixels.append(0)
            cycle += 1
            continue
        value = int(line[:-1].split(" ")[1])
        for i in range(2):
            if cycle == check_cycle:
                check_sum += check_cycle * x
                check_cycle += 40
            if cycle == 240:
                print("Part 1: " + str(check_sum))
                # return
            modulo_cycle = (cycle - 1) % 40
            if x == modulo_cycle or x - 1 == modulo_cycle or x + 1 == modulo_cycle:
                pixels.append(1)
            else:
                pixels.append(0)
            if i == 1:
                x += value
            cycle += 1
    screen = ""
    for i in range(len(pixels)):
        if (i + 1) % 40 == 0:
            screen += "\n"
        elif pixels[i] == 0:
            screen += u"\u2591"
        else:
            screen += u"\u2588"
    print(screen)


def day11():
    file = open("inputs/day11_1.txt", "r")
    monkeys = list()
    monkey = dict()
    for line in file.readlines():
        while line[0] == " ":
            line = line[1:]
        row_id = line.split(" ")[0:2]
        if row_id[0] == "\n":
            continue
        elif row_id == "Monkey":
            continue
        elif row_id[0] == "Starting":
            items = list()
            for item in line[:-1].split(": ")[1].split(", "):
                items.append(int(item))
            monkey["items"] = items
        elif row_id[0] == "Operation:":
            operation = dict()
            operation["operator"] = line.split(" ")[4]
            operation["value"] = line[:-1].split(" ")[5]
            monkey["operation"] = operation
        elif row_id[0] == "Test:":
            test_value = int(line[:-1].split(" ")[-1])
            monkey["test_value"] = test_value
        elif row_id[1] == "true:":
            monkey["true_id"] = int(line[:-1].split(" ")[-1])
        elif row_id[1] == "false:":
            monkey["false_id"] = int(line[:-1].split(" ")[-1])
            monkeys.append(monkey.copy())
            monkey.clear()
    # print(monkeys)
    # 20 for part 1
    rounds = 10000
    inspections_count = list()
    for i in range(len(monkeys)):
        inspections_count.append(0)
    divisors = list()
    for monkey in monkeys:
        divisors.append(monkey["test_value"])
    lcm = math.lcm(*divisors)

    for my_round in range(rounds):
        # print("Round: " + str(my_round + 1))
        monkey_id = 0
        for monkey in monkeys:
            for i in range(len(monkey["items"])):
                item = monkey["items"].pop(0)

                if monkey["operation"]["value"] == "old":
                    value = item
                else:
                    value = int(monkey["operation"]["value"])

                if monkey["operation"]["operator"] == "*":
                    item *= value
                else:
                    item += value
                # Uncomment for part 1
                # item //= 3

                # uncomment for part 2
                if item > lcm:
                    reminder = item % lcm
                    if reminder == 0:
                        item = lcm
                    else:
                        item = reminder

                if item % monkey["test_value"] == 0:
                    monkeys[monkey["true_id"]]["items"].append(item)
                else:
                    monkeys[monkey["false_id"]]["items"].append(item)
                inspections_count[monkey_id] += 1
            monkey_id += 1
    inspections_count.sort()
    monkey_business = inspections_count[-1] * inspections_count[-2]
    print(monkey_business)


def bfs(grid, start, width, height):
    queue = collections.deque([[start]])
    seen = {start}
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        # print(chr(grid[y][x] + ord('a') - 1))
        if grid[y][x] == 27:
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] <= (grid[y][x] + 1) and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    return -1


def day12():
    file = open("inputs/day12_1.txt")
    matrix = list()
    start = (0, 0)
    for line in file.readlines():
        row = list()
        for c in line[:-1]:
            if c == 'S':
                row.append(0)
            elif c == 'E':
                row.append(ord('z') - ord('a') + 2)
            else:
                row.append(ord(c) - ord('a') + 1)
        matrix.append(row)

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 0:
                start = (x, y)

    path = bfs(matrix, start, len(matrix[0]), len(matrix))
    print("Part 1: " + str(len(path) - 1))

    matrix[start[1]][start[0]] = 1
    shortest = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 1:
                path = bfs(matrix, (x, y), len(matrix[0]), len(matrix))
                if path != -1:
                    if shortest == 0 or len(path) - 1 < shortest:
                        shortest = len(path) - 1
    print("Part 2: " + str(shortest))


def compare_pair(left, right):
    if type(left) is type(right):
        if type(left) == int:
            if left < right:
                return 1
            elif left == right:
                return 0
            else:
                return -1
        elif type(left) == list:
            if len(left) < len(right):
                for i in range(len(left)):
                    ret = compare_pair(left[i], right[i])
                    if ret == 1:
                        return 1
                    elif ret == -1:
                        return -1
                return 1
            elif len(left) > len(right):
                for i in range(len(right)):
                    ret = compare_pair(left[i], right[i])
                    if ret == 1:
                        return 1
                    elif ret == -1:
                        return -1
                return -1
            else:
                for i in range(len(right)):
                    ret = compare_pair(left[i], right[i])
                    if ret == 1:
                        return 1
                    elif ret == -1:
                        return -1
                return 0
    elif type(left) == int:
        return compare_pair([left], right)
    else:
        return compare_pair(left, [right])


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if compare_pair(array[j], array[j + 1]) != 1:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array


def day13():
    file = open("inputs/day13_1.txt", "r")
    pairs = list()
    pair = list()
    indices_sum = 0
    for line in file.readlines():
        if line == "\n":
            pairs.append(pair.copy())
            pair.clear()
            continue
        pair.append(ast.literal_eval(line[:-1]))
    pairs.append(pair.copy())

    for i in range(len(pairs)):
        if compare_pair(pairs[i][0], pairs[i][1]) == 1:
            indices_sum += i + 1
    print("Part 1: " + str(indices_sum))

    array = list()
    array.append([[2]])
    array.append([[6]])
    for pair in pairs:
        array.append(pair[0].copy())
        array.append(pair[1].copy())

    array = bubble_sort(array)

    # for line in array:
    # print(line)

    decoder_key = 1
    for i in range(len(array)):
        packet = array[i]
        if packet == [[2]] or packet == [[6]]:
            decoder_key *= i + 1
    print("Part 2: " + str(decoder_key))


def day14():
    file = open("inputs/day14_1.txt", "r")
    limit_coords = [1000, 1000, 0, 0]
    structures = list()
    for line in file.readlines():
        coords = list()
        for coord in line[:-1].split(" -> "):
            coords.append([int(coord.split(",")[0]), int(coord.split(",")[1])])
            if coords[-1][0] < limit_coords[0]:
                limit_coords[0] = coords[-1][0]
            elif coords[-1][0] > limit_coords[2]:
                limit_coords[2] = coords[-1][0]
            elif coords[-1][1] < limit_coords[1]:
                limit_coords[1] = coords[-1][1]
            elif coords[-1][1] > limit_coords[3]:
                limit_coords[3] = coords[-1][1]
        structures.append(coords.copy())

    scan = np.zeros((limit_coords[3] + 3, limit_coords[2] + 2), dtype=int)
    scan[-1] = np.ones(len(scan[-1]), dtype=int)
    for structure in structures:
        for i in range(len(structure) - 1):
            if structure[i][1] < structure[i+1][1]:
                y1 = structure[i][1]
                y2 = structure[i+1][1]
            else:
                y1 = structure[i+1][1]
                y2 = structure[i][1]

            if structure[i][0] < structure[i+1][0]:
                x1 = structure[i][0]
                x2 = structure[i+1][0]
            else:
                x1 = structure[i+1][0]
                x2 = structure[i][0]

            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    scan[y][x] = 1

    sand_source = [500, 0]

    rested_count = 0
    rested_coord = [0, 0]
    [x, y] = sand_source.copy()
    # 'while y != len(scan) - 1' for part 1
    while rested_coord != [500, 0]:
        if x < 1:
            col = np.zeros((len(scan), 1), dtype=int)
            col[-1] = 1
            scan = np.hstack((col, scan))
        elif x > len(scan[0]) - 2:
            col = np.zeros((len(scan), 1), dtype=int)
            col[-1] = 1
            scan = np.hstack((scan, col))
        if scan[y+1][x] == 0:
            scan[y][x] = 0
            scan[y+1][x] = 1
            y += 1
        elif scan[y+1][x - 1] == 0:
            scan[y][x] = 0
            scan[y + 1][x - 1] = 1
            y += 1
            x -= 1
        elif scan[y+1][x+1] == 0:
            scan[y][x] = 0
            scan[y+1][x+1] = 1
            y += 1
            x += 1
        else:
            scan[y][x] = 2
            rested_coord = [x, y]
            [x, y] = sand_source.copy()
            rested_count += 1
    print("Part 2: " + str(rested_count))


def day15():
    file = open("inputs/day15_1.txt", "r")
    pairs = list()
    for line in file.readlines():
        coords = line.split(" ")
        pairs.append([[int(coords[2][:-1].split("=")[1]), int(coords[3][:-1].split("=")[1])],
                      [int(coords[-2][:-1].split("=")[1]), int(coords[-1][:-1].split("=")[1])]])

    modifiers = [0, 0]
    dimensions = [0, 0]
    for [[x1, y1], [x2, y2]] in pairs:
        if x1 + modifiers[0] > dimensions[0]:
            dimensions[0] = x1 + modifiers[0]
        elif x1 < 0 and abs(x1) > modifiers[0]:
            dimensions[0] += abs(x1) - modifiers[0]
            modifiers[0] = abs(x1)
        if x2 + modifiers[0] > dimensions[0]:
            dimensions[0] = x2 + modifiers[0]
        elif x2 < 0 and abs(x2) > modifiers[0]:
            dimensions[0] += abs(x2) - modifiers[0]
            modifiers[0] = abs(x2)
        if y1 + modifiers[1] > dimensions[1]:
            dimensions[1] = y1 + modifiers[1]
        elif y1  < 0 and abs(y1) > modifiers[1]:
            dimensions[1] += abs(y1) - modifiers[1]
            modifiers[1] = abs(y1)
        if y2 + modifiers[1] > dimensions[1]:
            dimensions[1] = y2 + modifiers[1]
        elif y2 < 0 and abs(y2) > modifiers[1]:
            dimensions[1] += abs(y2) - modifiers[1]
            modifiers[1] = abs(y2)

    # scan = np.zeros((dimensions[1] + 1, dimensions[0] + 1), dtype=np.int8)
    scan = np.zeros((1, dimensions[0] + 1), dtype=np.int8)

    line = 10
    for [[x1, y1], [x2, y2]] in pairs:
        # remove for part 1
        break
        x1 += modifiers[0]
        x2 += modifiers[0]
        y1 += modifiers[1]
        y2 += modifiers[1]
        man_dist = abs(x1 - x2) + abs(y1 - y2)

        for i in range(-man_dist, man_dist + 1):
            if y1 + i == line + modifiers[1]:
                if y1 + i < 0:
                    #row = np.zeros((abs(y1 + i), len(scan[0])), dtype=np.int8)
                    # scan = np.vstack((row, scan))
                    modifiers[1] += abs(y1 + i)
                    y1 += abs(y1 + i)
                    y2 += abs(y1 + i)
                if y1 + i > len(scan) - 1:
                    pass
                    # row = np.zeros((1, len(scan[0])), dtype=np.int8)
                    # scan = np.vstack((scan, row))
                for j in range(abs(i)-man_dist, man_dist+1-abs(i)):
                    if x1 + j < 0:
                        col = np.zeros((len(scan), abs(x1 + i)), dtype=np.int8)
                        scan = np.hstack((col, scan))
                        modifiers[0] += abs(x1 + i)
                        x1 += abs(x1 + i)
                        x2 += abs(x1 + i)
                    if x1 + j > len(scan[0]) - 1:
                        col = np.zeros((len(scan), 1), dtype=np.int8)
                        scan = np.hstack((scan, col))
                    if y1 + i == line + modifiers[1]:
                        scan[0][x1 + j] = 1
        if y1 == line + modifiers[1]:
            scan[0][x1] = 0
        if y2 == line + modifiers[1]:
            scan[0][x2] = 0

    for row in scan:
        for x in row:
            if x == 0:
                pass
                # print(".", end="")
            else:
                pass
                # print("#", end="")
        # print()
    print("Part 1: " + str(np.sum(scan[0])))

    sensors = list()
    for [[x1, y1], [x2, y2]] in pairs:
        sensor = [[x1, y1], abs(x1 - x2) + abs(y1 - y2)]
        sensors.append(sensor)

    for i in range(0, 4000000):
        limits = list()
        close_sensors = list()
        for item in sensors:
            if abs(item[0][1] - i) <= item[1]:
                close_sensors.append(item)
        for [[x, y], r] in close_sensors:
            y_dist = abs(y - i)
            x_max = (r - y_dist)
            start = x - x_max
            end = x + x_max
            limits.append([start, end])

        limits.sort()
        stack = list()
        stack.append(limits[0])
        for limit in limits:
            if stack[-1][0] <= limit[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], limit[-1])
            else:
                stack.append(limit)
        if len(stack) > 1:
            for a in range(len(stack) - 1):
                diff = abs(stack[a][1] - stack[a+1][0])
                if diff == 2:
                    tuning_freq = (stack[a][1] + 1) * 4000000 + i
                    print("Part 2: ", str(tuning_freq))
                    return


start_time = time.time()
# day1()
# day2()
# day3()
# day4()
# day5()
# day6()
# day7()
# day8()
# day9()
# day10()
# day11()
# day12()
# day13()
# day14()
day15()
print("--- %s seconds ---" % (time.time() - start_time))
