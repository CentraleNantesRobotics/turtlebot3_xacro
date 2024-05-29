#!/usr/bin/env python3
#
# Copyright 2019 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: Darby Lim
#
# adapted to multi-robot + simple_launch, Olivier Kermorgant

import os
from simple_launch import SimpleLauncher
from nav2_common.launch import RewrittenYaml


def generate_launch_description():
    TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']
    
    sl = SimpleLauncher(use_sim_time=False)
    
    # all happens in this namespace
    
    name = sl.declare_arg('name', os.uname().nodename)
    sl.declare_arg('cam', True)
    
    sl.declare_arg('usb_port', default_value='/dev/ttyACM0', description='Connected USB port with OpenCR')
    
    sl.declare_arg('tb3_param_dir',
                   sl.find('turtlebot3_xacro', TURTLEBOT3_MODEL + '.yaml'),
                   description='Full path to turtlebot3 parameter file to load')
    
    with sl.group(ns=name):
        
        sl.robot_state_publisher('turtlebot3_xacro','turtlebot3_' + TURTLEBOT3_MODEL + '.urdf.xacro',
                                 xacro_args={'prefix': name+'/'})
        
        sl.node('hls_lfcd_lds_driver', 'hlds_laser_publisher',
            parameters={'port': '/dev/ttyUSB0', 'frame_id': name/'base_scan'},
            output='screen')
        
        configured_params = RewrittenYaml(
                            source_file=sl.arg('tb3_param_dir'),
                            root_key=name,
                            param_rewrites={'frame_id': name/'odom',
                                            'child_frame_id': name/'base_footprint'},
                            convert_types=True)

        sl.node('turtlebot3_node', 'turtlebot3_ros',
                parameters=[configured_params],
                arguments=['-i', sl.arg('usb_port')])

    with sl.group(if_arg='cam'):
        sl.include('turtlebot3_xacro', 'cam_launch.py', launch_arguments={'name': name})

    return sl.launch_description()
