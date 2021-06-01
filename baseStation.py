import random
import neighbor as nb
import node as nd


class BaseStation:
    posX = 0
    posY = 0
    Nodes = []
    Range = 0
    nodeNum = 0
    nodeHeight = 0
    nodeCommRange = 0
    nodeIndicator = 0

    def __init__(self, posX, posY, Range, nodeNum, nodeHeight, nodeCommRange):
        self.posX = posX
        self.posY = posY
        self.Range = Range
        self.nodeNum = nodeNum
        self.nodeHeight = nodeHeight
        self.nodeCommRange = nodeCommRange

    def makeNodes(self):
        for i in range(self.nodeNum):
            randomPosX = random.randrange(self.posX - self.Range, self.posX + self.Range)
            randomPosY = random.randrange(self.posY - self.Range, self.posY + self.Range)
            node = nd.Node(self.nodeIndicator, randomPosX, randomPosY, self.nodeHeight)
            self.Nodes.append(node)
            self.nodeIndicator += 1

        assert (self.nodeNum == self.nodeIndicator)

    def calculateBetweenNodeRange(self, nodeIdA, nodeIdB):
        (x1, y1, _) = self.Nodes[nodeIdA].getNodePos()
        (x2, y2, _) = self.Nodes[nodeIdB].getNodePos()
        r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
        if r < self.nodeCommRange:
            return True
        return False

    def changeNodeToNeighbor(self, neighborID):
        (x, y, z) = self.Nodes[neighborID].getNodePos()
        neighbor = nb.Neighbor(neighborID, x, y, z)
        return neighbor

    def moveNodesInTime(self, time):
        for t in range(time):
            for i in range(self.nodeNum):
                self.Nodes[i].clearNeighbors()
                for j in range(self.nodeNum):
                    if i is j:
                        continue
                    if self.checkRange(i, j):
                        neighbor = self.changeNodeToNeighbor(j)
                        self.Nodes[i].updateNeighbor(neighbor)

            for i in range(self.nodeNum):
                self.Nodes[i].moveNode()

    def getNodesPos(self):
        xl = []
        yl = []
        for i in range(self.nodeNum):
            (x, y, _) = self.Nodes[i].getNodePos()
            xl.append(x)
            yl.append(y)

        return xl, yl
