import pybullet as p
import time
import math
import pybullet_data
from constants import *

useGui = True

if (useGui):

    p.connect(p.GUI)

else:

    p.connect(p.DIRECT)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)

p.setRealTimeSimulation(1)

obj1 = p.loadURDF(DRONE_URDF, [0, 0, 1], [0, 0, 0, 1])

obj2 = p.loadURDF(DRONE_URDF, [0,2, 1], [0, 0, 0, 1])

rayFrom = []
rayTo = []
rayIds = []

numRays = 15

rayLen = 2

rayHitColor = [1, 0, 0]
rayMissColor = [0, 1, 0]

replaceLines = True

for i in range(numRays):
    
    rayFrom.append([0, 0, 1])

    rayTo.append([math.sin(2. * math.pi * float(i) / numRays),
                  math.cos(2. * math.pi * float(i) / numRays), 1])

    if(replaceLines):

        rayIds.append(p.addUserDebugLine(rayFrom[i], rayTo[i], rayMissColor))

    else:

        rayIds.append(-1)

for j in range(numRays):
    
    results = p.rayTestBatch(rayFrom, rayTo, j + 1)

for i in range(numRays):
            
    hitObjectUid = results[i][0]

    if(hitObjectUid < 0):
        
        hitPosition = [0, 0, 0]
        p.addUserDebugLine(rayFrom[i], rayTo[i], rayMissColor, replaceItemUniqueId=rayIds[i])

    else:
        
        hitPosition = results[i][3]
        p.addUserDebugLine(rayFrom[i], hitPosition, rayHitColor, replaceItemUniqueId=rayIds[i])

for i in range(10000):
    
    time.sleep(0.01)

p.disconnect()






"""
numSteps = 10

if(useGui):

    numSteps = 327680

for i in range(numSteps):
    
    #p.stepSimulation()

    for j in range(numRays):

        results = p.rayTestBatch(rayFrom, rayTo, j + 1)

    #for i in range (10):
        #p.removeAllUserDebugItems()

    if (useGui):
      
        if(not replaceLines):
            
            p.removeAllUserDebugItems()

        for i in range(numRays):
            
            hitObjectUid = results[i][0]

            if(hitObjectUid < 0):
                
                hitPosition = [0, 0, 0]
                p.addUserDebugLine(rayFrom[i], rayTo[i], rayMissColor, replaceItemUniqueId=rayIds[i])

            else:
                
                hitPosition = results[i][3]
                p.addUserDebugLine(rayFrom[i], hitPosition, rayHitColor, replaceItemUniqueId=rayIds[i])
"""






