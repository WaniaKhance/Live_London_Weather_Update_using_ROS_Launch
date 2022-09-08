#!/usr/bin/env python3
import pyowm
import rospy
from std_msgs.msg import String
from math import pi


def weather_pub():
    rospy.init_node("weather_pub_node")
    pub = rospy.Publisher("Weather", String , queue_size = 10)

    rate = rospy.Rate(5)
    text = 'London'
    while not rospy.is_shutdown():
        pub.publish(text)


if __name__ == '__main__':
    try:
        weather_pub()
    except rospy.ROSInterruptException:
        pass
