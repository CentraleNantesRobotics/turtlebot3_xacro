#!/usr/bin/env bash

screen -dm ros2 launch turtlebot3_xacro bringup_launch.py "${@}"
