#!/usr/bin/bash

shift
screen -d -m bash -c 'ros2 launch turtlebot3_xacro bringup_launch.py $@'
