#!/usr/bin/env python

# Author: sgl
# data: 2018/07/09
# function: in ros, synchronize the imu info and the image info

import message_filters
from sensor_msgs.msg import Image, Imu
import rospy

def callback(image, camera_info):
#Solve all of perception here...
    pass


image_sub = message_filters.Subscriber('image', Image)
imu_sub = message_filters.Subscriber('imu', Imu)

ts = message_filters.TimeSynchronizer([image_sub, imu_sub], 10)
ts.registerCallback(callback)
rospy.spin()