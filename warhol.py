"""
File: warhol.py
---------------
ADD YOUR DESCRIPTION HERE
"""

# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage

# Name of file that we will use to create the warhol image
IMAGE_FILE = 'images/simba.jpg'


def green_scale():
    image = SimpleImage('images/simba.jpg')
    for pixel in image:
        pixel.red = pixel.red / 2
        pixel.green = pixel.green * 1
        pixel.blue = pixel.blue / 2
    return image


def orange_scale():
    image = SimpleImage('images/simba.jpg')
    for pixel in image:
        pixel.red = pixel.red * 3
        pixel.green = pixel.green * 1
        pixel.blue = pixel.blue / 2
    return image


def purple_scale():
    image = SimpleImage('images/simba.jpg')
    for pixel in image:
        pixel.red = pixel.red / 2
        pixel.green = pixel.green / 3
        pixel.blue = pixel.blue * 2
    return image


def red_scale():
    image = SimpleImage('images/simba.jpg')
    for pixel in image:
        pixel.red = pixel.red * 2
        pixel.green = pixel.green + 1
        pixel.blue = pixel.blue + 4
    return image


def yellow_scale():
    image = SimpleImage('images/simba.jpg')
    for pixel in image:
        pixel.red = pixel.red * 2
        pixel.green = pixel.green * 2
        pixel.blue = pixel.blue * 0
    return image


def brown_scale():
    return create_filtered_image(1 / 5, 1 / 40, 1 / 70)
    # image = SimpleImage('images/simba.jpg')
    # for pixel in image:
    #     pixel.red = pixel.red / 5
    #     pixel.green = pixel.green / 40
    #     pixel.blue = pixel.blue / 70
    # return image


def create_filtered_image(red_scale, green_scale, blue_scale):
    image = SimpleImage('images/simba.jpg')
    for pixel in image:
        pixel.red = pixel.red * red_scale
        pixel.green = pixel.green * green_scale
        pixel.blue = pixel.blue * blue_scale
    return image

    """
    Implement this function to make a patch for the Warhol program. It creates an
    image object from the image in the file IMAGE_FILE, and then recolors the image
    object.  The parameters to this function are:
      red_scale: A number to multiply each pixels' red component by
      green_scale: A number to multiply each pixels' green component by
      blue_scale: A number to multiply each pixels' blue component by
    This function should return a newly generated image with the appropriately
    scaled color values of the pixels.
    """


class Point:
    x = 0
    y = 0
    k = (860 / 2)

    def __init__(self, x, y):
        self.x = x
        self.y = y


# def insert_all_images_to_blank(array, board, point):
# def put_image(arrays):
#     for i in arrays[1]:
#         board.set_pixel(i.x, i.y, i)
#     for pixel in arrays[0]:
#         board.set_pixel(point.x + pixel.x, pixel.y, pixel)
#     for pixel in arrays[2]:
#         board.set_pixel((point.x * 2) + pixel.x, pixel.y, pixel)
#
# def put_images_to_2nd_row(array):
#     for i in array[3]:
#         board.set_pixel(i.x, point.y + i.y, i)
#     for i in array[4]:
#         board.set_pixel(i.x + point.x, point.y + i.y, i)
#     for i in array[5]:
#         board.set_pixel((point.x * 2) + i.x, i.y + point.y, i)

#     for i in array:
#         for pixel in i:
#             board.set_pixel(pixel.x + point.x, pixel.y + point.y, pixel)
#             point.x = point.x * 2
#
#         # put_image(array)
#         # put_images_to_2nd_row(array)
#     return board
#
# # -----------------------------------------------------------
# def set_image_at(background, image, point):
#      for pixel in image:
#          background.set_pixel(pixel.x + point.x, pixel.y + point.y, pixel)
#
#
# def put_image_to_background(array, background, point):
#     for index, dogImage in enumerate(array):
#         point.x = (1302 / 3) * index
#         set_image_at(background, dogImage, point)
#
#     return background
#
#
# def fill_background(firstarray, secoundarray, background):
#     startPixel = Point()
#     startPixel.x = 0
#     startPixel.y = 0
#     put_image_to_background(firstarray, background, startPixel)
#     startPixel.y = startPixel.k
#     put_image_to_background(secoundarray, background, startPixel)
#     return background
# -----------------------------------------------------------------------------
# def put_images_into_blank(array,blank,point):
#     i= "true"
#     while i == "true":
#         for image, arg in enumerate(array):
#             set_image_at(image,array)


#
def make_warhol():
    image = SimpleImage.blank(1302, 860)
    first_line = [
        green_scale(),
        orange_scale(),
        purple_scale(),
        red_scale(),
        yellow_scale(),
        brown_scale()
    ]

    # return fill_background(first_line, secound_line, image)

    for index, doimage in enumerate(first_line):

        for pixel in doimage:
            image.set_pixel(pixel.x + place_element(index).x, pixel.y + place_element(index).y, pixel)
        index = index +1
        return image


def place_element(index):
    image_width = 1302
    image_height = 860
    y = image_height / 2
    x = image_width / 3
    if index == 0:
        return Point(0, x)
    elif index == 1:
        x = x + 434
        return Point(0, x)
    elif index == 2:
        x = x * 3
        return Point(0, x)
    elif index == 3:
        return Point(y, x)
    elif index == 4:
        x = x + 434
        return Point(y, x)
    elif index == 5:
        x = x* 3
        return Point(y, x)


def main():
    """
    This program tests your create_filtered_image and make_warhol functions by calling
    those functions and displaying the resulting images.  Feel free to modify this code
    when you are writing your program.  For example, the call to the create_filtered_image
    function is provided to test that function by itself.  Feel free to delete that portion
    of the code when you have the create_filtered_image working, and then just focus on
    the make_warhol function.
    """

    #
    # single_patch = create_filtered_image(1.5, 0, 1.5)
    # if single_patch != None:
    #     single_patch.show()

    warhol_image = make_warhol()
    if warhol_image != None:
        warhol_image.show()


if __name__ == '__main__':
    main()
