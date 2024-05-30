# xacro files for Turtlebot3 in ROS 2

This packages builds upon `turtlebot3_description` with xacro models.

Use the `prefix` argument to rename all links e.g. `prefix:=turtle1/` leads to `turtle1/base_link`.

It is used to rename all links within the model, together with a namespaced execution, allowing an easy multi-robot setup.

It is compatible with spawning the models in Gazebo by using the `namespace` to remap the topics.

## Bringup

Assuming you have `simple_launch` and `nav2_common`, running the included `bringup_launch.py` will run ROS 2 on the Turtlebot and prefix or namespace nodes, topics and TF links with the `HOSTNAME` of the Turtlebot.

Running `bringup.sh` will launch this file in a detached screen.

Bringup can be run at boot with the package `robot-upstart`.

Meshes are set to package-relative paths (e.g. `$(find turtlebot3_description)/meshes/*`) so that a remote computer can find them  even if on a different absolute path, that may happen if using another ROS 2 distro.

In order to track a `(v,w)` command as close as possible, an intermediary node `cmd_vel_scale` will run and subscribe to `cmd_vel`. It will scale down the required velocity and forward it to the Turtlebot on `cmd_vel_scaled`. This allows not worrying about too high controls, while maintaining the curvature of the path.

## Upload in Ignition/Gazebo

The `upload_launch.py` will spawn a Turtlebot inside Ignition. Currently only `cmd_vel` and `odom` topics are bridged.

In this case the meshes are set to their absolute path (e.g. `/path/to/turtlebot3_description/meshes/*`) so that Gazebo can find them.

## Work in progress

Prefixed models:

 - `turtlebot3_waffle_pi.urdf.xacro`
 - `turtlebot3_burger.urdf.xacro`
