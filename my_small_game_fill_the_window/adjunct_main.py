class nevim_jak_to_nazvat:
    def nahoru(self):
        self.y -= self.rychlost
    def dolu(self):
        self.y += self.rychlost
    def vpravo(self):
        self.x += self.rychlost
    def vlevo(self):
        self.x -= self.rychlost
    def __init__(self,y,x,up,down,right,left):
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.x = x
        self.y = y
        self.rychlost = 7
        if sum ([self.up,self.down,self.right,self.left]) >= 3:
            pass
        elif sum ([self.up,self.down,self.right,self.left]) == 2:
            if self.left and self.up:
                self.nahoru()
                self.vlevo()
            if self.left and self.right:
                self.vlevo()
                self.vpravo()
            if self.left and self.down:
                self.dolu()
                self.vlevo()
            if self.down and self.up:
                pass
            if self.down and self.right:
                self.dolu()
                self.vpravo()
            if self.up and self.right:
                self.nahoru()
                self.vpravo()
        else:
            if self.up:
                self.nahoru()
            if self.left:
                self.vlevo()
            if self.right:
                self.vpravo()
            if self.down:
                self.dolu()
    def navrat(self):
        vsechno = [self.y, self.x, self.up, self.down, self.right, self.left]
        return vsechno
