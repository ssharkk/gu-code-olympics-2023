from collections import deque

# constants
walls = ['+', '-', '|']
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
names = {(1, 0): 'down', (0, 1): 'right', (-1, 0): 'up', (0, -1): 'left'}

# input here
grid = [['+', '-', '+', '-', '+', '-', '+'],
        ['|', ' ', ' ', ' ', ' ', ' ', '|'],
        ['+', ' ', '+', '-', '+', ' ', '+'],
        ['|', '  ', ' ', 'F', '|', ' ', '|'],
        ['+', '-', '+', '-', '+', ' ', '+'],
        ['|', '$', ' ', ' ', ' ', ' ', '|'],
        ['+', '-', '+', '-', '+', '-', '+']]

rows = range(len(grid))
cols = range(len(grid[0]))

# locate start and finish
s, f = (), ()
for i, row in enumerate(grid):
    for j, ch in enumerate(row):
        if ch == '$':
            s = (i, j)
        elif ch == 'F':
            f = (i, j)

# bfs
prev = [[None for _ in cols] for _ in rows]
queue = deque()

prev[s[0]][s[1]] = s
queue.append(s)
while len(queue) > 0:
    pt = queue.popleft()
    for dir in dirs:
        new_pt = (pt[0] + dir[0], pt[1] + dir[1])
        if new_pt[0] not in rows or new_pt[1] not in cols:
            continue
        if grid[new_pt[0]][new_pt[1]] in walls:
            continue

        if prev[new_pt[0]][new_pt[1]] is None:
            prev[new_pt[0]][new_pt[1]] = dir
            queue.append(new_pt)

# deduce and print path
path = []
pt = f
while pt != s:
    dir = prev[pt[0]][pt[1]]
    path.append(names[dir])
    pt = (pt[0] - dir[0], pt[1] - dir[1])
path.reverse()
print(', '.join(path))
