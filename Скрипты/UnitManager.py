import pygame as pg
from settings import *
from Items import *

hero_x , hero_y = int(screen_width) / 2 , int(screen_height)  / 2 - 150
hero_speed = 3
hero_health , hero_max_health = 10 , 10
hero_armor , hero_max_armor = 10 , 10
hero_anmations = [pg.image.load( 'персонажи/герой/hero_run_left_1.png' ) , pg.image.load( 'персонажи/герой/hero_run_right_1.png' ) ]
hero_image = hero_anmations[0]
current_ammo = 10
max_current_ammo = 50

class Enemies:
    def __init__( self , x , y , image , loot , speed , health ) : 
        self.x = x
        self.y = y    
        self.image = image
        self.loot=loot
        self.speed = speed
        self.health = health

enemies_list = []

x_enemies_filename ='txt/coords/enemies/x_enemies.txt'

y_enemies_filename ='txt/coords/enemies/y_enemies.txt'

enemiesfilemode = 'r'

enemies_x_file = open (x_enemies_filename , enemiesfilemode)

enemies_y_file = open (y_enemies_filename , enemiesfilemode)

enemies_x_file1 = enemies_x_file.readlines()

enemies_y_file1 = enemies_y_file.readlines()

enemies_images_list = [

pg.image.load( 'персонажи/противники/thief_run_right.png' ) ,

pg.image.load( 'персонажи/противники/thief1_run_right.png' ) ,

pg.image.load( 'персонажи/противники/mutant1_run_right.png' ) ,

pg.image.load( 'персонажи/противники/Dogman_run_right.png' ) ,

pg.image.load( 'персонажи/противники/hazamat_unit_run_right.png' ) ,

pg.image.load( 'персонажи/противники/yeti_run_right.png' ) ,

pg.image.load( 'персонажи/противники/beast_run_right.png' ) ,

pg.image.load( 'персонажи/противники/mutant+blades_run_right.png' ) ,

pg.image.load( 'персонажи/противники/maniac_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_run_right.png' ) ,




pg.image.load( 'персонажи/союзники/жители/citizen_1_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_2_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_3_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_4_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_5_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/солдаты/soldier_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/погибшие/deadman_left_empty_hands.png' ) ,

pg.image.load( 'персонажи/союзники/рыба/рыба.png' ) ,

pg.image.load( 'персонажи/союзники/солдаты/MG_man_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/нло/alien_turned_right.png' ) ,


pg.image.load( 'персонажи/союзники/нло/alien+rifle_turned_right.png' ) ,

pg.image.load( 'персонажи/союзники/погибшие/dead_man_turned_left.png' )]

for i in range( len ( enemies_x_file1 ) ) :
    i =Enemies( enemies_x_file1[ i ] , enemies_y_file1[ i ] ,enemies_images_list[ i ] ,items_images_list[i] , 5 , 0 ,  )
    enemies_list.append( i )



"""
class Friendly_creatures:
    def __init__( self , x , y , width , height , image , speed , health ) :
        self.x = x
        self.y = y    
        self.width = width
        self.height = height
        self.image = image
        self.speed = speed
        self.health = health

friendly_creatures_list = []

x_f_creatures_filename ='txt/coords/friendly_creatures/f_creatures_x.txt'

y_f_creatures_filename ='txt/coords/friendly_creatures/f_creatures_y.txt'

f_creaturesfilemode = 'r'

f_creatures_x_file = open (x_f_creatures_filename , f_creaturesfilemode)

f_creatures_y_file = open (y_f_creatures_filename , f_creaturesfilemode)

f_creatures_x_file1 = f_creatures_x_file.readlines()

f_creatures_y_file1 = f_creatures_y_file.readlines()

friendly_creatures_images_list = [

pg.image.load( 'персонажи/союзники/жители/citizen_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_1_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_2_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_3_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_4_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/жители/citizen_5_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/солдаты/soldier_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/погибшие/deadman_left_empty_hands.png' ) ,

pg.image.load( 'персонажи/союзники/рыба/рыба.png' ) ,

pg.image.load( 'персонажи/союзники/солдаты/MG_man_run_right.png' ) ,

pg.image.load( 'персонажи/союзники/нло/alien_turned_right.png' ) ,

pg.image.load( 'персонажи/союзники/нло/alien+rifle_turned_right.png' ) ,

pg.image.load( 'персонажи/союзники/погибшие/dead_man_turned_left.png' )

]

for i in range( len ( f_creatures_x_file1 ) ) :
    i = Friendly_creatures( f_creatures_x_file1[ i ] , f_creatures_y_file1 , 100 , 180 , friendly_creatures_images_list[ i ] , 5 , 5 )
    friendly_creatures_list.append( i )


"""