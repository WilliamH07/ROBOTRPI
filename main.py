
from matplotlib.pyplot import step
import RPi.GPIO as GPIO

from pyPS4Controller.controller import Controller

import threading
import time

import dynamixelPS4
import stepperPS

count = 0 #set the loop

###########################
# Actual motor control
###########################
#
GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor

dynamixelPS4  
stepperPS
def stepper() :    
                    def on_L3_left(self,value):
                        print("L3 direction gauche", value) 
                        motorbase.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                                            "Half" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                                            200, # number of steps
                                            .0005, # step delay [sec]
                                            False, # True = print verbose output 
                                            .05) # initial delay [sec]
                    def on_L3_right(self,value):
                        print("L3 direction droit", value) 
                        motorbase.motor_go(True, # True=Clockwise, False=Counter-Clockwise
                                            "Half" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                                            200, # number of steps
                                            .0005, # step delay [sec]
                                            False, # True = print verbose output 
                                            .05) # initial delay [sec]

                    def on_L3_up(self,value):
                        print("L3 direction haut", value) 
                        motorshoulder.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                                            "Half" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                                            200, # number of steps
                                            .0005, # step delay [sec]
                                            False, # True = print verbose output 
                                            .05) # initial delay [sec]
                    def on_L3_down(self,value):
                        print("L3 direction bas", value) 
                        motorshoulder.motor_go(True, # True=Clockwise, False=Counter-Clockwise
                                            "Half" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                                            200, # number of steps
                                            .0005, # step delay [sec]
                                            False, # True = print verbose output 
                                            .05) # initial delay [sec]

                    def on_R3_up(self,value):
                        print("L3 direction haut", value) 
                        motorend .motor_go(False, # True=Clockwise, False=Counter-Clockwise
                                            "Half" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                                            200, # number of steps
                                            .0005, # step delay [sec]
                                            False, # True = print verbose output 
                                            .05) # initial delay [sec]
                    def on_R3_down(self,value):
                        print("R3 direction bas", value) 
                        motorend.motor_go(True, # True=Clockwise, False=Counter-Clockwise
                                            "Half" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                                            200, # number of steps
                                            .0005, # step delay [sec]
                                            False, # True = print verbose output 
                                            .05) # initial delay [sec]
def dynamixel() : 
    dxl_goal_position = [DXL_MINIMUM_POSITION_VALUE, DXL_MAXIMUM_POSITION_VALUE]         # Goal position

    def on_R2_press(self,value):
                    print("R2", value) 

    def on_R1_press(self,value):
                    print("R1", value)                
    
    def on_R3_left(self,value):
                        print("R3 gauche", value) 

    def on_R3_right(self,value):
                        print("R3 droit", value) 

    def on_up_arrow_press(self):
                        print("Fleche haut") 

    def on_down_arrow_press(self):
                        print("Fleche bas") 

    # Get Dynamixel#1 present position value
    dxl1_present_position = groupSyncRead.getData(DXL1_ID, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)

    # Get Dynamixel#2 present position value
    dxl2_present_position = groupSyncRead.getData(DXL2_ID, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)

    print("[ID:%03d] GoalPos:%03d  PresPos:%03d\t[ID:%03d] GoalPos:%03d  PresPos:%03d" % (DXL1_ID, dxl_goal_position[index], dxl1_present_position, DXL2_ID, dxl_goal_position[index], dxl2_present_position))


t1 = threading.Thread(target=stepper)
t2 = threading.Thread(target=dynamixel)

while count < 5: #for the loop

    t1.start()
    t2.start()
    finish = time.perf_counter
