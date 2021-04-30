import numpy as np
from dearpygui.core import *
from dearpygui.simple import *
from dearpygui.demo import show_demo

"""
by @Hg & @Pdxr
"""

h = 256

M = np.array([
    180,167,154,141,129,116,103,90,
    10000,10000,77,64,51,39,26,13,0,
    -13,-26,-39,-51,-64,-77,-90,10000,
    10000,-103,-116,-129,-141,-154,-167,
])

def angle2index(angle):
    AngleDiffMatrix = abs(M - angle)
    minValue = np.amin(AngleDiffMatrix)
    index = list(AngleDiffMatrix).index(minValue)
    index = str(index)
    index = index if len(index) == 2 else f"0{index}"
    return index

def callback_compass():
    index = angle2index(get_value("yaw"))
    clear_drawing("compass2")
    draw_image("compass2",f"minecraft_compass/compass/compass_{index}.png",[0,0],[h,h])

with window("Minecraft Gang", width= 600, height= 600):
    add_drawing("compass2", width= h, height= h)
    add_drag_float("yaw",min_value=-180.0,max_value=180.0)

def render():
    callback_compass()

set_render_callback(callback=render)

start_dearpygui()