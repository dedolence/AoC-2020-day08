instructions = [line.strip() for line in open('input.txt', 'r')]
ACC = 0
def part1():
    global ACC
    completedIndexes = []
    lineIndex = 0
    while lineIndex < len(instructions):
        # first test to make sure if this line has been repeated
        if lineIndex in completedIndexes:
            print("Loop detected. ACC value is ", ACC)
            break
        else:
            # no loop detected, execute instruction
            completedIndexes.append(lineIndex)
            instruction, value = instructions[lineIndex].split(" ")
            value = int(value)
            if instruction == "acc":
                ACC += value
                lineIndex += 1
            elif instruction == "jmp":
                lineIndex += value
            elif instruction == "nop":
                lineIndex += 1

part1()