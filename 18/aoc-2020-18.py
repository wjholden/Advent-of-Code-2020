with open('example.txt') as f:
    lines = f.readlines()

def eval_lr(s):
    #print(s, 'length: ', len(s))
    op = {
        '*': lambda x, y: x * y,
        '+': lambda x, y: x + y
    }
    if len(s) == 1:
        return int(s)
    elif s[-1] == ')':
        # scan right to left until we find the matching left paren
        p = 1
        i = len(s) - 2
        while i > 0 and p > 0:
            if s[i] == ')':
                p += 1
            elif s[i] == '(':
                p -= 1
            i -= 1
        if i == 0:
            right = eval_lr(s[1:-1])
            return right
        else:
            right = eval_lr(s[i + 2:-1])
            left = eval_lr(s[:i - 2])
            operator = s[i - 1]
            result = op[operator](left, right)
            #print('Result:', left, operator, right, '=', result)
            return result
    elif s[-1].isdigit():
        left = eval_lr(s[:-4])
        right = int(s[-1])
        operator = s[-3]
        result = op[operator](left, right)
        #print('Result:', left, operator, right, '=', result)
        return result

part1 = [eval_lr(line.strip()) for line in lines]
print('Part 1:', sum(part1))
