from tkinter import *
from time import sleep


root = Tk()
root.title('Eaglercraft 1.20')
root.geometry('800x600')

def extract_png_asset(asset_name):
    return PhotoImage(file='assets/' + asset_name + '.png')


a_normal_black_photo = extract_png_asset('font/normal-black/a')
b_normal_black_photo = extract_png_asset('font/normal-black/b')
c_normal_black_photo = extract_png_asset('font/normal-black/c')
d_normal_black_photo = extract_png_asset('font/normal-black/d')
e_normal_black_photo = extract_png_asset('font/normal-black/e')
f_normal_black_photo = extract_png_asset('font/normal-black/f')
g_normal_black_photo = extract_png_asset('font/normal-black/g')
h_normal_black_photo = extract_png_asset('font/normal-black/h')
i_normal_black_photo = extract_png_asset('font/normal-black/i')
j_normal_black_photo = extract_png_asset('font/normal-black/j')
k_normal_black_photo = extract_png_asset('font/normal-black/k')
l_normal_black_photo = extract_png_asset('font/normal-black/l')
m_normal_black_photo = extract_png_asset('font/normal-black/m')
n_normal_black_photo = extract_png_asset('font/normal-black/n')
o_normal_black_photo = extract_png_asset('font/normal-black/o')
p_normal_black_photo = extract_png_asset('font/normal-black/p')
q_normal_black_photo = extract_png_asset('font/normal-black/q')
r_normal_black_photo = extract_png_asset('font/normal-black/r')
s_normal_black_photo = extract_png_asset('font/normal-black/s')
t_normal_black_photo = extract_png_asset('font/normal-black/t')
u_normal_black_photo = extract_png_asset('font/normal-black/u')
v_normal_black_photo = extract_png_asset('font/normal-black/v')
w_normal_black_photo = extract_png_asset('font/normal-black/w')
x_normal_black_photo = extract_png_asset('font/normal-black/x')
y_normal_black_photo = extract_png_asset('font/normal-black/y')
z_normal_black_photo = extract_png_asset('font/normal-black/z')
titlescreen_top_photo = extract_png_asset('titlescreen_top')
dirt_bg_photo = extract_png_asset('dirt_bg')
download_terrian_photo = extract_png_asset('download_terrain')
original_server_photo = extract_png_asset('original_server')
titlescreen_bg_photo = extract_png_asset('titlescreen_bg')
timed_out_photo = extract_png_asset('timed_out')
back_2_titlescreen_photo = extract_png_asset('buttons/back_2_titlescreen')
cancel_photo = extract_png_asset('buttons/cancel')
done_photo = extract_png_asset('buttons/done')
multiplayer_photo = extract_png_asset('buttons/multiplayer')
new_world_photo = extract_png_asset('buttons/new_world')
options_photo = extract_png_asset('buttons/options')
realms_photo = extract_png_asset('buttons/realms')
singleplayer_photo = extract_png_asset('buttons/singleplayer')
screenname_photo = extract_png_asset('screenname')
edit_profile_photo = extract_png_asset('edit_profile')
player_skin_photo = extract_png_asset('player_skin')


dirt_bg = Label(image=dirt_bg_photo)
dirt_bg.pack()





root.mainloop()
