import pybullet as p
import time
import math
import pybullet_data
from constants import *

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setRealTimeSimulation(1)

obj1 = p.loadURDF(DRONE_URDF, [0, 0, 1], [0, 0, 0, 1])
obj2 = p.loadURDF(DRONE_URDF, [0, 1, 1], [0, 0, 0, 1])

rayFrom = []
rayTo = []
rayIds = []

rayFrom2 = []
rayTo2 = []
rayIds2 = []

for i in range(10000):

    newPos, newOri = p.getBasePositionAndOrientation(obj1)

    posX = newPos[0]
    posY = newPos[1]

    for i in range(NUMBER_RAYS):
        
        rayFrom.append([posX, posY, 1])

        rayTo.append([(math.sin(2. * math.pi * float(i) / NUMBER_RAYS) + posX),
                      (math.cos(2. * math.pi * float(i) / NUMBER_RAYS) + posY), 1])
        
        rayIds.append(p.addUserDebugLine(rayFrom[i], rayTo[i], RAY_MISS_COLOR))

    for j in range(NUMBER_RAYS):
        
        results = p.rayTestBatch(rayFrom, rayTo, j + 1)

    hitFlag = False

    for k in range(NUMBER_RAYS):
        
        hitObject = results[k][0]

        if(hitObject < 0):
            
            hitPosition = [0, 0, 0]

            p.addUserDebugLine(rayFrom[k], rayTo[k], RAY_MISS_COLOR, replaceItemUniqueId = rayIds[k])

        else:
            
            hitPosition = results[k][3]

            print("HIT: ", hitPosition)

            p.addUserDebugLine(rayFrom[k], hitPosition, RAY_HIT_COLOR, replaceItemUniqueId = rayIds[k])

            hitFlag = True

            print("HIT OBJECT: ", hitObject)

    #if(hitFlag == False):

    posX = newPos[0] + 0.1
    posY = newPos[1] + 0.1

    newPos = [posX, posY, 1]

    for i in range (NUMBER_RAYS):

        p.removeAllUserDebugItems()

    rayFrom = []
    rayTo = []
    rayIds = []

    p.resetBasePositionAndOrientation(obj1, newPos, newOri)
















    newPos, newOri = p.getBasePositionAndOrientation(obj2)

    posX = newPos[0]
    posY = newPos[1]

    for i in range(NUMBER_RAYS):
        
        rayFrom2.append([posX, posY, 1])

        rayTo2.append([math.sin(2. * math.pi * float(i) / NUMBER_RAYS) + posX,
                       math.cos(2. * math.pi * float(i) / NUMBER_RAYS) + posY, 1])
        
        rayIds2.append(p.addUserDebugLine(rayFrom2[i], rayTo2[i], RAY_MISS_COLOR))

    for j in range(NUMBER_RAYS):
        
        results = p.rayTestBatch(rayFrom2, rayTo2, j + 1)

    hitFlag = False

    for k in range(NUMBER_RAYS):
        
        hitObject = results[k][0]

        if(hitObject < 0):
            
            hitPosition = [0, 0, 0]

            p.addUserDebugLine(rayFrom2[k], rayTo2[k], RAY_MISS_COLOR, replaceItemUniqueId = rayIds2[k])

        else:
            
            hitPosition = results[k][3]

            p.addUserDebugLine(rayFrom2[k], hitPosition, RAY_HIT_COLOR, replaceItemUniqueId = rayIds2[k])

            hitFlag = True

            print("HIT OBJECT: ", hitObject)

    


    if(hitFlag == False):

        posX = newPos[0] - 0.1
        posY = newPos[1] - 0.1

    newPos = [posX, posY, 1]

    for i in range (NUMBER_RAYS):
    
        p.removeAllUserDebugItems()

    rayFrom2 = []
    rayTo2 = []
    rayIds2 = []

    p.resetBasePositionAndOrientation(obj2, newPos, newOri)
    
    time.sleep(0.1)

p.disconnect()
