import baseStation as bs
import matplotlib.pyplot as plt

basePosX = 0
basePosY = 0
mapRange = 0
nodeNumber = 0
nodeHeight = 0
nodeCommRange = 0


baseStation = bs.BaseStation(basePosX, basePosY, mapRange, nodeNumber, nodeHeight, nodeCommRange)

baseStation.makeNodes()

(nodePosXList, nodePosYList) = baseStation.getNodesPos()

plt.scatter(nodePosXList, nodePosYList)







