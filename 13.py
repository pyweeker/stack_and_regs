import arcade
import arcade.gui

REG_R_color = (30,110,250)
REG_E_color = (215,90,200)
REG_X_color = (250,180,25)

REG_H_color = arcade.csscolor.YELLOW
REG_L_color = arcade.csscolor.LAWNGREEN

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000

class MyWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "GUI Widgets Example", resizable=True)

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="This is a Text Widget",
                                              width=450,
                                              height=40,
                                              font_size=24,
                                              font_name="Kenney Future")
        self.v_box.add(ui_text_label.with_space_around(bottom=0))

        text="The real danger is not that computers will begin to think like people, but that people will begin " \
             "to think like computers. - Sydney Harris (Journalist)"
        ui_text_label = arcade.gui.UITextArea(text=text,
                                              width=450,
                                              height=60,
                                              font_size=12,
                                              font_name="Arial")
        self.v_box.add(ui_text_label.with_space_around(bottom=0))

        # Create a UIFlatButton
        ui_flatbutton = arcade.gui.UIFlatButton(text="Flat Button", width=200)
        self.v_box.add(ui_flatbutton.with_space_around(bottom=20))

        # Handle Clicks
        @ui_flatbutton.event("on_click")
        def on_click_flatbutton(event):
            print("UIFlatButton pressed", event)

        # Create a UITextureButton
        texture = arcade.load_texture(":resources:onscreen_controls/flat_dark/play.png")
        ui_texture_button = arcade.gui.UITextureButton(texture=texture)

        # Handle Clicks
        @ui_texture_button.event("on_click")
        def on_click_texture_button(event):
            print("UITextureButton pressed", event)

        self.v_box.add(ui_texture_button.with_space_around(bottom=20))
        
        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )


    def on_click_start(self, event):
        print("Start:", event)

    def on_draw(self):
        arcade.start_render()
        self.manager.draw()

        #  SCREEN_HEIGHT

        #  SCREEN_WIDTH

        REG_R_width = 400

        REG_height = 50

        REG_H_height = REG_E_height = REG_R_height = REG_height

        REG_E_width = REG_R_width // 2

        REG_L_width = REG_H_width = REG_E_width // 2

        REG_R_x = 300
        REG_R_y = 900

        REG_L_y = REG_H_y = REG_E_y = REG_R_y

        Regs_y_decal = 10
        Regs_x_decal = 20

        # REG_R_color , REG_E_color

        ANGLE_TL = tuple((REG_R_x, REG_R_y))
        ANGLE_X = REG_R_x
        ANGLE_Y = REG_R_y

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

        for i in range(0,LINES):
            for j in range(0,COLUMNS):

                print(f" i {i}  j {j} ")

                arcade.draw_rectangle_filled(ANGLE_X+X_DECALS[j] , ANGLE_Y -i*Y_INTERLINE,  X_WIDTH[j], REG_height, arcade.color.GOLD)


        for i in range(0,LINES):
            arcade.draw_text(REGlist[i],REG_R_x + DECAL_X_REG_names - REG_E_width, ANGLE_Y -i*Y_INTERLINE,arcade.csscolor.WHITE,18,)







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

        # --------------------------------------------------------------------------------------


window = MyWindow()
arcade.run()

