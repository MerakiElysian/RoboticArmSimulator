import math
import numpy as np
class Move_arm():
    '''
        This Class is for move arm to new point with the help of the set of new points.
    '''
    def __init__(self,roboticArmName:object = None, newPoints:list=[[600,480]]) -> None:   
        '''
        This Class is for move arm to new point with the help of the set of new points.
        Args:
            newPoints (list, optional): It contains the list of all the new points
        '''
        self._new_points = newPoints # sample list for the 
        self._new_angles = []
        self._roboticArmName = roboticArmName
        # tryPoint = 
        # self._new_points(tryPoint)

    @property
    def new_points(self)->list:
        return self._new_points
    @new_points.setter
    def new_points(self,val:list)->None:
        self._new_points = val
    @property
    def robotic_arm_name(self)->object:
        return self._roboticArmName
    @robotic_arm_name.setter
    def robotic_arm_name(self,val:object)->None:
        self._roboticArmName = val

    def add_newAngle(self, val:list):
        '''
        function to add the new angles of arm in the _new_angles list
        '''
        self._new_angles.append(val)
    
    #Creating function of single point and will iterate it with the help of loop.
    def findNewAngles(self):
        pointListSize = len(self.new_points)
        self._new_angles.clear()
        for n in range(pointListSize):
            x1, y1 = self.robotic_arm_name.att_joints[0].anchor_point #Base Coords
            x2, y2 = self.new_points[n] #New Coords
            print(x2,y2)
            y1 = -y1
            y2 = -y2
            a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            b = self.robotic_arm_name.att_arms[0].arm_dim[2]
            c = self.robotic_arm_name.att_arms[1].arm_dim[2]
            x = (x2 - x1)
            y = (y2 - y1)

            # finding C angle
            cosC= (a**2 + b**2 - c**2) / (2 * a * b)
            C = math.degrees(np.arccos(cosC))
            print('C = ',C)
            # finding D1 angle
            D = math.degrees(math.atan2(y,x))
            print('D = ',D)

            # Finding New coordinate
            angle_rad = math.radians(C+D)
            print("hehe Degree",(C+D))
            x3 = x1 + b * math.cos(angle_rad)
            y3 = y1 + b * math.sin(angle_rad)
            print("mid coord",x3,y3)
            # finding angle of new coordinate from tan formula
            _x = (x3 - x1)
            _y = (y3 - y1)
            print(_x,_y)
            G = math.degrees(math.atan2(_y,_x))
            print('G = ',G) 
            _x2 = (x2 - x3)
            _y2 = (y2 - y3)
            print(_x2,_y2)
            G2 = math.degrees(math.atan2(_y2,_x2))
            print("G2 = ",G2)
            g2_rad = math.radians(G2)
            new_x2 = x3 +  c * math.cos(g2_rad)
            new_y2 = y3 + c * math.sin(g2_rad)
            print("HFIHEDIFIE last cord", new_x2,new_y2)
            newangle = [G,G2]
            self.add_newAngle(newangle)
            # self.robotic_arm_name.updateAngle(1,G)
            # self.robotic_arm_name.updateAngle(2,G2)
            print("this is list of new angles",self._new_angles)
        return self._new_angles
        # return G,G2
    