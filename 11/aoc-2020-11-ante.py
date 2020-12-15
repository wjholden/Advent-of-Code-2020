with open('input.txt') as f:
    input = [list(line.strip()) for line in f.readlines()]

rows = len(input)
cols = len(input[0])

print('''
USE aoc;
DROP TABLE Seats;

CREATE TABLE Seats (x TINYINT, y TINYINT, value CHAR(1), PRIMARY KEY (x, y));

DROP TABLE Neighbors;

CREATE TABLE Neighbors (x1 TINYINT, y1 TINYINT, x2 TINYINT, y2 TINYINT, PRIMARY KEY (x1, y1, x2, y2),
FOREIGN KEY (x1, y1) REFERENCES Seats(x, y), FOREIGN KEY (x2, y2) REFERENCES Seats(x, y));
''')

print('INSERT INTO Seats (x, y, value) VALUES')
for y in range(rows):
    for x in range(cols):
        if input[y][x] == 'L':
            print(f"({x}, {y}, 'L'),")

'''
Each seat has at most 8 neighbors.
We can compute them all this way, but we actually don't need to!
Computing left is the same as right in reverse, as are the diagonals.

SELECT A.x, A.y, MIN(B.x), MIN(B.y) FROM Seats AS A, Seats AS B WHERE A.x = B.x AND A.y < B.y GROUP BY A.x, A.y; /* Below (+y is down) */
SELECT A.x, A.y, MAX(B.y), MAX(B.y) FROM Seats AS A, Seats AS B WHERE A.x = B.x AND B.y < A.y GROUP BY A.x, A.y; /* Above (-y is up) */
SELECT A.x, A.y, MIN(B.x), MIN(B.y) FROM Seats AS A, Seats AS B WHERE A.y = B.y AND B.x < A.x GROUP BY A.x, A.y; /* Left */
SELECT A.x, A.y, MAX(B.x), MAX(B.y) FROM Seats AS A, Seats AS B WHERE A.y = B.y AND A.x < B.x GROUP BY A.x, A.y; /* Right */
SELECT A.x, A.y, MIN(B.x), MIN(B.y) FROM Seats AS A, Seats AS B WHERE A.x < B.x AND A.y < B.y AND (B.y - A.y) = (B.x - A.x) GROUP BY A.x, A.y; /* Bottom right */
SELECT A.x, A.y, MIN(B.x), MAX(B.y) FROM Seats AS A, Seats AS B WHERE A.x < B.x AND B.y < A.y AND (B.y - A.y) = (A.x - B.x) GROUP BY A.x, A.y; /* Top right */

/* I don't know why, but these two are considerably faster than the above two. */
SELECT A.x, A.y, MAX(B.x), MIN(B.y) FROM Seats AS A, Seats AS B WHERE B.x < A.x AND A.y < B.y AND (B.y - A.y) = (A.x - B.x) GROUP BY A.x, A.y; /* Bottom left */
SELECT A.x, A.y, MAX(B.x), MAX(B.y) FROM Seats AS A, Seats AS B WHERE B.x < A.x AND B.y < A.y AND (B.y - A.y) = (B.x - A.x) GROUP BY A.x, A.y; /* Top left */
'''

print('''
INSERT INTO Neighbors (x1, y1, x2, y2) SELECT A.x AS x1, A.y AS y1, MIN(B.x) AS x2, MIN(B.y) AS y2 FROM Seats AS A, Seats AS B WHERE A.x = B.x AND A.y < B.y GROUP BY A.x, A.y;
INSERT INTO Neighbors (x1, y1, x2, y2) SELECT A.x, A.y, MAX(B.y), MAX(B.y) FROM Seats AS A, Seats AS B WHERE A.x = B.x AND B.y < A.y GROUP BY A.x, A.y;
INSERT INTO Neighbors (x1, y1, x2, y2) SELECT A.x, A.y, MIN(B.x), MIN(B.y) FROM Seats AS A, Seats AS B WHERE A.x < B.x AND A.y < B.y AND (B.y - A.y) = (B.x - A.x) GROUP BY A.x, A.y;
INSERT INTO Neighbors (x1, y1, x2, y2) SELECT A.x, A.y, MAX(B.x), MAX(B.y) FROM Seats AS A, Seats AS B WHERE B.x < A.x AND B.y < A.y AND (B.y - A.y) = (B.x - A.x) GROUP BY A.x, A.y;
''')