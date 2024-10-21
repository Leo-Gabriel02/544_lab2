import sys

from utilities import Logger, euler_from_quaternion
import rclpy
from rclpy.time import Time
from rclpy.node import Node
from rclpy.qos import QoSProfile

from nav_msgs.msg import Odometry as odom

from rclpy import init, spin

rawSensor = 0
class localization(Node):
    
    def __init__(self, localizationType=rawSensor):

        super().__init__("localizer")
        
        # TODO Part 3: Define the QoS profile variable based on whether you are using the simulation (Turtlebot 3 Burger) or the real robot (Turtlebot 4)
        # Remember to define your QoS profile based on the information available in "ros2 topic info /odom --verbose" as explained in Tutorial 3

        odom_qos=QoSProfile(
            reliability = rclpy.qos.ReliabilityPolicy.RELIABLE,
            durability = rclpy.qos.DurabilityPolicy.VOLATILE,
            history = rclpy.qos.HistoryPolicy.KEEP_LAST, # terminal output says UNKNOWN, I think we defaulted to this last time
            depth = 10
        )

        self.loc_logger=Logger("robot_pose.csv", ["x", "y", "theta", "stamp"])
        self.pose=None
        
        if localizationType == rawSensor:
        # TODO Part 3: subscribe to the position sensor topic (Odometry)
            self.odom_sub = self.create_subscription(odom, "/odom", self.odom_callback, odom_qos)
        else:
            print("This type doesn't exist", sys.stderr)
    
    
    def odom_callback(self, pose_msg):
        
        # TODO Part 3: Read x,y, theta, and record the stamp
        self.pose=[
            pose_msg.pose.pose.position.x,  # x
            pose_msg.pose.pose.position.y,  # y
            euler_from_quaternion(pose_msg.pose.pose.orientation),  # theta
            pose_msg.header.stamp.sec + pose_msg.header.stamp.nanosec* (1e-9)  # stamp
        ]
        
        # Log the data
        self.loc_logger.log_values(self.pose)
    
    def getPose(self):
        return self.pose

# TODO Part 3
# Here put a guard that makes the node run, ONLY when run as a main thread!
# This is to make sure this node functions right before using it in decision.py
if __name__ == "__main__":
    rclpy.init() # Initiate library
    localizer_node = localization()  # Initiate node
    try:
        rclpy.spin(localizer_node) 
    except KeyboardInterrupt: # Exit if interrupted
        print("Exiting")
