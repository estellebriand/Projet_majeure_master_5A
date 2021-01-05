# Projet de majeure "Robotique de service"
s5_g7_briand_guy_kahan_martinez

**Auteurs:** Estelle BRIAND_Nicolas GUY_Jeremie KAHAN_Paul MARTINEZ
Démarrage

Essai commit Nico
Essai commit Paul


### Exemple de planning type
![Image planning prévu](https://gitlab.com/20-21_5ETI_PRJ/Sujet_5__Simulated_robotic_scenario/s5_g7_briand_guy_kahan_martinez/-/raw/master/autre/Planning-Pr%C3%A9vu.PNG)

### ACHATS SUPPLEMENTAIRES NECESSAIRES A LA BONNE CONDUITE DU PROJET RESPECTIVE A CHACUN(E)
=> Jérémie donne à Paul un raspberry Pi avec la caméra associée
=> Nicolas apporte sa malette d'électronique pour savoir si des composants peuvent servir

Lundi 04 Janvier 2021 matin :
- Jérémie : documentation IHM Matlab
- Nicolas : Recherche documentation/codes capteurs IR/US + se replonger dans les codes servomoteur dynamixel AX12 du projet proto
- Paul : Documentation et entrainement 
- Estelle: installation ubuntu mate + ROS sur raspberry, verifier le bon foncitonnement

# Branch BRIAND

-> work on the ROS, Integration of communication

## Work in progress:
- [ ] Dynamixel :  dans le workspace ROS /projet_ws  pour le controle du dynamixel en position
- [ ] ROS serial : dans le workspace ROS /projet_ws pour le la liaison serial entre arduino uno et raspberry
- [ ] ROS ethernet :  on veut une connection ethernet entre la raspberry et matlab
- [x] Installation OS: Ubuntu-mate 18.04
- [x] Installation ROS sur Ubuntu-mate : melodic de preference

--> rapsberry pi prête : 3
## How to
- flash_sd_card --> raspberry_pi/flash_sd_card.md
## Researchs and links

https://yoraish.com/2020/01/23/a-full-autonomous-stack-a-tutorial-ros-raspberry-pi-arduino-slam/

http://di.univ-blida.dz:8080/jspui/bitstream/123456789/2889/1/R%C3%A9alisation%20d%E2%80%99un%20Robot%20mobile%20avec%20%C3%A9vitement%20d%E2%80%99obstacle%20et%20atteinte%20un%20objectif%20fix%C3%A9.pdf

tuto ubuntu + ros: https://medium.com/@rishabhdevyadav/install-ubuntu-mate-18-04-and-ros-on-raspberry-pi-3-b-7ff84688fa37
