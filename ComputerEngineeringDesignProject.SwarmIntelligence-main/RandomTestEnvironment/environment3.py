import pybullet as p
import time
import pybullet_data
from constants import *

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setRealTimeSimulation(1)
p.setGravity(0, 0, GRAVITY)

def createWall(dimensions, color, basePosition, baseOrientation):
      
      boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX, halfExtents = dimensions)

      boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX, halfExtents = dimensions, rgbaColor = color)

      p.createMultiBody(MASS, boxCollisionId, boxVisualId, basePosition, baseOrientation)

# Plane ----------------------------------------------------------------------------------------------------

createWall(PLANE_DIMENSIONS, PLANE_COLOR, PLANE_POSITION, PLANE_ORIENTATION)

"""
# Reference ----------------------------------------------------------------------------------------------------

# Origin --------------------------------------------------

dimensions = [0.2, 0.2, 3]

basePosition = [0, 0, 3]

createWall(dimensions, REFERENCE_COLOR, basePosition, ORIGIN_ORIENTATION)

# Vertical --------------------------------------------------

dimensions = [0.2, 22.2, 0.2]

basePosition = [22, 0, 2]

createWall(dimensions, REFERENCE_COLOR, basePosition, VERTICAL_ORIENTATION)

basePosition = [-22, 0, 2]

createWall(dimensions, REFERENCE_COLOR, basePosition, VERTICAL_ORIENTATION)

# Horizontal --------------------------------------------------

dimensions = [0.2, 22.2, 0.2]

basePosition = [0, 22, 2]

createWall(dimensions, REFERENCE_COLOR, basePosition, HORIZONTAL_ORIENTATION)

basePosition = [0, -22, 2]

createWall(dimensions, REFERENCE_COLOR, basePosition, HORIZONTAL_ORIENTATION)
"""

# Vertical ----------------------------------------------------------------------------------------------------

# Length 1 --------------------------------------------------

dimensions = [2, 1.25, 0.25]

basePosition = [-9.75, 7, 2]

createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

basePosition = [0, -1, 2]

createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

# Length 4.25 --------------------------------------------------

dimensions = [2, 4.25, 0.25]

basePosition = [-11.75, 18, 2]

createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

basePosition = [0.25, 18, 2]

createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

# Length 5 --------------------------------------------------

dimensions = [2, 5.25, 0.25]

basePosition = [22, 9, 2]

createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

# Length 6 --------------------------------------------------

dimensions = [2, 6.25, 0.25]

basePosition = [4, -16, 2]

createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

# Length 9 --------------------------------------------------

dimensions = [2, 9.25, 0.25]

basePosition = [16, -1, 2]

createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

# Length 10 --------------------------------------------------

dimensions = [2, 10.25, 0.25]

basePosition = [-18, -12, 2]

createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

basePosition = [-22, 8, 2]

createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

basePosition = [-6, -12, 2]

createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

# Horizontal ----------------------------------------------------------------------------------------------------

# Length 2 --------------------------------------------------

dimensions = [0.25, 2.25, 2]

basePosition = [-9.75, 14, 2]

createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

# Length 3 --------------------------------------------------

dimensions = [0.25, 3.25, 2]

basePosition = [-3, -2, 2]

createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

basePosition = [19, 4, 2]

createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

# Length 4 --------------------------------------------------

dimensions = [0.25, 4.25, 2]

basePosition = [-5.75, 6, 2]

createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

basePosition = [-18, -2, 2]

createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

basePosition = [-18, 3, 2]

createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

# Length 5 --------------------------------------------------

dimensions = [0.25, 5.25, 2]

basePosition = [-17, 18, 2]

createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

# Length 6 --------------------------------------------------

dimensions = [0.25, 6.25, 2]

basePosition = [10, -10, 2]

createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

basePosition = [-5.75, 22, 2]

createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

basePosition = [-15.75, 8, 2]

createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

# Length 11 --------------------------------------------------

dimensions = [0.25, 11, 2]

basePosition = [11, 14, 2]

createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

# Length 11.25 --------------------------------------------------

dimensions = [0.25, 11.25, 2]

basePosition = [-7, -22, 2]

createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

#while(1000):
for i in range(10000):
      
  #keys = p.getKeyboardEvents()
  #print(keys)

  time.sleep(0.01)

p.disconnect()
