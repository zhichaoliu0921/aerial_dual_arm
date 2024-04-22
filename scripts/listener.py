#!/usr/bin/env python

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState


position = []

def callback(data):
    global position
    position = data.position
    numbers_as_strings = [str(num) for num in position]
    rospy.loginfo('I heard %s', ', '.join(numbers_as_strings))
def timer_callback(event):
     # output the value to the servo at certain frequency e.g. 100hz
    pass


def main():

    rospy.init_node('listener', anonymous=True)
    # Set the timer to run the callback function at 100 Hz (every 0.01 seconds)
    timer = rospy.Timer(rospy.Duration(0.01), timer_callback)
    rospy.Subscriber('joint_states', JointState, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()
