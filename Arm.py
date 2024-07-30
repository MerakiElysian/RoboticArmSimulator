import numpy as np

class Arm():
    def __init__(self, arm_dim: list = None, l_anchor: object = None, u_anchor: object = None, angle: float = 90):
        """
        Class for creating arms used in Robotic arm

        Args:
            arm_dim (list, optional): dimension for arm (x,y,w,h). Defaults to [10,2].
            l_anchor (object, optional): lower anchor(joint) object for current arm. Defaults to None.
            u_anchor (object, optional): upper anchor(joint) object for current arm. Defaults to None.
            angle (float, optional): angle of current arm with x-axis. Defaults to 90.
        """
        self.__arm_dim = arm_dim            #arm dimensions (x,y,w,h)
        self.__lower_anchor = l_anchor      #lower joint object
        self.__upper_anchor = u_anchor      #upper joint object
        self.__angle = angle                #arm angle
        
        self.calc_p1()
        
    @property
    def arm_dim(self) -> list:
        return self.__arm_dim
    
    @arm_dim.setter
    def arm_dim(self, val: list) -> None:
        self.__arm_dim = val
        
    @property
    def lower_anchor(self) -> object:
        return self.__lower_anchor
    
    @lower_anchor.setter
    def lower_anchor(self, val: object) -> None:
        self.__lower_anchor = val
        
    @property
    def Upper_anchor(self) -> object:
        return self.__upper_anchor
    
    @Upper_anchor.setter
    def Upper_anchor(self, val: object) -> None:
        self.__upper_anchor = val
        
    @property
    def angle(self) -> float:
        return self.__angle
    
    @angle.setter
    def angle(self, val: float) -> None:
        self.__angle = val

    def calc_p1(self):
        self.arm_dim = [self.lower_anchor.anchor_point[0], self.lower_anchor.anchor_point[1], self.arm_dim[2], self.arm_dim[3]]

    