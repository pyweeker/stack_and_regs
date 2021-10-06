import arcade
import arcade.gui


#---------------------------------------------------------------------------------------  CST

# Screen and colors ----------------------

REG_R_color = (30,110,250)
REG_E_color = (215,90,200)
REG_X_color = (250,180,25)

REG_H_color = arcade.csscolor.YELLOW
REG_L_color = arcade.csscolor.LAWNGREEN

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000


# Regs ------------------------------------------

REG_R_width = 300 #400

REG_height = 50

REG_H_height = REG_E_height = REG_R_height = REG_height

REG_E_width = REG_R_width // 2

REG_L_width = REG_H_width = REG_E_width // 2

REG_TOTAL_WIDTH = REG_R_width + REG_E_width + REG_H_width + REG_L_width


REG_R_x = 250
REG_R_y = 800

REG_L_y = REG_H_y = REG_E_y = REG_R_y

Regs_y_decal = 10
Regs_x_decal = 20

# REG_R_color , REG_E_color

ANGLE_TL = tuple((REG_R_x, REG_R_y))
ANGLE_X_REG = REG_R_x
ANGLE_Y_REG = REG_R_y

STACK_WIDTH = 100
STACK_HEIGHT = 700

Y_INTERLINE = 70

DECAL_Y_CARTOUCHE_REG = 55


DECAL_X_REG_names = -50



#X_DECALS = [0, REG_R_width,  REG_R_width + REG_E_width - 6 * Regs_x_decal,REG_R_width + REG_E_width + REG_H_width - 6 * Regs_x_decal]
X_DECALS = [0, REG_R_width- 4 * Regs_x_decal,  REG_R_width + REG_E_width - 6 * Regs_x_decal, REG_R_width + REG_E_width + REG_H_width - 6 * Regs_x_decal]

X_WIDTH = [REG_R_width, REG_E_width, REG_H_width, REG_L_width]

REGlist = ['A','B','C','D','BP','SP','SI','DI','IP']
archis = ['R','E','H','L']

LINES = len(REGlist)
COLUMNS = len(archis)


# Stacks -------

DECAL_X_STACK = 50

ANGLE_Y_STACK = ANGLE_Y_REG

#ANGLE_STACK = tuple((ANGLE_X_REG + REG_TOTAL_WIDTH + DECAL_X_STACK, ANGLE_Y_REG))
ANGLE_STACK = tuple((ANGLE_X_REG + REG_TOTAL_WIDTH , ANGLE_Y_STACK-200))

ANGLE_LOW = tuple((ANGLE_STACK[0],ANGLE_STACK[1]+30))
ANGLE_HIGH = tuple((ANGLE_STACK[0],ANGLE_STACK[1]-30-STACK_HEIGHT)) # ?

DECAL_X_RAM = 400
ANGLE_RAM = tuple((ANGLE_LOW[0]+ 300, ANGLE_LOW[1] -100))

RAM_WIDTH = 300
RAM_HEIGHT = 700


#---------------------------------------------------------------------------------------



class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "GUI Widgets Example", resizable=True)

        

        # Set background color
        #arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        arcade.set_background_color(arcade.color.MAROON)

        

        

    def on_draw(self):
        arcade.start_render()
        

        

        

        for i in range(0,LINES):
            for j in range(0,COLUMNS):

                

                arcade.draw_rectangle_filled(ANGLE_X_REG+X_DECALS[j] , ANGLE_Y_REG -i*Y_INTERLINE,  X_WIDTH[j], REG_height, arcade.color.GOLD)


        for i in range(0,LINES):
            arcade.draw_text(REGlist[i],REG_R_x + DECAL_X_REG_names - REG_E_width, ANGLE_Y_REG -i*Y_INTERLINE,arcade.csscolor.WHITE,18,)







        # -------------------------------------------------------------------------------------- REGs


        arcade.draw_rectangle_filled(REG_R_x, REG_R_y+DECAL_Y_CARTOUCHE_REG,  REG_R_width, REG_R_height, arcade.color.BLUE) # R
        arcade.draw_rectangle_filled(REG_R_x + REG_R_width - 4 * Regs_x_decal, REG_E_y+DECAL_Y_CARTOUCHE_REG,  REG_E_width, REG_E_height, arcade.color.RED) # E
        arcade.draw_rectangle_filled(REG_R_x + REG_R_width + REG_E_width - 6 * Regs_x_decal, REG_H_y+DECAL_Y_CARTOUCHE_REG,  REG_H_width, REG_H_height, arcade.color.ORANGE) # H
        arcade.draw_rectangle_filled(REG_R_x + REG_R_width + REG_E_width + REG_H_width - 6 * Regs_x_decal, REG_H_y+DECAL_Y_CARTOUCHE_REG,  REG_H_width, REG_H_height, arcade.color.GREEN) # L




        #arcade.draw_rectangle_filled(REG_R_x, REG_R_y,  REG_R_width, REG_R_width, arcade.color.GREEN)

        #arcade.draw_rectangle_filled(REG_R_x, REG_R_y,  REG_R_width, REG_R_width, arcade.color.GREEN)

        #arcade.draw_rectangle_filled(820, 900, 15, 15, arcade.color.RED, 45)


        arcade.draw_text('R',REG_R_x, REG_R_y+DECAL_Y_CARTOUCHE_REG,arcade.csscolor.WHITE,18,)
        arcade.draw_text('E',REG_R_x + REG_R_width - 4 * Regs_x_decal, REG_E_y+DECAL_Y_CARTOUCHE_REG,arcade.csscolor.WHITE,18,)
        arcade.draw_text('H',REG_R_x + REG_R_width + REG_E_width - 6 * Regs_x_decal, REG_H_y+DECAL_Y_CARTOUCHE_REG,arcade.csscolor.WHITE,18,)
        arcade.draw_text('L',REG_R_x + REG_R_width + REG_E_width + REG_H_width - 6 * Regs_x_decal, REG_H_y+DECAL_Y_CARTOUCHE_REG,arcade.csscolor.WHITE,18,)
        arcade.draw_text('X',10,10,arcade.csscolor.WHITE,18,)


        arcade.draw_rectangle_filled(ANGLE_STACK[0] , ANGLE_STACK[1],  STACK_WIDTH, STACK_HEIGHT, arcade.color.BLACK)
        arcade.draw_rectangle_outline(ANGLE_STACK[0] , ANGLE_STACK[1],  STACK_WIDTH, STACK_HEIGHT, arcade.color.RED)

        

        arcade.draw_text("LOW 0x00", ANGLE_LOW[0]-DECAL_X_STACK, ANGLE_LOW[1] + 350, arcade.csscolor.BLACK, 18,)
        arcade.draw_text("HIGH 0xFF", ANGLE_LOW[0]-DECAL_X_STACK, ANGLE_LOW[1] -400,arcade.csscolor.BLACK,18,)


        arcade.draw_text("RAM Adresses and values", ANGLE_RAM[0] -150, ANGLE_LOW[1] + 350, arcade.color.CADET, 18,)        
        arcade.draw_rectangle_filled(ANGLE_RAM[0] , ANGLE_RAM[1],  RAM_WIDTH, RAM_HEIGHT, arcade.color.CADET)

        #arcade.draw_text("HIGH 0xFF", ANGLE_HIGH[0],ANGLE_HIGH[1] -300,arcade.csscolor.WHITE,18,)

        # --------------------------------------------------------------------------------------


window = MyWindow()
arcade.run()



