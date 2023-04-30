
class Ship(object):
    alive = True

    def __init__(self, idx, x, y, direction, length):
        self.idx = idx
        self.x = x
        self.y = y
        self.direction = direction
        self.length = length
        # self.alive = True
        self.hp = length

    def reroll(self, t):
        rein_y = int(input("Again! input your Y (column) for ship%d :" % t))
        rein_x = int(input("Again! input your X (row) for ship%d :" % t))
        if self.direction is True:
            if (rein_x < (5-self.length)) and (rein_y < 5):
                self.y = rein_y
                self.x = rein_x
        else:
            if (rein_y < (5-self.length)) and (rein_x < 5):
                self.y = rein_y
                self.x = rein_x

    def hit(self):
        self.hp -= 1
        if self.hp == 0:
            self.alive = False


class EnemySea(object):

    def __init__(self):
        self.grid_en = [["."] * 5 for _ in range(5)]
        # self.ships = []
        self.totalHp = 2 + 2 + 2
        self.lenghts = [2, 2, 2]
        self.flag = None

    def print_board(self, board):
        for row in board:
            print(" ".join(row))

    def target(self):
        tagY = int(input("Please input your target Y [column]:"))
        tagX = int(input("Please input your target X [row]:"))
        if (tagX < (len(self.grid_en[0]))) and (tagY < (len(self.grid_en))) and self.grid_en[tagX][tagY] == ".":
            # self.change_cell(tagX, tagY, self.flag)
            return tagY, tagX
        else:
            print("!!!Enter Again!!!")
            return self.target()

    def change_cell(self, tgY, tgX, state):
        if state == 0:
            print("Message: MISS")
            self.grid_en[tgY][tgX] = "#"
        if state == 1:
            print("Message: HIT")
            self.grid_en[tgY][tgX] = "X"
        if state == 2:
            print("Message: VICTORY")
            self.grid_en[tgY][tgX] = "X"


class YourSea(object):

    def __init__(self):
        self.grid_yo = [["."] * 5 for _ in range(5)]
        self.ships = []
        self.totalHp = 2 + 2 + 2
        self.lengths = [2, 2, 2]
        self.create_ship()
        self.set_ships()

    def print_board(self, board):
        for row in board:
            # print(row)
            print(" ".join(row))

    def set_dir(self, j):
        # true - horizontal      false - vertical
        dirIn = input("input your direction for ship%d \n 'True'-horizontal, 'False'-vertical:" % j)
        if dirIn == "T":
            return True
        elif dirIn == "F":
            return False
        else:
            return self.set_dir(j)

    def set_x(self, k):
        in_x = int(input("input your X (column) for ship%d :" % k))
        if in_x < 5:
            return in_x
        else:
            return self.set_x(k)

    def set_y(self, b):
        in_y = int(input("input your Y (row) for ship%d :" % b))
        if in_y < 5:
            return in_y
        else:
            return self.set_y(b)

    def create_ship(self):
        pts_x = []
        pts_y = []
        ships_dir = []

        for i in range(3):
            input_y = self.set_y(i)
            pts_y.append(input_y)
            input_x = self.set_x(i)
            pts_x.append(input_x)
            input_dir = self.set_dir(i)
            ships_dir.append(input_dir)

            self.ships.append(Ship(i, pts_x[i], pts_y[i], ships_dir[i], self.lengths[i]))

    # add checking collisions
    def set_ships(self):
        ok = False
        for i in range(3):
            tempShipX = [None] * self.ships[i].length
            tempShipY = [None] * self.ships[i].length

            if self.ships[i].direction is True:
                while ok is False:
                    for j in range(self.ships[i].length):
                        tempShipX[j] = self.ships[i].x + j
                        tempShipY[j] = self.ships[i].y

                    for j in range(self.ships[i].length):
                        if self.grid_yo[tempShipY[j]][tempShipX[j]] != ".":
                            self.ships[i].reroll(i)
                            break
                        if j == (self.ships[i].length-1):
                            ok = True
                for j in range(self.ships[i].length):
                    self.grid_yo[self.ships[i].y][self.ships[i].x + j] = str(self.ships[i].idx)
            else:
                while ok is False:
                    for j in range(self.ships[i].length):
                        tempShipX[j] = self.ships[i].x
                        tempShipY[j] = self.ships[i].y + j

                    for j in range(self.ships[i].length):
                        if self.grid_yo[tempShipY[j]][tempShipX[j]] != ".":
                            self.ships[i].reroll(i)
                            break
                        if j == (self.ships[i].length-1):
                            ok = True
                for j in range(self.ships[i].length):
                    self.grid_yo[self.ships[i].y + j][self.ships[i].x] = str(self.ships[i].idx)
            ok = False

    # 0 - miss, 1 - hit, 2 - defeat
    # 3 - sink < can be added later >
    def check_shoot(self, y, x):
        if self.grid_yo[y][x] == ".":
            return 0
        else:
            self.ships[int(self.grid_yo[y][x])].hit()
            self.totalHp -= 1
            # if self.ships[int(self.grid_yo[y][x])].alive is False:
            #     return 3
            if self.totalHp == 0:
                return 2
            return 1

    def ships_info(self):
        for i in range(len(self.ships)):
            print(self.ships[i].__dict__)

    def draw_cell(self, tgY, tgX, state):
        if state == "0":
            print("Message: Enemy MISS")
            self.grid_yo[tgY][tgX] = "#"
        if state == "1":
            print("Message: Enemy HIT")
            self.grid_yo[tgY][tgX] = "X"
        if state == "2":
            print("Message: Enemy VICTORY")
            self.grid_yo[tgY][tgX] = "X"
