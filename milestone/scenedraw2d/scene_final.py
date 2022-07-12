# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from textwrap import fill
from tkinter import Canvas
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random
import tkinter as tk

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500


    x0 = 250
    y0 = 50    
    x1 = x0 + 15
    y1 =  y0 + 15
    x2 = x0 + 35
    y2 = y0 + 15 
    x3 = x0 + 50
    y3 = y0

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Barad-dûr", scene_width, scene_height)
    # draw_pine_tree(canvas, 550, 150, 250)
    
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_texture(canvas)

    # half_height = round(scene_height / 2)
    # min_diam = 15
    # max_diam = 30

    # # Draw 100 circles, each with
    # # a random location and diameter.
    # for i in range(100):
    #     x = random.randint(0, 800)
    #     y = random.randint(0, 150)
    #     # diameter = random.randint(min_diam, max_diam)
    #     draw_oval(canvas, x, y, x, y, fill="gray")






    draw_mountain_1(canvas, 500, 150, 600, 250, 700, 150)
    draw_lava(canvas, 575, 225, 586, 240, 616, 240, 625, 225)
    draw_mountain_cloud(canvas, 550, 240, 650, 260)



    draw_complete_tower(canvas)
    # draw_tower(canvas, 350, 150, 400)
    # draw_arc_oval(canvas, 350, 400, 40, 50)
    # draw_background_oval(canvas, 340, 355, 360, 425)
    # draw_eye(canvas, 335, 390, 365, 405)
    # draw_pupil(canvas, 347, 390, 353, 405)
    # draw_search_light(canvas, 352, 400, 100, 150, 150, 115)

    # draw_boulder(canvas, x0, y0, x1, y1, x2, y2, x3, y3)
    # draw_boulder(canvas, 250, 50, 265, 65, 285, 65, 300, 50)



    # draw_grid(canvas, scene_width, scene_height, 50)



    draw_cloud_1(canvas, 50, 425, 200, 450)
    draw_cloud_2(canvas, 50, 425, 200, 450)
    draw_cloud_3(canvas, 50, 425, 200, 450)
    draw_cloud_4(canvas, 50, 425, 200, 450)
    
    rand_placed_birds(canvas)


    # draw_rand_clouds(canvas, scene_height, scene_width)
    # draw_rand_nasgul(canvas)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
# def draw_pine_tree(canvas, center_X, bottom, height):
#     #draw trunk
#     trunk_width = height / 10
#     trunk_height = height / 8
#     left_trunk = center_X - trunk_width / 2
#     bottom_trunk = bottom
#     right_trunk = center_X + trunk_width / 2
#     trunk_top = bottom + trunk_height
#     draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill="tan4")

#     #draw skirt/top
#     skirt_width = height / 2
#     skirt_left = center_X - skirt_width / 2 
#     skirt_bottom = trunk_top
#     peak_x = center_X
#     peak_y = bottom + height
#     skirt_right = center_X + skirt_width / 2
#     draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill="forestGreen")


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def draw_complete_tower(canvas):
    draw_tower(canvas, 350, 150, 400)
    draw_arc_oval(canvas, 350, 400, 40, 50)
    draw_background_oval(canvas, 340, 355, 360, 425)
    draw_eye(canvas, 335, 390, 365, 405)
    draw_pupil(canvas, 347, 390, 353, 405)
    draw_search_light(canvas, 352, 400, 100, 150, 150, 115)



def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="gray25")


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="gray60")

def draw_boulder(canvas, x0, y0, x1, y1, x2, y2, x3, y3):

    for i in range(4):
        x0 += 100
        # x0 = 250
        y0 += 10    
        x1 = x0 + 15
        y1 =  y0 + 15
        x2 = x0 + 35
        y2 = y0 + 15 
        x3 = x0 + 50
        y3 = y0

        draw_polygon(canvas, x0, y0, x1, y1, x2, y2, x3, y3, width=0, outline="black", fill="gray6")


def draw_rand_clouds(canvas, scene_height, scene_width):
    half_height = round(scene_height / 2)
    min_diam = 15
    max_diam = 30
    # a random location and diameter.
    for i in range(4):
        x0 = random.randint(450, 800)
        y0 = random.randint(300, 500)
        # diameter = random.randint(min_diam, max_diam)
        x1 = random.randint(450, 800)
        y1 = random.randint(300, 500)

        draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="gray40")


def draw_bird(canvas, center_x, center_y):

    x0 = center_x - 20
    y0 = center_y + 5
    x1 = center_x
    y1 = center_y - 5
    x2 = center_x + 20
    y2 = center_y + 5
    draw_arc(canvas, x0, y0, x1, y1, start=0, extent=180, width=2, outline="black", fill="", style=tk.ARC)
    draw_arc(canvas, x1, y1, x2, y2, start=0, extent=180, width=2, outline="black", fill="", style=tk.ARC)
    
def rand_placed_birds(canvas):
      for i in range(4):
        center_x = random.randint(450, 800)
        center_y = random.randint(300, 500)
        draw_bird(canvas, center_x, center_y)   
    
def draw_texture(canvas):
    for i in range(500):
        x = random.randint(0, 800)
        y = random.randint(0, 150)

        draw_polygon(canvas, x, y, x + 10, y, x + 5, y+5, width=0, fill="gray35")

    


def draw_mountain_1(canvas, x0, y0, x1, y1, x2, y2):
    draw_polygon(canvas, x0, y0, x1, y1, x2, y2, width=0, fill="gray10")

# def draw_mountain_2():
#     draw_polygon(canvas,
#         100, 100, 200, 100, 200, 150, fill="green")
#         pass
def draw_lava(canvas, x0, y0, x1, y1, x2, y2, x3, y3):
    draw_polygon(canvas, x0, y0, x1, y1, x2, y2, x3, y3, width=0, outline="red4", fill="red4")



def draw_arc_oval(canvas, center_x, center_y, width, half_height):
    x1 = center_x - width / 2
    y1 = center_y - half_height
    x2 = center_x + width / 2
    y2 = center_y + half_height
    draw_arc(canvas, x1, y1, x2, y2, start=0, extent=-180, width=0, fill="gray5")



    
def draw_cloud_1(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="gray40")

def draw_cloud_2(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="gray40")

def draw_cloud_3(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="gray40")

def draw_cloud_4(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="gray40")



def draw_mountain_cloud(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="gray40")







def draw_background_oval(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="gray60")

def draw_eye(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="firebrick3")

def draw_pupil(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="black")

def draw_search_light(canvas, x0, y0, x1, y1, x2, y2):
    draw_polygon(canvas, x0, y0, x1, y1, x2, y2, fill="gold1")

def draw_tower(canvas, center_X, bottom, height):
    #draw tower
    tower_width = height / 10
    tower_height = height / 2
    left_tower = center_X - tower_width / 2
    bottom_tower = bottom
    right_tower = center_X + tower_width / 2
    tower_top = bottom + tower_height
    draw_rectangle(canvas, left_tower, bottom_tower, right_tower, tower_top, fill="gray5")
# def draw_cloud_2(canvas, x0, y0, x1, y1):
#     draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="white")

# def draw_cloud_3(canvas, x0, y0, x1, y1):
#     draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="white")

# def draw_cloud_4(canvas, x0, y0, x1, y1):
#     draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="white")
    
# def draw_backgroundcolor_oval():
#     pass

# def draw_mountains():
#     pass


    # #draw mountain 1
    # skirt_width = height / 2
    # skirt_left = center_X - skirt_width / 2 
    # skirt_bottom = tower_top
    # peak_x = center_X
    # peak_y = bottom + height
    # skirt_right = center_X + skirt_width / 2
    # draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill="forestGreen")







# Define your functions such as
# draw_sky and draw_ground here.
def draw_grid(canvas, width, height, interval, color="black"):
    # horizontal lines
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")
        # vertical lines
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0,x,height)
        draw_text(canvas, x, label_y, f"{x}")


# Call the main function so that
# this program will start executing.
main()