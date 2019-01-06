from PIL import Image, ImageOps, ImageDraw
from dice_drawer import draw_dice

number_of_dices_in_a_row = 10
img_address = 'linux.png'

# load image
img = Image.open(img_address)

# get ride of alpha channel if exists
if img.mode == 'RGBA':
    tmp = Image.new('RGB', img.size, (255, 255, 255))
    tmp.paste(img, mask=img.split()[3]) 
    img = tmp

# convert to gray scale and equalize the spectrum values
img = ImageOps.grayscale(img)
img = ImageOps.equalize(img)

img.show()

# calculate dice_size, how many pixel is a dice
dice_size = img.width // number_of_dices_in_a_row
dice_in_height = img.height // dice_size

print('dice_size', dice_size)
print('image size in dice', (number_of_dices_in_a_row, dice_in_height))
print('total dices needed', number_of_dices_in_a_row * dice_in_height)

# create the result image
# create an empty image in grayscale mode  with the size rounded to the sum of dice size
# loaded image and all pixels having white value
width = number_of_dices_in_a_row * dice_size
height = dice_in_height * dice_size
tiled_img = Image.new('L', (width, height), 255)
res_img = Image.new('L', (width, height), 255)

# initialize drawing 
draw = ImageDraw.Draw(tiled_img)

dice_map = []
for r in range(0, res_img.height, dice_size):
    for c in range(0, res_img.width, dice_size):
        avg_color = 0
        tmp_dice_row = []
        for dy in range(dice_size):
            for dx in range(dice_size):
                pos = (c+dx, r+dy)
                intensity = img.getpixel(pos)
                avg_color += intensity
        # draw tiled image
        avg_color //= dice_size ** 2
        start_pos = (c, r)
        end_pos = (c+dice_size, r+dice_size)
        draw.rectangle([start_pos, end_pos], fill=(avg_color,))
        
        # fill dice map
        # convert intensity to dice number
        dice_num = (255 - avg_color) * 6 // 255 + 1
        tmp_dice_row.append(dice_num)

        # draw dice on result image
        draw_dice(res_img, start_pos, end_pos, dice_num)

    # append a row of dice to dice map
    dice_map.append(tmp_dice_row)

        
         
tiled_img.show()
res_img.show()
tiled_img.save('tiled.jpg')
res_img.save('dice.jpg')
