#!/usr/bin/env python

#Program: keyboard_input.py
#Purpose: Acts as a publisher to the /cmd_vel topic and takes keyboard input to control ros robot
#Authors: Jordan Sinoway,


import rclpy
from rclpy.qos import qos_profile_default

import sys #for exiting purposes
import getch #theoretically gets keyboard input. need pip3 to install
#to install 'pip3 install getch'

from geometry_msgs.msg import Twist #import geometry stuff
from std_msgs.msg import String #for pushing info to terminal


directionInfo = """
Taking input from keyboard and publishing to /cmd_vel

Movement:
q   w   e   up/l  up  up/r
  a   d       left right
    s            down

    r       accelerate by 10%
    t       deccelerate by 10%

Hit esc to exit
-----------------
"""

def get_keys(): #gets keyboard input
    key = 0
    k = ord(getch.getch()) #converts keypress to ord value
    if (k==119):
        key = 1 #up
    elif (k==115):
        key = 2 #down
    elif (k==97):
        key = 3 #left
    elif (k==100):
        key = 4 #right
    elif (k==113):
        key = 5 #turn left and forward
    elif (k==101):
        key = 6 #turn right and forward
    elif (k==114):
        key = 7 #accelerate
    elif (k==116):
        key = 8 #deccelerate
    elif (k==27):
        sys.exit("Exited Progam")
    else:
        key = 0
    #rospy.loginfo(str(key)) #write val to terminal
    return key


def velocityOut(speed,turn): #for printing/getting speed & turn angle
    return "speed & turn angle: \tspeed %s\tturn %s " % (speed,turn)


def keyboard_input():
    speed = rclpy.get_param("~speed", 0.5) #default speed val
    turn = rclpy.get_param("~turn", 1.0) #default turn val
    x = 0
    y = 0
    z = 0
    th = 0
    status = 0

    while not rclpy.is_shutdown():
        input = get_keys()
        if(input == 1): #up
            x = 1
            y = 0
            z = 0
            th = 0
        elif(input == 2): #down
            x = -1
            y = 0
            z = 0
            th = 0
        elif(input == 3): #left
            x = 0
            y = 0
            z = 0
            th = 1
        elif(input == 4): #right
            x = 0
            y = 0
            z = 0
            th = -1
        elif(input == 5): #left + forward
            x = 1
            y = 0
            z = 0
            th = 1
        elif(input == 6): #right + forward
            x = 1
            y = 0
            z = 0
            th = -1
        elif(input == 7): #accelerate by 10%
            x = 0
            y = 0
            z = 0
            th = 0
            speed += 0.1
        elif(input == 8): #deccelerate by 10%
            x = 0
            y = 0
            z = 0
            th = 0
            speed -= 0.1
        else:
            x = 0
            y = 0
            z = 0
            th = 0

        twist = Twist()
        twist.linear.x = x*speed
        twist.linear.y = y*speed
        twist.linear.z = z*speed
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = th*turn
        pub.publish(twist)
        print(velocityOut(speed,twist.angular.z)) #write speed/angle to terminal


def main(args=None):
    if args is None:
	       args = sys.argv

    rclpy.init(args=args)

    node = rclpy.create_node('keyboard_input2')

    pub = rclpy.create_publisher(Twist, 'cmd_vel', qos_profile_default)

    print(directionInfo)
    keyboard_input()



if __name__ == '__main__':
    try:
        main()
    except:
        print(e)
