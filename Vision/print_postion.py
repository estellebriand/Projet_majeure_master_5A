from __future__ import print_function
import pixy 
from ctypes import *
from pixy import *
from math import *


pixy.init ()
pixy.change_prog ("color_connected_components")

class Blocks (Structure):
  _fields_ = [ ("m_signature", c_uint),
    ("m_x", c_uint),
    ("m_y", c_uint),
    ("m_width", c_uint),
    ("m_height", c_uint),
    ("m_angle", c_uint),
    ("m_index", c_uint),
    ("m_age", c_uint) ]

blocks = BlockArray(100)
frame = 0
posz = []
fov=60 #75?
taille_objet_reel=20
taille_objet_image=10
tab_ret=[]
#x -> 0-315
#y -> 0-207

while 1:
  count = pixy.ccc_get_blocks (100, blocks)

  if count > 0:
    print('frame %3d:' % (frame))
    frame = frame + 1
    for index in range (0, count):
        print('[BLOCK: SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks[index].m_signature, blocks[index].m_x, blocks[index].m_y, blocks[index].m_width, blocks[index].m_height))
    # z = opposé/tangente(fov/2)
    #if blocks[index].m_x < 315/2
    #    posz[index] = 
    #if blocks[index].m_x > 315/2
    #    posz[index] = 

        #On utilise  la taille reelle de l'objet pour calculer la distance à l'objet
        taille_objet_image = blocks[index].m_height
        posz[index] = (taille_objet_reel*0.68)/taille_objet_image
        #calcul fov pour distance x reel grace à un peu de trigonometrie 
        taille_fov_reel = 2*posz[index]*math.tan(fov/2)
        posx[index] =(1/315)*blocks[index].m_x*taille_fov_reel
        #On enrengistre les valeurs x,y,z pour chaque box
        position = [posx[index],blocks[index].m_y,posz[index]]
        #attention la valeur de la position en y sera surement fausse mais pas utile dans notre cas
        print(posz[index])
        print(posx[index])
        tab_ret[index] = position


return[tab_ret]