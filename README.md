# keyboard_control2
----------------------------------------------------------------------------------------------------------
_Note: This is a modified version of keyboard_control developed for ROS1 Noetic, and ported to ROS2 Foxy._

_Original: https://github.com/jbennet-t/keyboard_control_

----------------------------------------------------------------------------------------------------------


This is a basic keyboard teleoperation/control module built for ROS2 Foxy. Interfaces with Twist in ROS2, and publishes to turtlesim1/cmd_vel for simple robot control. If you want to publish to the standard /cmd_vel for more genral robot control, change the line ```publisher = node.create_publisher(Twist, 'turtle1/cmd_vel', 10)``` to ```publisher = node.create_publisher(Twist, 'cmd_vel', 10)```

### How to Install
1. cd to the src folder in your ros2 workspace, and clone this repository there (assuming you have ros2 and git installed)
2. ```git clone https://github.com/jbennet-t/keyboard_control2.git```
3. Install the python getch module: ```pip3 install getch```

### How to Run
1. In the first terminal tab, cd to the top level of your ros2 directory
2. Source your setup.bash: ```source /opt/ros/foxy/setup.bash``` and ```. install/setup.bash```
3. Build the keyboard_control2 package: ```colcon build --packages-select keyboard_control2```
4. Run the package: ```ros2 run keyboard_control2 keyboard_input3```
5. In a new tab, cd to the top level of your ros2 directory
6. Source again: ```source /opt/ros/foxy/setup.bash``` and ```. install/setup.bash```
7. Run turtlesim```ros2 run turtlesim turtlesim_node```
8. With the turtlesim window on the side, select the terminal running keyboard_control2, and follow the on-screen instructions



Note: you may have to install pip3 and if it is not already part of your python install
* pip install: https://pip.pypa.io/en/stable/installing/
