class Robot:
    #Aryan
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 0  # 0 = East, 1 = North, 2 = West, 3 = South
        self.perimeter = 2 * (self.w + self.h - 2)
        
        self.directions = [
            (1, 0),   # East
            (0, 1),   # North
            (-1, 0),  # West
            (0, -1)   # South
        ]
        
        self.dirNames = ["East", "North", "West", "South"]

    def step(self, num):
        if self.perimeter == 0:
            return

        num %= self.perimeter
        if num == 0:
            num = self.perimeter

        while num > 0:
            nx = self.x + self.directions[self.dir][0]
            ny = self.y + self.directions[self.dir][1]

            # check boundary
            if nx < 0 or nx >= self.w or ny < 0 or ny >= self.h:
                self.dir = (self.dir + 1) % 4  # turn CCW
                nx = self.x + self.directions[self.dir][0]
                ny = self.y + self.directions[self.dir][1]

            self.x = nx
            self.y = ny
            num -= 1

    def getPos(self):
        return [self.x, self.y]

    def getDir(self):
        return self.dirNames[self.dir]