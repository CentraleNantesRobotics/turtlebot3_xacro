cmake_minimum_required(VERSION 3.5)
project(turtlebot3_xacro)

find_package(ament_cmake REQUIRED)

# share meshes to Gazebo
ament_environment_hooks("hooks/resource_paths.dsv.in")

install(DIRECTORY launch config meshes urdf DESTINATION share/${PROJECT_NAME})

file(GLOB scripts scripts/*)
install(PROGRAMS ${scripts} DESTINATION lib/${PROJECT_NAME})

ament_package()
