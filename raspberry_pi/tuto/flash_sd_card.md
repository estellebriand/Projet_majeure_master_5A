# How to flash sd card for our projet

## On your Laptop

- download the image:
[ubuntu-mate-18.04.2](https://releases.ubuntu-mate.org/archived/bionic/armhf/ubuntu-mate-18.04.2-beta1-desktop-armhf%2Braspi-ext4.img.xz)
 - download [raspberry pi imager](https://downloads.raspberrypi.org/imager/imager_1.5.exe), it's helping you to flash the sd card
 - then execute the application and select our os image:
 ![selection os](tuto1.png)
 - select your sd card and write
 ![selection os](tuto2.png)

 Remove your sd card from you laptop and put it in raspberry.

 ## On the raspberry pi 3B

 - Powered the raspberry pi
 - Follow the configuration
 
 - Choose user and password
    - user: ros-ubuntu
    - password: projet2020

--> Don't upgrade to 20.0 !! ROS will not be compatible with.

- you have to update your package : 

```shell
$ sudo apt update
```

- restart

- install git

```shell
$ sudo apt-get git
```

- install ROS 

following the [ROS wiki installation](http://wiki.ros.org/melodic/Installation/Ubuntu).

If you have enough space on your sd card, install

```shell
$ sudo apt install ros-melodic-desktop
```

Then ros is installed ! check with the command line:

```shell
$ ls /opt/ros/melodic
```

 and look if it exists.
- install opencv ( for object detection):

```shell
$ sudo apt update install python3-pip
$ sudo pip3 install opencv-python 
```

- On the desktop:

```shell
$ cd ~/Bureau
$ git clone --branch dev_briand https://gitlab.com/20-21_5ETI_PRJ/Sujet_5__Simulated_robotic_scenario/s5_g7_briand_guy_kahan_martinez.git 
```
Now you have your sd card configured correctly