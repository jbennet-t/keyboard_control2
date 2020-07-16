import rclpy
from rclpy.node import Node

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

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('keyboard_input3')
    publisher = node.create_publisher(Twist, 'turtle1/cmd_vel', 10)


    def get_keys(): #gets keyboard input
        key = ''
        k = ord(getch.getch()) #converts keypress to ord value
        if (k==119):
            key = 'up' #up
        elif (k==115):
            key = 'down' #down
        elif (k==97):
            key = 'left' #left
        elif (k==100):
            key = 'right' #right
        elif (k==113):
            key = 'left_fwd' #turn left and forward
        elif (k==101):
            key = 'right_fwd' #turn right and forward
        elif (k==114):
            key = 'accel' #accelerate
        elif (k==116):
            key = 'deccel' #deccelerate
        elif (k==27):
            sys.exit("Exited Progam")
        else:
            key = ''
        #rospy.loginfo(str(key)) #write val to terminal
        return key


    def velocityOut(speed,turn): #for printing/getting speed & turn angle
        return "speed & turn angle: \tspeed %s\tturn %s " % (speed,turn)


    def keyboard_input():
        speed = 0.5 #default speed val
        turn = 1.0 #default turn val
        x = 0
        y = 0
        z = 0
        th = 0
        status = 0

        while (1):
            input = get_keys()
            if(input == 'up'): #up
                x = 1
                y = 0
                z = 0
                th = 0
            elif(input == 'down'): #down
                x = -1
                y = 0
                z = 0
                th = 0
            elif(input == 'left'): #left
                x = 0
                y = 0
                z = 0
                th = 1
            elif(input == 'right'): #right
                x = 0
                y = 0
                z = 0
                th = -1
            elif(input == 'left_fwd'): #left + forward
                x = 1
                y = 0
                z = 0
                th = 1
            elif(input == 'right_fwd'): #right + forward
                x = 1
                y = 0
                z = 0
                th = -1
            elif(input == 'accel'): #accelerate by 10%
                x = 0
                y = 0
                z = 0
                th = 0
                speed += 0.1
            elif(input == 'deccel'): #deccelerate by 10%
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
            publisher.publish(twist)
            print(velocityOut(speed,twist.angular.z)) #write speed/angle to terminal

    print(directionInfo)
    keyboard_input()

    rclpy.spin(node)


    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    try:
        main()
    except:
        print(e)
