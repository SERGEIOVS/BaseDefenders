from settings import *

class interface :
    def __init__( self, x , y , width , height , image ) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

cells_num = 10

beltinventorycell = interface( int(screen_width) / 2 -cells_num * 50 / 2 , int(screen_height) - 50 , 50 , 50 , pg.image.load( 'интерфейс/иконки/inventory_cell.png' ) )

backpackinventorycell = interface( 710 , 300 , 50 , 50 , pg.image.load( 'интерфейс/иконки/inventory_cell.png' ) )

currentinventorycell = interface( int(screen_width) / 2 -cells_num * 25 , beltinventorycell.y , 50 , 50 , pg.image.load( 'интерфейс/иконки/current_inventory_cell.png' ) )

achievements_menu = interface( 2000 , 100 , 300 , 500 , pg.image.load( 'интерфейс/иконки/achievements_menu.png' ) )

minimap_menu = interface(2000 , 0 , 1500 , 1000 , pg.image.load( 'интерфейс/иконки/mini_map1.png' ) )

cursor_icon = interface( 0 , 0 , 10 , 10 , pg.image.load( 'интерфейс/иконки/crosshair.png' ) )

clock_icon = interface( 900 , 0 , 30 , 30 , pg.image.load( 'интерфейс/иконки/clock_icon.png' ) )

achievements_icon = interface( 3000 , 125 , 30 , 30 , pg.image.load( 'интерфейс/иконки/achievements_icon.png' ) )

health_icon = interface( 0 , int(screen_height) - 50 , 25 , 25 , pg.image.load( 'интерфейс/иконки/health_icon.png' ) )

armor_icon = interface( 0 , int(screen_height) - 25 , 25 , 25 , pg.image.load( 'интерфейс/иконки/armor_icon.png' ) )

current_ammo_icon = interface(0 , int(screen_height) - 75 , 34 , 50 , pg.image.load( 'интерфейс/иконки/pistol_ammo_icon.png' ) )

button = interface(2100,210,200,50,pg.image.load( 'интерфейс/иконки/button.png' ) )

MusicIcon = interface(0,100,30,30,pg.image.load( 'интерфейс/иконки/MusicIcon.png' ) )

craft_icon = interface(2100,125,20,30,pg.image.load( 'интерфейс/иконки/craft_icon.png' ) )

energy_icon = interface( 200 , beltinventorycell.y , 11 , 26 , pg.image.load( 'интерфейс/иконки/energy_icon.png' ) )

left_pointer = interface( achievements_menu.x + 50 , achievements_menu.y + 100 ,20 , 20 , pg.image.load( 'интерфейс/иконки/pointer_left.png' ) )

right_pointer = interface(achievements_menu.x + 200 , achievements_menu.y + 100 , 20 , 20 , pg.image.load( 'интерфейс/иконки/pointer_right.png' ) )

cancel_icon = interface( minimap_menu.x , minimap_menu.y + 25 , 20 , 20 , pg.image.load( 'интерфейс/иконки/cancel_icon.png' ) )

cancel_icon1 = interface( achievements_menu.x + achievements_menu.width - 20 , minimap_menu.y + 25 , 20 , 20 , pg.image.load( 'интерфейс/иконки/cancel_icon.png' ) )

minimap_icon = interface( int(screen_width) - 710 , 1030 , 50 , 50 , pg.image.load( 'интерфейс/иконки/minimap_icon.png' ) )