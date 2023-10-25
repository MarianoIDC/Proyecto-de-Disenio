import pybullet as p
import time
import pybullet_data

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
#p.setRealTimeSimulation(1)
#p.createCollisionShape(p.GEOM_PLANE)
planeId = p.loadURDF("plane.urdf")
p.setGravity(0, 0, -9.8)
#p.createMultiBody(0, 0)

mass = 1
color = [0, 1, 1, 1]

# Reference ----------------------------------------------------------------------------------------------------

# Origin --------------------------------------------------

dimensions = [0.2, 0.2, 3]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = [4, 1, 1, 1])

basePosition = [0, 0, 3]

baseOrientation = [0, 0, 0, 1]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

# Vertical --------------------------------------------------

baseOrientation = [0, 1, 0, 1]

dimensions = [0.2, 22, 0.2]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = [4, 1, 1, 1])

basePosition = [22, 0, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

basePosition = [-22, 0, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

# Horizontal --------------------------------------------------

baseOrientation = [0, 0, 1, 1]

dimensions = [0.2, 22, 0.2]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = [4, 1, 1, 1])

basePosition = [0, 22, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

basePosition = [0, -22, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

# Vertical ----------------------------------------------------------------------------------------------------

baseOrientation = [0, 1, 0, 1]

# Length 1 --------------------------------------------------

dimensions = [2, 1.25, 0.25]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = color)

basePosition = [-9.75, 7, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

basePosition = [0, -1, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

# Length 4.25 --------------------------------------------------

dimensions = [2, 4.25, 0.25]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = color)

basePosition = [-11.75, 18, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

basePosition = [0.25, 18, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

# Length 5 --------------------------------------------------

dimensions = [2, 5.25, 0.25]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = color)

basePosition = [22, 9, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

# Length 6 --------------------------------------------------

dimensions = [2, 6.25, 0.25]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = color)

basePosition = [4, -16, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

# Length 9 --------------------------------------------------

dimensions = [2, 9.25, 0.25]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = color)

basePosition = [16, -1, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

# Length 10 --------------------------------------------------

dimensions = [2, 10.25, 0.25]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = color)

basePosition = [-18, -12, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

basePosition = [-22, 8, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

basePosition = [-6, -12, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

# Horizontal ----------------------------------------------------------------------------------------------------

baseOrientation = [0, 0, 1, 1]

# Length 2 --------------------------------------------------

dimensions = [0.25, 2.25, 2]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = color)

basePosition = [-9.75, 14, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

# Length 3 --------------------------------------------------

dimensions = [0.25, 3.25, 2]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = color)

basePosition = [-3, -2, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

basePosition = [19, 4, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

# Length 4 --------------------------------------------------

dimensions = [0.25, 4.25, 2]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = color)

basePosition = [-5.75, 6, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

basePosition = [-18, -2, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

basePosition = [-18, 3, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

# Length 5 --------------------------------------------------

dimensions = [0.25, 5.25, 2]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = color)

basePosition = [-17, 18, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

# Length 6 --------------------------------------------------

dimensions = [0.25, 6.25, 2]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = color)

basePosition = [10, -10, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

basePosition = [-5.75, 22, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

basePosition = [-15.75, 8, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

# Length 11 --------------------------------------------------

dimensions = [0.25, 11, 2]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = color)

basePosition = [11, 14, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

# Length 11.25 --------------------------------------------------

dimensions = [0.25, 11.25, 2]

boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX,
                                        halfExtents = dimensions)

boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX,
                                  halfExtents = dimensions,
                                  rgbaColor = color)

basePosition = [-7, -22, 2]

boxId = p.createMultiBody(mass,
                          boxCollisionId,
                          boxVisualId,
                          basePosition,
                          baseOrientation)

#while(1000):
for i in range(10000):
      
  #keys = p.getKeyboardEvents()
  #print(keys)

  time.sleep(0.01)

p.disconnect()
