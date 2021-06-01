class Neighbor:
    idNum = -1
    posX = 0
    posY = 0
    posZ = 0

    def __init__(self, idNum, posX, posY, posZ):
        self.idNum = idNum
        self.posX = posX
        self.posY = posY
        self.posZ = posZ

    def getNeighborID(self):
        return self.idNum

    def getNeighborPos(self):
        return self.posX, self.posY, self.posX