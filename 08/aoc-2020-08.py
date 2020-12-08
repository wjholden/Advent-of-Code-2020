def read_input(filename):
    with open(filename) as f:
        for line in f.readlines():
            instruction, operation = line.split()
            yield instruction, int(operation)

def execute_instruction(instructions, ip, acc):
    instruction, operation = instructions[ip]
    if instruction == 'nop':
        return (ip + 1, acc)
    elif instruction == 'acc':
        return (ip + 1, acc + operation)
    elif instruction == 'jmp':
        return (ip + operation, acc)
    raise ValueError('unknown instruction')

def run_program(instructions):
    acc = 0
    ip = 0
    executed = set()
    while not ip in executed and (0 <= ip < len(instructions)):
        executed.add(ip)
        (ip, acc) = execute_instruction(instructions, ip, acc)
    if ip == len(instructions):
        return ("Completed successfully", ip, acc)
    else:
        return ("Infinite loop detected", ip, acc)

def find_corrupt_instruction(instructions):
    for i in range(len(instructions)):
        instruction, operation = instructions[i]
        if instruction == 'nop':
            instructions[i] = ('jmp', operation)
        elif instruction == 'jmp':
            instructions[i] = ('nop', operation)
        if instruction == 'nop' or instruction == 'jmp':
            result, ip, acc = run_program(instructions)
            if result == "Completed successfully":
                return (result, ip, acc)
        instructions[i] = (instruction, operation)

instructions = list(read_input('input.txt'))

print("Part 1:", run_program(instructions))
print("Part 2:", find_corrupt_instruction(instructions))