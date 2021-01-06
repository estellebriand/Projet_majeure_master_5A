# Installation de ROS

## Suivant le site officiel
[ROS wiki installation](http://wiki.ros.org/melodic/Installation/Ubuntu).

Cependant lors de la configuration, on peut ermarqué l'installation de python2 et non 3. Or nous allons probablement utilisé opencv version 4.5 pour de la détection d'objet et cette version n'est disponible que pour python3.

## Premiere tentative
https://www.miguelalonsojr.com/blog/robotics/ros/python3/2019/08/20/ros-melodic-python-3-build.html

Le premier catkin_make fonctionne mais dès que l'on a plus de 1 package, le build ne peut pas se finir, notemment avec le package dynamixel.
