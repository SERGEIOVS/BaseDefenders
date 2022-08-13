#system/python modules
import pygame as pg , datetime , time , random , math , sys , pyautogui , pickle ; from PIL import Image ; import os ; import logging ; from cv2 import log

#my custom  files
from settings import * ; from MapController import * ; from BuildingsManager import * ; from UnitManager import * ; from Items import * ; from traps import * ;
from SpawnFile import * ; from interface import * ; from VihiclesManager import * ; from PathManager import *

logfilepath = 'logs/log.txt'

logfilestatus = logging.INFO
logfileformat = ' %(asctime)s - %(levelname)s - %(message)s '

logging.basicConfig(filename =  logfilepath , level = logfilestatus , format = logfileformat)

#отключить протоколирование - logging.disable()

pg.init()

pg.font.init()

pos = pg.mouse.get_pos()
game_status_list = ['main_menu','play']
game_status = game_status_list[0]
bg_image = pg.image.load( 'интерфейс/иконки/mini_map.png' )

def make_screenshot() :
    screenshot = pyautogui.screenshot()
    screenshot.save( 'скриншоты/screenshot' + '.png' )

def start():
    if game_status == 'main_menu':

        mouse_visible = True
        mouse_set_visible = pg.mouse.set_visible( mouse_visible )

        screen.blit(  bg_image, ( 0 ,0 ) )
        screen.blit( button.image , ( 800 / 2  - button.width / 2  ,120 ) )
        screen.blit( button.image , ( 800 / 2  - button.width / 2 ,180 ) )
        screen.blit( button.image , (  800 / 2  - button.width / 2,250 ) )
        screen.blit( button.image , ( 800 / 2  - button.width / 2 ,310 ) )

    if game_status == 'play':

        mouse_visible = False
        mouse_set_visible = pg.mouse.set_visible( mouse_visible )

        for i in range( len ( islands_x_file1 ) ) :
            screen.blit( Island_images[i] ,   ( -camera.rect[ 0 ] + int(islands_x_file1[i])  , -camera.rect[ 1 ] + int(islands_y_file1[i]) ) )

        for i in range( len ( vihicles_x_file1 ) ) :
            screen.blit( vihicles_images_list[ i ] , ( -camera.rect[ 0 ] + int(vihicles_x_file1[ i ]) , -camera.rect[ 1 ] + int(vihicles_y_file1[ i ]) ) ) 

        for i in range( len ( buildings_x_file1 ) ) :
            screen.blit( buildings_images_list[ i ] , ( -camera.rect[ 0 ] + int(buildings_x_file1[ i ]) , -camera.rect[ 1 ] + int(buildings_y_file1[ i ] ) )) 

        #for i in range( len ( f_creatures_x_file1 ) ) :
        # screen.blit( friendly_creatures_images_list[i] , ( -camera.rect[ 0 ] + int(f_creatures_x_file1[ i ] ) , -camera.rect[ 1 ] + int(f_creatures_y_file1[ i ] ) ) )   

        for i in range( len ( enemies_x_file1 ) ) :
                if int(enemies_x_file1[ i ])  >= camera.rect[0]  and int(enemies_x_file1[ i ]) <= camera.rect[0] + int(screen_width)  and \
                int(enemies_y_file1[ i ])  >= camera.rect[1]  and int(enemies_y_file1[ i ]) <= camera.rect[1] + int(screen_height) :
                    screen.blit( enemies_images_list[ i ] , ( -camera.rect[ 0 ] + int(enemies_x_file1[ i ]) , -camera.rect[ 1 ] + int(enemies_y_file1[ i ] ) ) )
  
        #for i in range( len ( furniture ) ) :
            #screen.blit( furniture_images_list[ i ] , ( -camera.rect[ 0 ] + furniture_x_list  [ i ]  , -camera.rect[ 1 ] + furniture_y_list[ i ] ) ) 

        for i in range(len(items_x_file1 ) ) :
            screen.blit(items_images_list[ i ] , ( -camera.rect[ 0 ] + int(items_x_file1[ i ]) , -camera.rect[ 1 ] + int(items_y_file1[ i ] ) ) ) 

        for i in range( len ( traps_x_file1 ) ) :
            screen.blit( traps_images_list[i] , ( -camera.rect[ 0 ] + int(traps_x_file1[ i ] ) , -camera.rect[ 1 ] + int(traps_x_file1[ i ] )  ) )  

        for i in range( len ( hero_belt_inventory_cells_x_list ) ) : 
            screen.blit ( hero_belt_inventory_cells_images[ i ] , ( hero_belt_inventory_cells_x_list[ i ] ,  hero_belt_inventory_cells_y_list[ i ] ) )

        for i in range( len ( hero_belt_inventory_items_x_list ) ) :
            screen.blit ( hero_belt_inventory_images[ i ] , ( hero_belt_inventory_items_x_list[ i ] ,  hero_belt_inventory_items_y_list[ i ] ) )

        for i in range( len ( hero_backpack_inventory_cells_x_list ) ) :
            screen.blit ( hero_backpack_inventory_cells_images[ i ] , ( hero_backpack_inventory_cells_x_list[ i ] ,  hero_backpack_inventory_cells_y_list[ i ] ) )

        for i in range( len( hero_backpack_inventory_items_x_list ) ) :
            screen.blit ( hero_backpack_inventory_images[ i ] , ( hero_backpack_inventory_items_x_list[ i ] ,  hero_backpack_inventory_items_y_list[ i ] ) )

        screen.blit( achievements_menu.image , ( achievements_menu.x , achievements_menu.y ) )

        screen.blit( armor_icon.image , ( armor_icon.x , armor_icon.y ) )

        screen.blit( show_hero_armor , (armor_icon.x + armor_icon.width, armor_icon.y ) )

        screen.blit( health_icon.image , (health_icon.x, health_icon.y ) )

        screen.blit( show_health , ( health_icon.x + health_icon.width , beltinventorycell.y ) )

        screen.blit( current_ammo_icon.image , (current_ammo_icon.x , current_ammo_icon.y ) )

        screen.blit( current_ammo_counter , ( current_ammo_icon.x + current_ammo_icon.width , current_ammo_icon.y ) )

        screen.blit( hero_image , ( hero_x , hero_y ) )

herojump , herojumpcounter = False , 10 # запрет на прыжок , высота прыжка

run = True

logging.info(msg='GAME STARTED!')

while run :
    vector = [ 0 , 0 ]
    for event in pg.event.get() :
        if event.type == pg.MOUSEMOTION :
            pos = pg.mouse.get_pos()

            if game_status == 'play':
                mouse_visible = TRUE
                screen.blit( cursor_icon.image , ( pos[ 0 ] , pos[ 1 ] ) )

            pg.display.update()

            """            if pos[ 0 ] > str(screen_width /2):
                hero_image = pg.image.load( 'персонажи/герой/hero_run_right_1.png' )

            if pos[ 0 ] < str(screen_width /2):
                hero_image = pg.image.load( 'персонажи/герой/hero_run_left_1.png' )"""

            pressed = pg.mouse.get_pressed()
            pos = pg.mouse.get_pos()

            if pressed[ 0 ] and currentinventorycell.x == beltinventorycell.x + beltinventorycell.width * 4 :
                current_ammo -= 1
                current_ammo_counter = big_font.render( str( current_ammo ) + "/" + str( max_current_ammo ) , False , ( 250 , 0, 0 ) ) 
                click_sound = pg.mixer.Sound( 'Звуки/pistol_shot.wav' )
                click_sound.play()
            if pressed[1]:
                game_status_list.reverse()
                game_status = game_status_list[0]

                if pressed[ 0 ]  and pos[ 0 ] > enemies_list[0] :
                    enemies_images_list[0] = pg.image.load( 'персонажи/герой/hero_shoot_right+pistol.png' ) 

                if pressed[ 0 ] and pos[ 0 ] < enemies_list[0] :
                    enemies_images_list[0] = pg.image.load( 'персонажи/герой/hero_shoot_left+pistol.png' )

        if event.type == pg.MOUSEBUTTONDOWN :
            if event.button == 1 and current_ammo > 0 and game_status == 'play':
                current_ammo -= 1
                current_ammo_counter = big_font.render( str( current_ammo ) + "/" + str( max_current_ammo ) , False , ( 250 , 0 , 0 ) )
                gun_shot = pg.mixer.Sound( 'Звуки/pistol_shot.wav' )
                gun_shot.play()

            if pos[ 0 ] >= button.x and pos[ 0 ] <= button.x + button.width and pos[1] >= button.y and pos[1] <= button.y + button.height :
                pg.mixer.music.play()
            
            if event.button == 1 and current_ammo <= 0 and game_status == 'play':
                current_ammo = 0
                current_ammo_counter = big_font.render( str( current_ammo ) + "/" + str( max_current_ammo ) , False , ( 255 , 0 , 0 ) ) 
                no_ammo = pg.mixer.Sound( 'Звуки/no_ammo.wav' )
                no_ammo.play()

            if event.button == 1 and pos[ 0 ] >= hero_x and game_status == 'play':
                hero_image = pg.image.load( 'персонажи/герой/hero_shoot_right+pistol.png' )

            if event.button == 1 and pos[ 0 ] <= hero_x  and game_status == 'play':
                hero_image = pg.image.load( 'персонажи/герой/hero_shoot_left+pistol.png' )

            for i in range( len ( enemies_x_file1 ) ) :
                if event.button == 1 and int(enemies_x_file1[ i ])  >= camera.rect[0]  and int(enemies_x_file1[ i ]) <=camera.rect[0] + screen_width  and \
                int(enemies_x_file1[ i ])  >= camera.rect[0]  and int(enemies_x_file1[ i ]) <=camera.rect[0] + screen_width :
                    print(int(i),':','В зоне видимости камеры!')

        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    if keys[pg.K_a] and game_status == 'play':
        vector[ 0 ] -= hero_speed
        hero_image = pg.image.load( 'персонажи/герой/hero_run_left.png' )

    if keys[pg.K_a] and keys[pg.K_LSHIFT] and game_status == 'play':
        vector[ 0 ] -= hero_speed
        hero_image = pg.image.load( 'персонажи/герой/hero_run_left.png' )

    if keys[pg.K_w] and keys[pg.K_LSHIFT] and game_status == 'play':
        vector[ 1 ] -= hero_speed

    if keys[pg.K_s] and keys[pg.K_LSHIFT] and game_status == 'play':
        vector[ 1 ] += hero_speed

    if keys[pg.K_d] and game_status == 'play':
        vector[ 0 ] += hero_speed
        hero_image = pg.image.load( 'персонажи/герой/hero_run_right.png' )

    if keys[pg.K_d] and keys[pg.K_LSHIFT] and game_status == 'play':
        vector[ 0 ] += hero_speed
        hero_image = pg.image.load( 'персонажи/герой/hero_run_right.png' )

    if not( herojump ) :

        if keys[pg.K_w] and game_status == 'play':
            vector[ 1 ] -= hero_speed
  
        if keys[pg.K_s] and game_status == 'play':
            vector[ 1 ] += hero_speed

        if keys[pg.K_SPACE] and game_status == 'play':
            herojump = True #можно прыгать

        ##  Если игрок ходил
        if vector != [ 0 , 0 ] and game_status == 'play':
            camera.move( vector )

    else:
        if herojumpcounter >= -10 :
            if herojumpcounter < 0 :
                hero_y += ( herojumpcounter ** 2 ) / 2

            else:
                hero_y-= ( herojumpcounter ** 2 ) / 2
            herojumpcounter -=1

        else:
            herojump = False
            herojumpcounter = 10
    
    if keys [pg.K_r]and game_status == 'play':
        reload = pg.mixer.Sound( 'Звуки/reload.wav' )
        reload.play()
        current_ammo = 10
        current_ammo_counter = big_font.render( str( current_ammo ) + "/" + str( max_current_ammo ) , False , ( 250 , 0 , 0 ) )

    if keys [pg.K_F5] :
        make_screenshot()
        logging.info(msg='SCREENSHOT SAVED!')

    if keys [pg.K_F12] :

        camerafilemode = 'w'
        camera_file = open (camera_filename , camerafilemode)
        camera_file.write( str(camera.rect[0])+':'+str(camera.rect[1])  )
        camera_file.close()
        logging.info(msg='GAME SAVED!')
        pg.quit()
        logging.info(msg='QUIT GAME!')
        
    if keys [pg.K_c] :
        achievements_menu.x = screen_width = ( 1920 / 2 ) - ( achievements_menu.width / 2 )

    if keys [pg.K_v] :
        achievements_menu.x = 2000

    if keys [pg.K_b] :
            button.x = screen_width / 2 - button.width / 2

    if keys [pg.K_n] :
            button.x = 3000
    
    if keys [pg.K_1] :
            game_status = 'play'
    
    if keys [pg.K_2] :
            game_status = 'main_menu'

    screen.fill( BGcolor )

    start()

    pg.display.update()