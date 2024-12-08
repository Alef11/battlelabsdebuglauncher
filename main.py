import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


games = ["Paladins", "Fortnite", "Usw"]

dpg.create_context()



with dpg.window(label="GameManager", width = 1280, height=720, no_resize=True, no_move=True, menubar=False, no_title_bar=True):

    with dpg.table(tag = "table", header_row=True, width = 1200, resizable=False, policy=dpg.mvTable_SizingStretchProp,
                   borders_outerH=True, borders_innerV=True, borders_outerV=True):

        dpg.add_table_column(label="Game")
        dpg.add_table_column(label="Version")
        dpg.add_table_column(label="Start")
        
        for game in games:
            with dpg.table_row():
                dpg.add_text(game)
                dpg.add_text("bbb")
                dpg.add_text("ccc")

                
demo.show_demo()

dpg.create_viewport(title='BattleLabs Debug Launcher', width=1280, height=720)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()