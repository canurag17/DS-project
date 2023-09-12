
class Tank(object):
    alive = True

    def __init__(self, idx, x, y, direction, length):
        self.idx = idx
        self.x = x
        self.y = y
        self.direction = direction
        self.length = length
        self.hp = length

    def reroll(self, t):
        rein_y = int(input("Again! input your Y (column) for Tank%d :" % t))
        rein_x = int(input("Again! input your X (row) for Tank%d :" % t))
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


class EnemyGround(object):

    def __init__(self):
        self.grid_en = [["."] * 5 for _ in range(5)]
        # self.Tanks = []
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


class YourGround(object):

    def __init__(self):
        self.grid_yo = [["."] * 5 for _ in range(5)]
        self.Tanks = []
        self.totalHp = 2 + 2 + 2
        self.lengths = [2, 2, 2]
        self.create_Tank()
        self.set_Tanks()

    def print_board(self, board):
        for row in board:
            # print(row)
            print(" ".join(row))

    def set_dir(self, j):
        # true - horizontal      false - vertical
        dirIn = input("input your direction for Tank%d \n 'True'-horizontal, 'False'-vertical:" % j)
        if dirIn == "T":
            return True
        elif dirIn == "F":
            return False
        else:
            return self.set_dir(j)

    def set_x(self, k):
        in_x = int(input("input your X (column) for Tank%d :" % k))
        if in_x < 5:
            return in_x
        else:
            return self.set_x(k)

    def set_y(self, b):
        in_y = int(input("input your Y (row) for Tank%d :" % b))
        if in_y < 5:
            return in_y
        else:
            return self.set_y(b)

    def create_Tank(self):
        pts_x = []
        pts_y = []
        Tanks_dir = []

        for i in range(3):
            input_y = self.set_y(i)
            pts_y.append(input_y)
            input_x = self.set_x(i)
            pts_x.append(input_x)
            input_dir = self.set_dir(i)
            Tanks_dir.append(input_dir)

            self.Tanks.append(Tank(i, pts_x[i], pts_y[i], Tanks_dir[i], self.lengths[i]))

 
    def set_Tanks(self):
        ok = False
        for i in range(3):
            tempTankX = [None] * self.Tanks[i].length
            tempTankY = [None] * self.Tanks[i].length

            if self.Tanks[i].direction is True:
                while ok is False:
                    for j in range(self.Tanks[i].length):
                        tempTankX[j] = self.Tanks[i].x + j
                        tempTankY[j] = self.Tanks[i].y

                    for j in range(self.Tanks[i].length):
                        if self.grid_yo[tempTankY[j]][tempTankX[j]] != ".":
                            self.Tanks[i].reroll(i)
                            break
                        if j == (self.Tanks[i].length-1):
                            ok = True
                for j in range(self.Tanks[i].length):
                    self.grid_yo[self.Tanks[i].y][self.Tanks[i].x + j] = str(self.Tanks[i].idx)
            else:
                while ok is False:
                    for j in range(self.Tanks[i].length):
                        tempTankX[j] = self.Tanks[i].x
                        tempTankY[j] = self.Tanks[i].y + j

                    for j in range(self.Tanks[i].length):
                        if self.grid_yo[tempTankY[j]][tempTankX[j]] != ".":
                            self.Tanks[i].reroll(i)
                            break
                        if j == (self.Tanks[i].length-1):
                            ok = True
                for j in range(self.Tanks[i].length):
                    self.grid_yo[self.Tanks[i].y + j][self.Tanks[i].x] = str(self.Tanks[i].idx)
            ok = False

    
   
    def check_shoot(self, y, x):
        if self.grid_yo[y][x] == ".":
            return 0
        else:
            self.Tanks[int(self.grid_yo[y][x])].hit()
            self.totalHp -= 1
            
            if self.totalHp == 0:
                return 2
            return 1

    def Tanks_info(self):
        for i in range(len(self.Tanks)):
            print(self.Tanks[i].__dict__)

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
