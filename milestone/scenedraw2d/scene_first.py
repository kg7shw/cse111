# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from textwrap import fill
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Barad-dûr", scene_width, scene_height)
    # draw_pine_tree(canvas, 550, 150, 250)
    
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_tower(canvas, 350, 150, 400)
    
    draw_mountain_1(canvas, 500, 150, 600, 250, 700, 150)
    draw_mountain_cloud(canvas, 550, 240, 650, 260)
    draw_arc_oval(canvas, 350, 400, 40, 50)
    draw_background_oval(canvas, 340, 355, 360, 425)
    draw_eye(canvas, 335, 390, 365, 405)
    # draw_pupil(canvas, 335, 390, 365, 405)
    draw_grid(canvas, scene_width, scene_height, 50)
    # draw_cloud_1(canvas, 250, 450, 50, 400)
    

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

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="gray25")


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="gray60")

def draw_mountain_1(canvas, x0, y0, x1, y1, x2, y2):
    draw_polygon(canvas, x0, y0, x1, y1, x2, y2, fill="black")

# def draw_mountain_2():
#     draw_polygon(canvas,
#         100, 100, 200, 100, 200, 150, fill="green")
#         pass

def draw_arc_oval(canvas, center_x, center_y, width, half_height):
    x1 = center_x - width / 2
    y1 = center_y - half_height
    x2 = center_x + width / 2
    y2 = center_y + half_height
    draw_arc(canvas, x1, y1, x2, y2, start=0, extent=-180, width=0, fill="black")
    
def draw_cloud_1(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="gray40")

def draw_mountain_cloud(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="gray40")

def draw_background_oval(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="gray60")

def draw_eye(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="firebrick3")

def draw_pupil(canvas, x0, y0, x1, y1):
    draw_oval(canvas, x0, y0, x1, y1, width=0, outline="black", fill="black")



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

def draw_tower(canvas, center_X, bottom, height):
    #draw tower
    tower_width = height / 10
    tower_height = height / 2
    left_tower = center_X - tower_width / 2
    bottom_tower = bottom
    right_tower = center_X + tower_width / 2
    tower_top = bottom + tower_height
    draw_rectangle(canvas, left_tower, bottom_tower, right_tower, tower_top, fill="black")

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