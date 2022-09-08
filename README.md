# London Live Weather Update using ROS Launch
## Publish and Subscribe Method with ROS Launch - Intelligent Systems and Robotics

In this project, we have developed a same system as given in chapter one but with the use of ‘Launch’ feature of ROS. Launch files provide a convenient way to start up multiple nodes and a master, as well as other initialization requirements such as setting parameters. Also it automatically start roscore if it detects that it is not already running. 


* Python Files Description
  ------------

We have developed this system in ROS using publisher, subscriber and Launch file method where:

1.	London_weather_pub file: a publisher node where ‘London’ as a city name will be published on the topic named as ‘Weather’.

2.	London_weather_sub file: a publisher as well as subscriber node where Weather topic will be subscribed to get the desired data through making a call on OpenWeather API using API key. Once it retrieves the information, it will be published on multiple topics i.e. “Temperature” for current temperature and humidity and “Status” for weather status.

3.  For creating launch file, we added a new file in launch folder of our my_robot_tutorial directory with .launch extension where we mentioned the names of topics in publisher and subscriber nodes, the directory name and the name of the python files where these topics have been created. So, when we run this launch file, it started up both publisher and subscriber nodes.
 

* Requirements
  ------------

1.	Linux OS - Ubuntu 20.04 

2.	Python 3.7 or above 


* Output Results
  ------------
  
We can directly execute our launch file without running roscore in the background and it automatically starts publishing data on their respective topics as shown below: (roslaunch my_robot_tutorial weather.launch)

![alt text](https://github.com/WaniaKhance/London_Live_Weather_Update_using_ROS_Launch/blob/main/Picture3.png?raw=true)


