
import numpy as np
import math
        
class Joint():
    """Class for making and editing joints used to join arm section in Robotic arm
    """
    def __init__(self, anchor_point: list = None, L_arm = None, U_arm = None, att_base: bool = False) -> None:
        """
        Class for making and editing joints used to join arm section in Robotic arm

        Args:
            anchor_point (list, optional): anchor point for joint (x,y). Defaults to None.
            L_arm (_type_, optional): lower arm anchor object. Defaults to None.
            U_arm (_type_, optional): upper arm anchor object. Defaults to None.
            att_base (bool, optional): flag, if attached to base. Defaults to False.
        """
        self.__lower_arm = L_arm
        self.__upper_arm = U_arm
        self.__att_2_base = att_base
        self.__anchor_point = anchor_point

        if not self.att_2_base:
            self.anchor_point = self.calc_anchor()
    
    @property
    def lower_arm(self) -> object:
        return self.__lower_arm
    
    @lower_arm.setter
    def lower_arm(self, val: object) -> None:
        self.__lower_arm = val
    
    @property
    def upper_arm(self) -> object:
        return self.__upper_arm
    
    @upper_arm.setter
    def upper_arm(self, val: object) -> None:
        self.__upper_arm = val
    
    @property
    def att_2_base(self) -> bool:
        return self.__att_2_base
    
    @property
    def anchor_point(self) -> list:
        return self.__anchor_point
    
    @anchor_point.setter
    def anchor_point(self, val: list) -> None:
        self.__anchor_point = val
    
    def calc_anchor(self):
        # print(self.upper_arm)
        theta = math.radians(self.lower_arm.angle)
        dx = self.lower_arm.arm_dim[2] * math.cos(theta)
        dy = self.lower_arm.arm_dim[2] * math.sin(theta)
        # print("dx,dy")
        # print(dx,dy)
        
        x1 = self.lower_arm.lower_anchor.anchor_point[0]
        y1 = self.lower_arm.lower_anchor.anchor_point[1]
        # print("x1,y1")
        # print(x1,y1)

        x2p = x1 + dx
        y2p = y1 - dy
        
        return (x2p,y2p)
        