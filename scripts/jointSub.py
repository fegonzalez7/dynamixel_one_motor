#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState

def callback(data):
    rospy.loginfo(data.position)
    if data.position[4]>-2:
        print('gripper abierto')
    else:
        print('gripper cerrado')
    
def listener():
    rospy.init_node('joint_listener', anonymous=True)
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            listener()
    except rospy.ROSInterruptException:
        pass