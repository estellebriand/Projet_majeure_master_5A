# Projet de majeure "Robotique de service"
s5_g7_briand_guy_kahan_martinez

**Auteurs:** 
Estelle BRIAND
Nicolas GUY
Jeremie KAHAN
Paul MARTINEZ

# Cahier des charges

Creer un environement de simulaiton et une raspberry_pi qui sera connectée au robot réel et ses capteurs afin de pouvoir plannifier son parcours, les étapes à suivre et effectuer des tâches définies.

## Contraintes

- raspberry_pi 3 B
- Connection au PC une fois en début d'épreuve
- Vehicule doit être autonome
- Connection avec une arduino, capteurs(lidar et IMU) et camera
- Doit être capable de reconnaitre des points d'interets.

## Technologies utilisées:

- ROS (sur rapsberry pi)
    - rosserial --> arduino sur robot
    - dynamixel_motor --> controller moteur en position
    - rplidar_ros --> gestion du Lidar
    - hector_slam (simultaneous localization and mapping) --> gestion de la map 
- Matlab (sur PC)
    - ROS toolboxes
    - IHM
    - calcul des trajectoires
- Vision (sur rapsberry pi)
    - reconnaissance cannettes
    - reconnaissance couleur
- Capteurs : Lidar & IMU

# Listes des fonctionnalités :

1. [ ] Lidar
    1. [x] Detection obstacles
    2. [X] Envoie leur emplacement (devant/derriere/gauche/droite)
    3. [ ] Mapping ?
2. [ ] IHM
    1. [x] Affichage de la map
    2. [ ] Creation de la map
    3. [x] Affichage information de l'etat du robot
    4. [x] Affichage liste des commandes
3. [x] ROS Navigation
    1. [ ] Algorithme du plus court chemin
    2. [ ] ordre de déplacement 
4. [ ] Vision du robot
    1. [x] Detection d'objet "cannette"
    2. [ ] Detection de la couleur
    3. [ ] Calcule la distance de l'objectif
# Représentation des noeuds
> En cours de construction
```mermaid
graph LR
    T1[Odometry source] -- /odom --> Node((local_planner_student))
    T2[Laser source] -- /scan --> Node((local_planner_student))

    S1[ ] -. /move_to/singleGoal .-> Node
    S2[ ] -. /move_to/pathGoal .-> Node

    Node -- /cmd_vel_mux/input/navi -->D[base controller]
```

# Description de l'algo
> En cours de construction
```mermaid
sequenceDiagram
    participant Alice
    participant Bob
    Alice->John: Hello John, how are you?
    loop Healthcheck
        John->John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/>prevail...
    John-->Alice: Great!
    John->Bob: How about you?
    Bob-->John: Jolly good!
```

# Vidéos de présentation

[Lien vers la vidéo pitch youtube](url)

[Lien vers la vidéo tutoriel youtube](url)

# Liste des dépendances et pré-requis

- a
- b
# Mise en oeuvre
Suivre les wikis (section wiki de gitlab) dans l'ordre suivant:
- Flasher une carte SD pour rapsberry pi 3B
- Etablir la connection ssh raspberry pi - ordinateur windows
- How to use SLAM with a RPLidar on RaspberryPi 3B+ using ROS

### Exemple de planning type
![Image planning prévu](https://gitlab.com/20-21_5ETI_PRJ/Sujet_5__Simulated_robotic_scenario/s5_g7_briand_guy_kahan_martinez/-/raw/master/autre/Planning-Pr%C3%A9vu.PNG)

## Rendu par séances
Séance 1 du Lundi 04 Janvier 2021 matin :
- Jérémie : documentation et tests IHM Matlab
- Nicolas : Recherche documentation/codes capteurs IR/US + se replonger dans les codes servomoteur dynamixel AX12 du projet proto
- Paul : Documentation et entrainement 
- Estelle : Installation ubuntu mate + ROS sur raspberry, verifier le bon fonctionnement --> difficultés rencontrées avec la version 20, essai avec rasperry pi OS (debian)

Séance 2 du Lundi 04 Janvier 2021 après-midi :
- Jérémie : documentation liens Simulink-IHM Matlab et généralités sur les Digital Twins, découverte des toolboxes associées
- Estelle : Installation & tests ubuntu-mate-18.04.2-beta1-desktop-armhf+raspi-ext4.img 

Séance 3 du Mardi 05 Janvier 2021 matin :
- Jérémie : Mise au point objectifs du projet, matériel et documentation Toolboxes Matlab
- Paul : Debut entrainement à la reconnaissance d'objet, canette/couleur & test materiel
- Estelle: test du matériel et flash des cartes SD des autres raspberry. Deux raspberry (pi3 et pi4) operationnelles.
carte SD de 16G / 64G / 128G prêtes + documentation

Séance 5 du Lundi 11 Janvier 2021 matin :
- Paul : Detection d'objet avec l'internal software du pixy2. Voir pour l'utlisation des coordonnées des box et installation des dependances pour rasberry. https://docs.pixycam.com/wiki/doku.php?id=wiki:v2:hooking_up_pixy_to_a_raspberry_pi
