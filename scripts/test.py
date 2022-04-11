#!/usr/bin/python3

from platform import node
import rospy
import roslib
import time
roslib.load_manifest('cmd_dir_image')
import cv2
from std_msgs.msg import Int8MultiArray

class cmd_dir_image_node:
    def __init__(self):
        self.file_go = roslib.packages.get_pkg_dir('cmd_dir_image')+ '/images/go.png'
        self.file_right = roslib.packages.get_pkg_dir('cmd_dir_image')+ '/images/right.png'
        self.file_left = roslib.packages.get_pkg_dir('cmd_dir_image')+ '/images/left.png'
        self.file_con = '/home/haru/catkin_ws/src/cmd_dir_image/images/con.png'
        #roslib.packages.get_pkg_dir('cmd_dir_image')+ '/images/con.png'
        self.imgCV_go = cv2.imread(self.file_go)  # flagsは省略（デフォ値＝1)
        self.imgCV_right = cv2.imread(self.file_right)
        self.imgCV_left = cv2.imread(self.file_left)
        self.imgCV_con = cv2.imread('con.png')
        self.cmd_dir_list = []
        self.old_cmd_dir_list =[]
        self.cmd_dir_sub = rospy.Subscriber("/cmd_data",Int8MultiArray, self.cmd_dir_callback)
    
    def cmd_dir_callback(self,data):
        self.cmd_dir_list = data #list
        
    def loop(self):
        
    #     if self.old_cmd_dir_list != self.cmd_dir_list:
             
    #         if self.cmd_dir_list[0] == 100:
        cv2.imshow('dir', self.imgCV_con)
        cv2.waitKey(1)
            # if self.cmd_dir_list[1] == 100:
            #     cv2.imshow("dir", self.imgCV_go)
            
            # if self.cmd_dir_list[2] == 100:
            #     cv2.imshow("dir", self.imgCV_left)

            # if self.cmd_dir_list[3] == 100:
            #     cv2.imshow("dir", self.imgCV_right)

        # else:
        #     pass

        # self.old_cmd_dir_list = self.cmd_dir_list

if __name__ == '__main__':
    rospy.init_node('cmd_dir_img')
    hoge = cmd_dir_image_node()
    # #r = rospy.Rate(1)
    # while not rospy.is_shutdown():
    #     hoge.loop
    # #    r.sleep()