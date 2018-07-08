#!/usr/bin/env python

# Author: sgl
# data: 2018/07/09
# function: in ros, get the QRcode center

import cv2

def callback(image, camera_info):
#Solve all of perception here...
    pass





if __name__=="__main__":
    image_sub = message_filters.Subscriber('image', Image)
    imu_sub = message_filters.Subscriber('imu', Imu)

    ts = message_filters.TimeSynchronizer([image_sub, imu_sub], 10)
    ts.registerCallback(callback)
    rospy.spin()

