operators = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y
}

def eval_lr(s):
    s = s.strip()
    #print(s)
    if s[-1] == ')':
        p_count = 1
        i = len(s) - 2
        while p_count > 0 and i > 0:
            if s[i] == ')':
                p_count += 1
            elif s[i] == '(':
                p_count -= 1
            i -= 1
        right = eval_lr(s[i + 2:len(s) - 1])
        if i > 0:
            op = s[i - 2:i - 1]
            left = eval_lr(s[0:i - 3])
            result = operators[op](left, right)
            print(s, 'becomes', result)
            return result
        else:
            print(s, 'becomes', right)
            return right
    else:
        right = int(s[-1:])
        if len(s) > 1:
            op = s[-3:-2]
            left = eval_lr(s[:-4])
            result = operators[op](left, right)
            print(s, 'becomes', result)
            return result
        else:
            print(s, 'becomes', right)
            return right

def eval_rl(s):
    s = s.strip()
    if s[0] == '(':
        x = 1
        i = 1
        while x > 0 and i < len(s):
            if s[i] == '(':
                x += 1
            elif s[i] == ')':
                x -= 1
            i += 1
        left = eval(s[1:i - 1])
        if i == len(s):
            print(s, 'becomes', left)
            return left
        else:
            operator = s[i + 1:i + 2]
            right = eval(s[i + 3:])
            result = operators.get(operator)(left, right)
            print(s, 'becomes', result)
            return result
    else:
        left = int(s[0:1])
        if len(s) == 1:
            print(s, 'becomes', left)
            return left
        else:
            operator = s[2:3]
            right = eval(s[4:])
            result = operators.get(operator)(left, right)
            print(s, 'becomes', result)
            return result
#print(eval('1 + (2 * 3) + (4 * (5 + 6))'))

#with open('example.txt') as f:
#    print([eval(line) for line in f.readlines()])

print(eval_lr('2 * 3 + (4 * 5)'))