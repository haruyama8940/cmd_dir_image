#!/usr/bin/python

import cmd
from platform import node
import rospy
import roslib
roslib.load_manifest('cmd_dir_image')
import cv2
from std_msgs.msg import Int8MultiArray

class cmd_dir_image_node:
    def __init__(self):
        rospy.init_node('cmd_dir_img')
        self.file_go = roslib.packages.get_pkg_dir('cmd_dir_image')+ '/images/go.png'
        self.file_right = roslib.packages.get_pkg_dir('cmd_dir_image')+ '/images/right.png'
        self.file_left = roslib.packages.get_pkg_dir('cmd_dir_image')+ '/images/left.png'
        self.file_con = roslib.packages.get_pkg_dir('cmd_dir_image')+ '/images/con.png'
        self.imgCV_go = cv2.imread(self.file_go)  # flagsは省略（デフォ値＝1)
        self.imgCV_right = cv2.imread(self.file_right)
        self.imgCV_left = cv2.imread(self.file_left)
        self.imgCV_con = cv2.imread(self.file_con)
        self.cmd_dir_list = []
        self.old_cmd_dir_list =[]
        self.cmd_dir_sub = rospy.Subscriber("/cmd_dir",Int8MultiArray, self.cmd_dir_callback)
    
    def cmd_dir_callback(self,data):
        self.cmd_dir_list = data #list
        
    def loop(self):
        
        if self.old_cmd_dir_list != self.cmd_dir_list:
             
            if self.cmd_dir_list[0] == 100:
                cv2.imshow("image", self.imgCV_con)
            
            if self.cmd_dir_list[1] == 100:
                cv2.imshow("image", self.imgCV_go)
            
            if self.cmd_dir_list[2] == 100:
                cv2.imshow("image", self.imgCV_left)

            if self.cmd_dir_list[3] == 100:
                cv2.imshow("image", self.imgCV_right)

        else:
            pass

        self.old_cmd_dir_list = self.cmd_dir_list

if __name__ == '__main__':
    hoge = cmd_dir_image_node
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        hoge.loop()
        rate.sleep()