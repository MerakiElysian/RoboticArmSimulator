#Simulator for simulation and testing of Wilson's(Robotic arm) movement in 3-Dimensions
import Robotic_arm as ra
import numpy as np
import pygame
import math
import Move
pygame.init()

win_x = 1200
win_y = 800
panel_width = 300

#color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)

window = pygame.display.set_mode((win_x,win_y))
pygame.display.set_caption("Robotic Arm Simulator")
clock = pygame.time.Clock()
window.fill((255,255,255))

#Active input tracking
global active_input, input_x , input_y
active_input = None
input_x = ""
input_y = ""
#input fields setup
inpRectX = pygame.Rect(win_x - panel_width + 50, 110,200,25) # box of input X
inpRectY = pygame.Rect(win_x - panel_width + 50, 140,200,25) # box of input Y
RunBox = pygame.Rect(win_x - panel_width + 40, 190,80,50)
SubmitBox = pygame.Rect(win_x - panel_width + 140, 190,100,50)
#function for side panel
def side_panel():
    #Font Setup
    Heading1 = pygame.font.SysFont('timesnewroman',25)
    Heading2 = pygame.font.SysFont('timesnewroman',20)

    #Render Text
    MainHeading = Heading1.render("Robotic Arm Simulator", False,'Red')
    Label1 = Heading2.render("Enter the new coordinate points",False,"Brown")
    Label1_1 = Heading2.render("X : ",False,"black")
    Label1_2 = Heading2.render("Y : ",False,"black")
    Run = Heading2.render("RUN",True,'White')
    Submit = Heading2.render("SUBMIT",True,"purple")
    
    #Rendering main panel
    pygame.draw.rect(window, (220, 220, 220), (win_x - panel_width, 0, panel_width, win_y))
    
    #Render input boxes
    pygame.draw.rect(window, LIGHT_BLUE if active_input == "X" else GRAY,inpRectX)
    pygame.draw.rect(window, LIGHT_BLUE if active_input == "Y" else GRAY,inpRectY)
    pygame.draw.rect(window,(100,100,255),RunBox)
    pygame.draw.rect(window,(255,100,100),SubmitBox)

    #Creating Rectangle for the input.
    
    window.blit(MainHeading,(win_x - panel_width + 20, 20))
    window.blit(Label1,(win_x - panel_width + 20, 80))
    window.blit(Label1_1,(win_x - panel_width + 20, 110))
    window.blit(Label1_2,(win_x - panel_width + 20, 140))
    window.blit(Run,(win_x - panel_width + 40 + 15, 190 + 15))
    window.blit(Submit,(win_x - panel_width + 140 + 15, 190 + 15))

    # Render input text
    X_text = Heading2.render(input_x,True, "black")
    Y_text = Heading2.render(input_y,True, "black")
    window.blit(X_text,(inpRectX.x + 2,inpRectX.y + 2))
    window.blit(Y_text,(inpRectY.x + 2,inpRectY.y + 2))
    
#Function for Arm lines
def drawLine(self):
    for arm in self.att_arms:
        line = pygame.draw.line(window,"black",arm.lower_anchor.anchor_point,arm.Upper_anchor.anchor_point,2)
#fun for finding mid of two joints
def findCenter(self):
    x1,y1 = self.lower_anchor.anchor_point
    x2,y2=  self.Upper_anchor.anchor_point
    # print(x1,y1,x2,y2) ################
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    # print(mx,my)  ####################
    return (mx, my)
# Function to rotate the surface
def rotate_surface(surface, angle):
    return pygame.transform.rotate(surface, angle)
#function for arm rectangle by using surface
def drawSurRect(self):
    for arm in self.att_arms:
        _arm = pygame.Surface((arm.arm_dim[2],arm.arm_dim[3]))
        _arm.set_colorkey((0,0,0))
        _arm.fill("red")
        __arm = pygame.transform.rotate(_arm,arm.angle)
        des=__arm.get_rect(center=findCenter(arm))
        
        window.blit(__arm,des)
        pygame.display.flip()

if __name__ == "__main__":
    print("starting simulation!")
    tok = False # For while condition
    # robot_arm = ra.Robotic_arm(total_arms = 3, arms_dim = [[0,0,180,20],[15,30,100,25],[65,45,200,15]])
    robot_arm = ra.Robotic_arm(total_arms = 2, arms_dim = [[0,0,180,20],[0,0,200,35]])

    #Change to new coordinate
    TheNewCoord = [[400,500],[600,300]]
    # TheNewCoord = [[400,500],[600,480],[500,250],[543,700]]
    print("the Base", robot_arm.att_joints[0].anchor_point)
    print("arm1 length = ", robot_arm.att_arms[0].arm_dim[2],"| arm2 length = ", robot_arm.att_arms[1].arm_dim[2])
    
#------------giving new coordinate to find the new angles of arms and saving it in an array-----------------
    a = Move.Move_arm(robot_arm,TheNewCoord)
    # global newPointsList 
    newPointsList = a.findNewAngles()  
    baseDim = robot_arm.base_dim # Defines tha base dimensions
    base = pygame.Rect(baseDim)
    
# Now putting this into for loop to iterate for every new points
    def moveArmLoop(NEWPOINTSLIST):
        # Drawing Arms
        for i in range(len(NEWPOINTSLIST)):
            window.fill((255,255,255))
        # Drawing Base rectangle
            pygame.draw.rect(window,(173,173,64),base)
            window.set_at((robot_arm.att_joints[0].anchor_point[0], robot_arm.att_joints[0].anchor_point[1]), (255,0,0))
        # Side Panel funtion call
            side_panel()
            # function for updating arm angles.
            robot_arm.updateAngle(1,newPointsList[i][0])
            robot_arm.updateAngle(2,newPointsList[i][1])
            # Drawing the new robotic arm image.
            drawSurRect(robot_arm)
            drawLine(robot_arm)
            pygame.display.flip()
            pygame.time.delay(1300)
# Here I am creating the function to show the last position of arm when click submit.
    def showArm(NEWPOINTSLIST):
        window.fill((255,255,255))
        pygame.draw.rect(window,(173,173,64),base)
        window.set_at((robot_arm.att_joints[0].anchor_point[0], robot_arm.att_joints[0].anchor_point[1]), (255,0,0))
    # Side Panel funtion call
        side_panel()  
        # function for updating arm angles.
        robot_arm.updateAngle(1,newPointsList[-1][0])
        robot_arm.updateAngle(2,newPointsList[-1][1])
        # Drawing the new robotic arm image.
        drawSurRect(robot_arm)
        drawLine(robot_arm)
        pygame.display.flip()

    while not tok:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tok = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if inpRectX.collidepoint(event.pos):
                    active_input = "X"
                elif inpRectY.collidepoint(event.pos):
                    active_input = "Y"
                elif SubmitBox.collidepoint(event.pos):
                    print(f"Submitted X : {input_x} , Y : {input_y}")
                    TheNewCoord.append([int(input_x),int(input_y)])
                    newPointsList = a.findNewAngles() 
                    print("The new array ",TheNewCoord)
                    input_x = ""
                    input_y = ""
                    active_input = None
                    showArm(newPointsList)
                elif RunBox.collidepoint(event.pos):
                    print("Running")
                    # input_x = ""
                    # input_y = ""
                    # active_input = None
                    #Run the loop below with move arm funtion 
                    moveArmLoop(newPointsList)
                    print(newPointsList)
                else:
                    active_input = None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press Escape to exit
                    tok = True
                elif active_input == "X":
                    if event.key == pygame.K_BACKSPACE:
                        input_x = input_x[:-1]
                    else:
                        input_x += event.unicode
                elif active_input == "Y":
                    if event.key == pygame.K_BACKSPACE:
                        input_y = input_y[:-1]
                    else:
                        input_y += event.unicode
                    
        side_panel()
        pygame.display.update()
        
        # pygame.time.delay(2000)
        clock.tick(60)
pygame.quit()