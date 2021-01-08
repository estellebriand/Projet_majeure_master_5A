# Ros matlab and raspberry pi
Pour connecter ros matlab au roscore de la raspberry:
- suivre network_ros.md pour configurer correctement la raspberry pi
- raspberry -> launch roscore et les noeuds
- Matlab -> ```rosinit("192.168.1.54")```

## Get/Put file
[Wiki matlab](https://fr.mathworks.com/help/ros/ref/putfile.html)

Tout d'abord il faut se connecter en ssh pour pouvoir avoir accès au fichier. Avec le rosinit on sera connecter au roscore et avec rosdevice on sera comme en ssh sur la raspberry.

Matlab:

```matlab
device = rosdevice('192.168.1.54','ros-ubuntu','projet2020')
% Telecharger un fichier de la rasp vers le PC:
getFile(d,'~/Bureau/projet_ws/bagfiles/bagfile.bag')
% Envoyer un fichier du PC vers la rasp:
putFile(d,'test_file.txt','~/Bureau/projet_ws')
% Supprimer un fichier sur la rasp
deleteFile(d,'~/Bureau/projet_ws/test_file.txt')
```

## Rosbag
les rosbag permet d'enregistrer les topics et leurs valeurs.
Il possible

## tutos
simulation gazebo + Ros matlab + detection couleur: https://github.com/mathworks-robotics/getting-started-ros

https://wiki.nps.edu/pages/viewpage.action?pageId=1149861927

http://wiki.ros.org/rosbag/Tutorials
