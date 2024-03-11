cmake_minimum_required(VERSION 3.5)
project(turtlebot3_xacro)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch config urdf DESTINATION share/${PROJECT_NAME})

file(GLOB scripts scripts/*)
install(PROGRAMS ${scripts} DESTINATION lib/${PROJECT_NAME})

ament_package()
