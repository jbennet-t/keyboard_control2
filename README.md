# keyboard_control2
_Note: This is a modified version of keyboard_control developed for ROS1 Noetic, and ported to ROS2 Foxy._

_Original: https://github.com/jbennet-t/keyboard_control_

This is a basic keyboard teleoperation/control module built for ROS2 Foxy. Interfaces with Twist in ROS2, and publishes to /cmd_vel for simple robot control. 

### How to Install
1. cd to the src folder in your catkin workspace, and clone this repository there (assuming you have ros and git installed)
2. ```git clone https://github.com/jbennet-t/keyboard_control2.git```
3. Install the python getch module: ```pip3 install getch```

### How to Run
1. In the first terminal tab


Note: you may have to install pip3 and if it is not already part of your python install
* pip install: https://pip.pypa.io/en/stable/installing/
