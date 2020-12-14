'''
For testing:

BaseInstructions = [
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",   # this needs to be changed to nop to avoid loop
        "acc +6"
        ]
'''

BaseInstructions = open('input.txt', 'r').readlines()

ACC = 0

def execute(instructions):
    '''
        runs through each line of the code, executing it accordingly.
        before it runs a line, it checks to see if that particular line
        has been run once before. if so, we know we have a loop.
    '''
    global ACC
    # reset ACC to 0 because we want only to count the ACC value for this
    # single iteration that has a single line changed
    ACC = 0
    # execute the instructions and return the line number at which loop occurs
    completedIndexes = []
    lineIndex = 0
    while lineIndex < len(instructions):
        # first test to make sure if this line has been repeated
        if lineIndex in completedIndexes:
            return False
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
    # looped through all instructions without a double-line execution
    return True

def swapLine(i):
    '''
        resets the instructions to the original version, then swaps the one
        line at index i and returns the new instructions to be tested.
    '''

    # copy the original instructions
    instructions = BaseInstructions.copy()
    lineArray = instructions[i].split(' ')

    # inelegant but straightforward toggle of jmp/nop
    if lineArray[0] == "jmp":
        lineArray[0] = "nop"
        instructions[i] = ' '.join(lineArray)
    elif lineArray[0] == "nop":
        lineArray[0] = "jmp"
        instructions[i] = ' '.join(lineArray)
    
    # return the new instructions to check, with a single line switched
    return instructions



# array of lines we've already tried swapping, to prevent infinite loop
# of trying the same line over and over
triedLines = []

def part2(instructions):
    '''
        check if execute() returns true, in which case this particular version of
        the instructions executes fine.
        if false, iterate through the lines, finding the first line that hasn't been
        tried yet (not in triedLines). swap that line and call this function again
        with the new instructions and try again.
    '''
    global triedLines

    # if this executes fine and returns True, great! done.
    if execute(instructions):
        print(ACC)
    
    # otherwise,
    else:
        # iterate through each line
        i = 0
        while i < len(instructions):

            # if the line hasn't been tried before
            if i not in triedLines:

                # get a new set of instructions with this new line swapped
                instructions = swapLine(i)
                triedLines.append(i)
                break
        
            i += 1
        
        # with the new instructions, with one line swapped, try to run it again
        part2(instructions)


# run main program
part2(BaseInstructions)