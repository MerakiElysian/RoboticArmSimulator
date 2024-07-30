from Arm import Arm
from Joint import Joint
import math
import numpy as np

class Robotic_arm():
    """
        Class for creating and editing robotic arm.
        
        base_dim = dimensions of base platform for anchor and graphical representation
        total_arms = total number of starting arms
        arms_dim = dimensions for starting arms if applicable
    """
    def __init__(self, base_anchor: list = [int(1200/3), 600, 100, 20], total_arms: int = 0, arms_dim: list = None) -> None:
        self.att_arms = []      #list of objects of all arms attached from bottom to top
        self.att_joints = []    #list of objects of all joints attached from bottom to top
        self.__base_joint = None    #base joint object
        self.__base_dim = base_anchor   #base anchor points set (x,y,w,h)
        
        #create base joint
        self.base_joint = self.create_base_joint()
        self.att_joint(self.base_joint)
        
        #create starting arms if applicable
        if total_arms != 0: 
            self.arm_gen(total_arms, arms_dim)
        
        print("Wilson_generated")
        
    def att_arm(self, val: object, func: bool = False) -> None:
        """function to add or remove arms objects

        Args:
            val (object): object to be added
            func (bool, optional): False to add and True to remove. Defaults to False.
        """
        if not func:
            self.att_arms.append(val)
        else:
            self.att_arms.pop()
    
    def att_joint(self, val: object, func: bool = False) -> None:
        """function to add or remove joints objects

        Args:
            val (object): object to be added
            func (bool, optional): False to add and True to remove. Defaults to False.
        """
        if not func:
            self.att_joints.append(val)
        else:
            self.att_joints.pop()
    
    @property
    def base_dim(self) -> list:
        return self.__base_dim
    
    @base_dim.setter
    def base_dim(self, new_dim: list) -> None:
        self.__base_dim = new_dim
    
    @property
    def arm_anchor(self) -> int:
        return self.__arm_anchor
    
    @arm_anchor.setter
    def arm_anchor(self, val: int) -> None:
        self.__arm_anchor = val
    
    @property
    def base_joint(self) -> object:
        return self.__base_joint
    
    @base_joint.setter
    def base_joint(self, val: object) -> None:
        self.__base_joint = val
    
    def create_base_joint(self):    
        """
            Creates base joint for connecting arms to base
        """
        return Joint(anchor_point = list((int(self.base_dim[0] + self.base_dim[2]/2), int(self.base_dim[1] + self.base_dim[3]/2))), att_base = True)
    
    def arm_gen(self, total_arm: int, arms_dim: list) -> list:
        """_summary_
            Generates arms and attaches them one by one to form an arm
            
        Args:
            total_arm (int): total number of arms needed in Robotic arm
            arms_dim (list): dimensions of each arm in sequential order (bottom up) (x,y,w,h)

        Returns:
            list: list of objects of constructed arm
        """
        if len(arms_dim) != total_arm:
            Warning("number of dim values provided are more than number of arms. excess dim values will not be used.")
        t_arms = []
        for arm in range(total_arm):
            #create new arm and give p1 as its lower joint anchor
            self.att_arm(Arm(arm_dim = arms_dim[arm], l_anchor = self.att_joints[-1]))
            
            # print(self.att_arms[arm].arm_dim)#####


            #connect lower joint to current arm
            self.att_joints[-1].upper_arm = self.att_arms[-1]
            #calculate coords for p2 joint from p1 joint and current arm's dim
            l_anchor_coord = self.att_arms[-1].lower_anchor.anchor_point
            #create p2 joint
            upper_anchor = Joint(anchor_point = list((int(l_anchor_coord[0] ), int(l_anchor_coord[1] + arms_dim[arm][3]))), L_arm = self.att_arms[-1])
            #give p2 joint as current arm's upper anchor
            self.att_arms[-1].Upper_anchor = upper_anchor
            #append p2 joint to joints list
            self.att_joint(upper_anchor)

        #     print(self.att_joints[arm].anchor_point)#######
        # print(self.att_joints[arm+1].anchor_point)#######

            #give current arm as p2 joint's lower_arm
            #self.att_joints[-1].lower_arm = self.att_arms[-1]
        


    #------------------------------------------------------------
    def updateAngle(self,arm:int, angle:float):
        '''
        Args:    
            arm = start with 1
            angle = write the new angle
        '''
        arm = arm-1
        self.att_arms[arm].angle = angle
        for i in range(len(self.att_arms)):
            self.att_arms[i].Upper_anchor.anchor_point = self.att_joints[(1+i)].calc_anchor()
    
