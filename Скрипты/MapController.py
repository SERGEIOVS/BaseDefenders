import pygame as pg
islands_list = []

islands_x_filename ='txt/coords/islands/islands_x.txt'
islands_y_filename ='txt/coords/islands/islands_y.txt'

islands_x_filemode = 'r'
islands_y_filemode = 'r'

islands_x_file = open (islands_x_filename , islands_y_filemode)
islands_x_file1 = islands_x_file.readlines()

islands_y_file = open (islands_y_filename , islands_y_filemode)
islands_y_file1 = islands_y_file.readlines()

Island_types = ['Continent','Continent']

Island_images = [

pg.image.load( 'задний фон/локации/background_1.png' ),

pg.image.load( 'задний фон/локации/background.png' )        ]

class Background :
    def __init__( self, x , y , width , height ,type ,  image ) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type
        self.image = image

for i in range( len ( islands_x_file1) ) :
    i = Background( islands_x_file1[i] ,islands_y_file1[i] , 5 , 5 ,Island_types[i], Island_images[i] ) 
    islands_list.append( i )
   