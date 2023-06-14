import os
from simple_launch import SimpleLauncher


def generate_launch_description():
    TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']
    
    sl = SimpleLauncher(use_sim_time=True)
    
    name = sl.declare_arg('name', 'turtlebot')
    
    with sl.group(ns=name):
        
        sl.robot_state_publisher('turtlebot3_description','turtlebot3_' + TURTLEBOT3_MODEL + '.urdf.xacro',
                                 xacro_args={'prefix': sl.name_join(name, '/')})

    return sl.launch_description()
