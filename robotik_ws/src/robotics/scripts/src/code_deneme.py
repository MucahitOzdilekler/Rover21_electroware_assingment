#!/usr/bin/env python
import rospy
from std_msgs.msg import String 

def pub_drive(publishing_drive_data):
	
	pub = rospy.Publisher('/position/drive', String, queue_size=10)
       
	pub.publish(publishing_drive_data)
 

def pub_arm(publishing_arm_data):
	
	pub = rospy.Publisher('/position/robotic_arm', String, queue_size=10)
    
	pub.publish(publishing_arm_data)
      

def data_proces(camon_data):

	if len(camon_data)==18 and camon_data[0]=='A' and camon_data[17] == 'B' : 
		
		camon_data = camon_data[:-1:]
		
		camon_data = camon_data[1 : : ]
		
		split_strings = []
		
		n  = 4

		for index in range(0, len(camon_data), n):
		
			split_strings.append(camon_data[index : index + n])
		 	
		for i in range(4) :
			
			if int(split_strings[i]) > 1255 :
			
				split_strings[i] = '1255'
				
			elif int(split_strings[i]) > 255 and int(split_strings[i])<1000 :
			
				split_strings[i] = '0255' 
			
		
		camon_data = "".join(split_strings)
		
		camon_data_1 = list(camon_data)

		for i in range(0,16,4) :
			
			if camon_data_1[i] == '0':
			
			 camon_data_1[i] = ' -'
			
			elif camon_data_1[i] == '1':
			
			 camon_data_1[i] = ' '
				
		camon_data = "".join(camon_data_1)
		
		print(camon_data)

		camon_data = camon_data[1::]
		
		pub_drive(camon_data)
	    	
    
	elif len(camon_data)==26 and camon_data[0]=='A' and camon_data[25] == 'B' :
				
		camon_data = camon_data[:-1:]
		
		camon_data = camon_data[1 : : ]

		split_strings = []
		
		n  = 4

		for index in range(0, len(camon_data), n):
		
			split_strings.append(camon_data[index : index + n])
		   	
		
		for i in range(4) :
			
			if int(split_strings[i]) > 1255 :
		
				split_strings[i] = '1255'
				
			elif int(split_strings[i]) > 255 and int(split_strings[i])<1000 :
		
				split_strings[i] = '0255' 
			
		
		camon_data = "".join(split_strings)
		
		camon_data_1 = list(camon_data)

		for i in range(0,24,4) :
			
			if camon_data_1[i] == '0':
			
			 camon_data_1[i] = ' -'
			
			elif camon_data_1[i] == '1':
			
			 camon_data_1[i] = ' '
		
		camon_data = "".join(camon_data_1)
		
		print(camon_data)

		camon_data = camon_data[1::]
		
		pub_arm(camon_data)


def callback(data):
		
	rospy.loginfo(data.data) 
	
	
	string_data = data.data

	return string_data


def subs():

	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber('/serial/drive', String,callback)

	rospy.Subscriber('/serial/robotic_arm', String,callback)
	


if __name__ == '__main__':
	
	while not  rospy.is_shutdown():


		subs()	

		data_proces(callback())


		rospy.spin()	


