import neighbor as nb
import nodeFunction as nF


class Node:
    idNum = -1
    posX = 0
    posY = 0
    posZ = 0
    nbs = {}

    def setNode(self, idNum, posX, posY, posZ):
        self.idNum = idNum
        self.posX = posX
        self.posY = posY
        self.posZ = posZ

    def findNeighbor(self, neighborID):
        result = self.nbs.get(neighborID)
        if result is None:
            return False
        return True

    def calculatePos(self):
        totalMomentum = [0, 0]
        for nb in self.nbs:
            (nx, ny, _) = self.nbs[nb].getNeighborPos()
            (mx, my) = nF.calculateMomentum(self.posX, self.posY, nx, ny)
            totalMomentum[0] += mx
            totalMomentum[1] += my
        newPosX = self.posX + totalMomentum[0]
        newPosY = self.posY + totalMomentum[1]

        return newPosX, newPosY

    def moveNode(self):
        (newPosX, newPosY) = self.calculatePos()
        self.posX = newPosX
        self.posY = newPosY

    def updateNeighbor(self, neighbor):
        neighborID = neighbor.getNeighborID()
        (neighborPosX, neighborPosY, neighborPosZ) = neighbor.getNeighborPos()
        self.nbs[neighborID] = nb.Neighbor(neighborID, neighborPosX, neighborPosY, neighborPosZ)

    def getNodePos(self):
        return self.posX, self.posY, self.posZ

    def getNodeID(self):
        return self.idNum

    def clearNeighbors(self):
        self.nbs.clear()
