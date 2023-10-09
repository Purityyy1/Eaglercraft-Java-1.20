from tkinter import *
from time import sleep


root = Tk()
root.title('Eaglercraft 1.20')
root.geometry('800x600')

def extract_png_asset(asset_name):
    return PhotoImage('assets/' + asset_name + '.png')

panorama_photo = extract_png_asset('panorama')
titlescreen_top_photo = extract_png_asset('titlescreen_top')
dirt_bg_photo = extract_png_asset('dirt_bg')
download_terrian_photo = extract_png_asset('download_terrain')
original_server_photo = extract_png_asset('original_server')
panorama_photo = extract_png_asset('panorama')
timed_out_photo = extract_png_asset('times_out')
back_2_titlescreen_photo = extract_png_asset('buttons/back_2_titlescreen')
cancel_photo = extract_png_asset('buttons/cancel')
done_photo = extract_png_asset('buttons/done')
multiplayer_photo = extract_png_asset('buttons/multiplayer')
new_world_photo = extract_png_asset('buttons/new_world')
options_photo = extract_png_asset('buttons/options')
realms_photo = extract_png_asset('buttons/realms')
singleplayer_photo = extract_png_asset('buttons/singleplayer')
root.after(2000)







root.mainloop()
