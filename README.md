# Projet de majeure "Robotique de service"
s5_g7_briand_guy_kahan_martinez

**Auteurs:** Estelle BRIAND_Nicolas GUY_Jeremie KAHAN_Paul MARTINEZ
Démarrage

Essai commit Nico
Essai commit Paul

# Cahier des charges

Creer un environement de simulaiton et une raspberry_pi qui sera connectée au robot réel et ses capteurs afin de pouvoir plannifier son parcours, les étapes à suivre et effectuer des tâches définies.

## Contraintes

- raspberry_pi 3 B
- Connection au PC une fois en début d'épreuve
- Vehicule doit être autonome
- Connection avec une arduino, capteurs et camera
- Doit être capable de reconnaitre des points d'interets.

## Technologies utilisées:

- ROS (sur rapsberry pi)
    - rosserial --> arduino sur robot
    - dynamixel_motor --> controller moteur en position
    - rplidar_ros --> gestion du Lidar
    - slam (simultaneous localization and mapping) --> gestion de la map 
- Matlab (sur PC)
    - ROS toolboxes
    - IHM
    - calcul des trajectoires
- Darknet (sur rapsberry pi)
    - reconnaissance cannettes
    - reconnaissance couleur
- Capteurs : Lidar

### Exemple de planning type
![Image planning prévu](https://gitlab.com/20-21_5ETI_PRJ/Sujet_5__Simulated_robotic_scenario/s5_g7_briand_guy_kahan_martinez/-/raw/master/autre/Planning-Pr%C3%A9vu.PNG)

### ACHATS SUPPLEMENTAIRES NECESSAIRES A LA BONNE CONDUITE DU PROJET RESPECTIVE A CHACUN(E)
=> Jérémie donne à Paul un raspberry Pi avec la caméra associée
=> Nicolas apporte sa malette d'électronique pour savoir si des composants peuvent servir

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
