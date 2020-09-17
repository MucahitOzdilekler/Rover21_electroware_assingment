#!/usr/bin/env python
import rospy
from std_msgs.msg import String 


def callback(data):
		
	rospy.loginfo(data.data) 
	


def subs():

	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber('/position/drive', String,callback)

	rospy.Subscriber('/position/robotic_arm', String,callback)
	    
	rospy.spin()


if __name__ == '__main__':
	
	subs()		

