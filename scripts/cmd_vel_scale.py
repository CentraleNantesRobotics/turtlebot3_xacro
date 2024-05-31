#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class Scaler(Node):
    def __init__(self):
        super().__init__('cmd_vel_scale')

        self.sub = self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_cb, 1)

        self.pub = self.create_publisher(Twist, 'cmd_vel_scaled', 1)
        self.cmd = Twist()

        self.base = 0.287
        self.vmax = 0.26

    def cmd_vel_cb(self, twist: Twist):

        v = twist.linear.x
        w = twist.angular.z

        vl = v + self.base*w/2
        vr = v - self.base*w/2

        scale = max(abs(vl), abs(vr))/self.vmax

        if scale > 1.:
            v = v/scale
            w = w/scale

        self.cmd.linear.x = v
        self.cmd.angular.z = w
        self.pub.publish(self.cmd)


rclpy.init(args=None)
node = Scaler()
rclpy.spin(node)
node.destroy_node()
rclpy.shutdown()
