import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI) # or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) # optionally
p.setGravity(0,0,-9.8)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.createCollisionShape(p.GEOM_PLANE)
p.createMultiBody(0, 0)

robot1StartPos = [0, 0, 1]
robot1StartOrientation = p.getQuaternionFromEuler([0, 0, 0])
robot1Id = p.loadURDF("husky/husky.urdf", robot1StartPos, robot1StartOrientation)

robot2StartPos = [0, 2, 0]
robot2StartOrientation = p.getQuaternionFromEuler([0, 0, -1])
robot2Id = p.loadURDF("husky/husky.urdf", robot2StartPos, robot2StartOrientation)

robot3StartPos = [2, 0, 0]
robot3StartOrientation = p.getQuaternionFromEuler([0, 0, 1])
robot3Id = p.loadURDF("husky/husky.urdf", robot3StartPos, robot3StartOrientation)

robot4StartPos = [0, -2, 0]
robot4StartOrientation = p.getQuaternionFromEuler([0, 0, -1])
robot4Id = p.loadURDF("husky/husky.urdf", robot4StartPos, robot4StartOrientation)

robot5StartPos = [-2, 0, 0]
robot5StartOrientation = p.getQuaternionFromEuler([0, 0, 1])
robot5Id = p.loadURDF("husky/husky.urdf", robot5StartPos, robot5StartOrientation)


robotsIdList = [robot1Id, robot2Id, robot4Id, robot4Id]

#x = 0.0
#y = 0.0

for i in range(10000):

    if i <= 300:

        pass

    else:

        
        newPos, newOri = p.getBasePositionAndOrientation(robot1Id)
        #newOri = list(p.getBasePositionAndOrientation(robot1Id)[1])

        newPos = list(newPos)
        newOri = list(newOri)

        
        if(i <= 1000):    
        
            newPos[0] += 0.001
            newOri[2] += 0.001

        else:

            newPos[0] -= 0.001
            newOri[2] -= 0.001

        p.resetBasePositionAndOrientation(robot1Id, newPos, newOri)
        

        """
        if i == 1000:

            p.resetBasePositionAndOrientation(robot1Id, newPos, newOri)
        """

        """
        if x < 10.0:

            x = x + 0.01
            y = y + 0.01        

        else:

            x = 0        
            #p.removeBody(robot1Id)
            #p.removeBody(robot2Id)
            #robot1Id = p.loadURDF("husky/husky.urdf", robot1StartPos, robot1StartOrientation)
            #robot2Id = p.loadURDF("husky/husky.urdf", robot2StartPos, robot2StartOrientation)
        """

        #p.setGravity(-x, -x, 0, robot1Id)
        #p.setGravity(-x, -y, 0)

        p.stepSimulation()
        time.sleep(1./240.)

        """
        for robot in robotsIdList:   
            p.setJointMotorControlArray(bodyUniqueId = robot, jointIndices = [2, 3, 4, 5], controlMode = p.VELOCITY_CONTROL,
                                        targetVelocities = [5.0, 5.0, 5.0, 5.0], forces = [500.0, 500.0, 500.0, 500.0])
        """

        if i <= 1000:
            
            p.setJointMotorControlArray(bodyUniqueId = robot1Id, jointIndices = [2, 3, 4, 5], controlMode = p.VELOCITY_CONTROL,
                                        targetVelocities = [-10.0, -10.0, -10.0, -10.0], forces = [500.0, 500.0, 500.0, 500.0])
            
            p.setJointMotorControlArray(bodyUniqueId = robot2Id, jointIndices = [2, 3, 4, 5], controlMode = p.VELOCITY_CONTROL,
                                        targetVelocities = [10.0, 10.0, 10.0, 10.0], forces = [500.0, 500.0, 500.0, 500.0])
            
            p.setJointMotorControlArray(bodyUniqueId = robot3Id, jointIndices = [2, 3, 4, 5], controlMode = p.VELOCITY_CONTROL,
                                        targetVelocities = [-10.0, -10.0, -10.0, -10.0], forces = [500.0, 500.0, 500.0, 500.0])

            p.setJointMotorControlArray(bodyUniqueId = robot4Id, jointIndices = [2, 3, 4, 5], controlMode = p.VELOCITY_CONTROL,
                                        targetVelocities = [-10.0, -10.0, -10.0, -10.0], forces = [500.0, 500.0, 500.0, 500.0])
            
            p.setJointMotorControlArray(bodyUniqueId = robot5Id, jointIndices = [2, 3, 4, 5], controlMode = p.VELOCITY_CONTROL,
                                        targetVelocities = [10.0, 10.0, 10.0, 10.0], forces = [500.0, 500.0, 500.0, 500.0])
        
        else:

            p.setJointMotorControlArray(bodyUniqueId = robot1Id, jointIndices = [2, 3, 4, 5], controlMode = p.VELOCITY_CONTROL,
                                    targetVelocities = [-10.0, -10.0, -10.0, -10.0], forces = [500.0, 500.0, 500.0, 500.0])
        
            p.setJointMotorControlArray(bodyUniqueId = robot2Id, jointIndices = [2, 3, 4, 5], controlMode = p.VELOCITY_CONTROL,
                                        targetVelocities = [-10.0, -10.0, -10.0, -10.0], forces = [500.0, 500.0, 500.0, 500.0])
            
            p.setJointMotorControlArray(bodyUniqueId = robot3Id, jointIndices = [2, 3, 4, 5], controlMode = p.VELOCITY_CONTROL,
                                        targetVelocities = [10.0, 10.0, 10.0, 10.0], forces = [500.0, 500.0, 500.0, 500.0])

            p.setJointMotorControlArray(bodyUniqueId = robot4Id, jointIndices = [2, 3, 4, 5], controlMode = p.VELOCITY_CONTROL,
                                        targetVelocities = [10.0, 10.0, 10.0, 10.0], forces = [500.0, 500.0, 500.0, 500.0])
            
            p.setJointMotorControlArray(bodyUniqueId = robot5Id, jointIndices = [2, 3, 4, 5], controlMode = p.VELOCITY_CONTROL,
                                        targetVelocities = [-10.0, -10.0, -10.0, -10.0], forces = [500.0, 500.0, 500.0, 500.0])
    
p.disconnect()
