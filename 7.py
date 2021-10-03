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
        REG_R_height = 50

        REG_H_height = REG_E_height = REG_R_height

        REG_E_width = REG_R_width // 2

        REG_H_width = REG_E_width // 2

        REG_R_x = 300
        REG_R_y = 900

        REG_L_y = REG_H_y = REG_E_y = REG_R_y

        Regs_y_decal = 10
        Regs_x_decal = 20

        # REG_R_color , REG_E_color





        # -------------------------------------------------------------------------------------- REGs

        #arcade.draw_rectangle_filled(200, SCREEN_HEIGHT - 500 , 200+REG_R_width, SCREEN_HEIGHT - 600, arcade.color.BLUSH)

        arcade.draw_rectangle_filled(REG_R_x, REG_R_y,  REG_R_width, REG_R_height, arcade.color.BLUE) # R


        #arcade.draw_rectangle_filled(REG_R_x + REG_R_width, REG_E_y,  REG_E_width, REG_E_height, arcade.color.RED) # E
        arcade.draw_rectangle_filled(REG_R_x + REG_R_width - 4 * Regs_x_decal, REG_E_y,  REG_E_width, REG_E_height, arcade.color.RED) # E

        arcade.draw_rectangle_filled(REG_R_x + REG_R_width + REG_E_width - 6 * Regs_x_decal, REG_H_y,  REG_H_width, REG_H_height, arcade.color.ORANGE) # H

        arcade.draw_rectangle_filled(REG_R_x + REG_R_width + REG_E_width + REG_H_width - 6 * Regs_x_decal, REG_H_y,  REG_H_width, REG_H_height, arcade.color.GREEN) # L




        #arcade.draw_rectangle_filled(REG_R_x, REG_R_y,  REG_R_width, REG_R_width, arcade.color.GREEN)

        #arcade.draw_rectangle_filled(REG_R_x, REG_R_y,  REG_R_width, REG_R_width, arcade.color.GREEN)

        #arcade.draw_rectangle_filled(820, 900, 15, 15, arcade.color.RED, 45)


        arcade.draw_text('R',REG_R_x, REG_R_y,arcade.csscolor.WHITE,18,)
        arcade.draw_text('E',REG_R_x + REG_R_width - 4 * Regs_x_decal, REG_E_y,arcade.csscolor.WHITE,18,)
        arcade.draw_text('H',REG_R_x + REG_R_width + REG_E_width - 6 * Regs_x_decal, REG_H_y,arcade.csscolor.WHITE,18,)
        arcade.draw_text('L',REG_R_x + REG_R_width + REG_E_width + REG_H_width - 6 * Regs_x_decal, REG_H_y,arcade.csscolor.WHITE,18,)
        arcade.draw_text('X',10,10,arcade.csscolor.WHITE,18,)

        # --------------------------------------------------------------------------------------


window = MyWindow()
arcade.run()

