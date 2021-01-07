# Installation de ROS

## Suivant le site officiel
[ROS wiki installation](http://wiki.ros.org/melodic/Installation/Ubuntu).

Cependant lors de la configuration, on peut ermarqué l'installation de python2 et non 3. Or nous allons probablement utilisé opencv version 4.5 pour de la détection d'objet et cette version n'est disponible que pour python3.

## Premiere tentative
https://www.miguelalonsojr.com/blog/robotics/ros/python3/2019/08/20/ros-melodic-python-3-build.html

Le premier catkin_make fonctionne mais dès que l'on a plus de 1 package, le build ne peut pas se finir, notemment avec le package dynamixel.

Erreur du make -j4 -l4

## Deuxieme tentative
http://wiki.ros.org/UsingPython3/BuildUsingPython3

essai mais pareil lors du build ça ne fonctionne pas.
besoin de ROS neotic.

On retourne sur ROS melodic avec python2.7 et lors des essais avec la detection. Nous trouverons une solution alternative.

## Installer darknet rapsberry pi 3B
https://github.com/stanfordroboticsclub/RPI-Darknet?fbclid=IwAR2x4Zz1TSCKb-BcZhmubIMINv19E4TcxPDvtAaAM7hQPOCdbDufUoWMwyE