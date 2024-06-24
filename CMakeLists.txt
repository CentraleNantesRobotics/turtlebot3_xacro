cmake_minimum_required(VERSION 3.5)
project(turtlebot3_xacro)

find_package(ament_cmake REQUIRED)

# assume turtlebot3_description was installed through apt
set(TURTLEBOT3_DESCRIPTION_SHARE "/opt/ros/$ENV{ROS_DISTRO}/share" CACHE STRING "Path to folder containing share of turtlebot3_description package (for Gazebo hooks)")
ament_environment_hooks("hooks/resource_paths.dsv.in")

install(DIRECTORY launch config urdf DESTINATION share/${PROJECT_NAME})

file(GLOB scripts scripts/*)
install(PROGRAMS ${scripts} DESTINATION lib/${PROJECT_NAME})

ament_package()
