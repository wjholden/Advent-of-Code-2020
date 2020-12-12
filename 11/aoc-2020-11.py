with open('example.txt') as f:
    input = [list(line.strip()) for line in f.readlines()]

def seat_shuffle(A):
    m = len(A)
    n = len(A[0])
    print(m, n)
    B = [['.'] * n for i in range(m)]
    print(len(B), len(B[0]))
    for (row, col) in ((row, col) for row in range(m) for col in range(n)):
        if A[row][col] == 'L':
            B[row][col] = '#'
    return B

def print_matrix(M):
    for line in M:
        for e in line:
            print(e,end = '')
        print()

print_matrix(input)
print_matrix(seat_shuffle(input))

