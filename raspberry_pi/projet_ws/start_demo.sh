#!/bin/bash
#this script will execute all the commands to start the projet
#Usage: ./start_nodes

#set all the permission
echo ============= Autorisation des ports USB =============
sudo chmod 666 /dev/ttyUSB0
sudo chmod 666 /dev/ttyUSB1
#sudo chmod 666 /dev/ttyACM0
echo ============= Check IP address =============

ipadress=`hostname -I`
echo $ipadress
#echo 'export ROS_HOSTNAME=192.168.1.54' >> ~/.bashrc
#do a source
source ~/.bashrc
source ~/Bureau/projet_ws/devel/setup.bash

#execute the launch file
echo ============= Execute  roslaunch sensor =============
#roslaunch rplidar_ros rplidar.launch 
#roslaunch projet publisher.launch 
#rosrun rosserial_python serial_node.py /dev/ttyUSB1
roslaunch projet start_sensors.launch

