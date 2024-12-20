import dearpygui.dearpygui as dpg
import os
import git
import glob

aaaa = True

def UpdateRepo():
    if(os.path.isdir('AppRenders')):
        g = git.cmd.Git(os.getcwd() + "\\AppRenders")
        msg = g.pull()
    else:
        git.Git("").clone("https://github.com/Alef11/AppRenders.git")
    UpdateUI()
    

def getGames():
    try:
        g = os.listdir(os.getcwd() + "\\AppRenders")
        for i in g:
            if(i == ".git"):
                g.remove(i)
        return g
    except:
        return []

def getGameVersion(game):
    path = (os.getcwd() + "\\AppRenders\\" + game)
    versionpath = glob.glob(path + "\\version")
    f = open(versionpath[0], "r")
    return f.read() 

def LaunchGame(user_data):
    path = os.listdir(os.getcwd() + "\\AppRenders" + "\\" + user_data)
    for p in path:
        if(p[-4:] == ".exe"):
            if(p[-11:] == "console.exe"):
                path.remove(p)
        else:
            path.remove(p)
    if("version" in path):
        path.remove("version")

    os.system(os.getcwd() + "\\AppRenders" + "\\" + user_data + "\\" + path[0])

def UpdateUI():
    global aaaa
    aaaa = True
    dpg.stop_dearpygui()


def main():
    global aaaa
    aaaa = False

    games = getGames()

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
                    dpg.add_text(getGameVersion(game))
                    dpg.add_button(label="Launch", callback=LaunchGame, tag=game)

        dpg.add_button(label="Reload", callback=UpdateRepo)

                    
    dpg.create_viewport(title='BattleLabs Debug Launcher', width=1280, height=720)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


while aaaa:
    main()