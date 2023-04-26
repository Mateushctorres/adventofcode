with open("./day9/input.txt") as file:
    lines = file.read().strip().split("\n")

headx, heady = 0, 0
tailx, taily = 0, 0

def touching(x1, y1, x2, y2):
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1 

def move(dx, dy):
    global headx, heady, tailx, taily

    headx += dx
    heady += dy

    if not touching(headx, heady, tailx, taily):
        sign_x = 0 if headx == tailx else (headx - tailx) / abs(headx - tailx)
        sign_y = 0 if heady == taily else (heady - taily) / abs(heady - taily)

        tailx += sign_x
        taily += sign_y


dd = {
    "R": [1, 0],
    "U": [0, 1],
    "L": [-1, 0],
    "D": [0, -1]
}

tail_visited = set()
tail_visited.add((tailx, taily))

for line in lines:
    op, amount = line.split(" ")
    amount = int(amount)
    dx, dy = dd[op]

    for _ in range(amount):
        move(dx, dy)
        tail_visited.add((tailx, taily))

print(len(tail_visited))