from PIL import ImageDraw


def draw_dice(img, start_pos, end_pos, dice_num):
    if img.mode != 'L':
        raise Exception('expected grayscale image')
    img_drawer = ImageDraw.Draw(img)

    dice_w = end_pos[0] - start_pos[0]
    dice_h = end_pos[1] - start_pos[1]
    circle_diagonal = dice_w // 3  

    # draw a white rectangle
    img_drawer.rectangle([start_pos, end_pos], fill=(255,))


    r = circle_diagonal/2

    if dice_num == 1:
        # center
        x = start_pos[0] + circle_diagonal + r
        y = start_pos[1] + circle_diagonal + r
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))
    elif dice_num == 2:
        x = start_pos[0] + circle_diagonal
        y = start_pos[1] + circle_diagonal 
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))
        
        x += circle_diagonal
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))
    elif dice_num == 3:
        x = start_pos[0] + r
        y = start_pos[1] + r
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))

        x += circle_diagonal
        y += circle_diagonal
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))

        x += circle_diagonal
        y += circle_diagonal
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))
    elif dice_num == 4:
        x = start_pos[0] + circle_diagonal
        y = start_pos[1] + circle_diagonal 
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))

        x += circle_diagonal + r
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))

        y += circle_diagonal + r
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))

        x -= circle_diagonal + r
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))
    elif dice_num == 5:
        # left
        ## up
        x = start_pos[0] + r
        y = start_pos[1] + r 
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))
        ## down
        y += circle_diagonal * 2
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))

        # center
        x += circle_diagonal
        y -= circle_diagonal
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))

        # right
        ## up
        x += circle_diagonal
        y -= circle_diagonal
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))
        ## down
        y += circle_diagonal * 2
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))
    elif dice_num == 6:
        # up
        x = start_pos[0] + r
        y = start_pos[1] + r
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))

        x += circle_diagonal
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))

        x += circle_diagonal
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))

        # down
        y += circle_diagonal
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))

        x -= circle_diagonal
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))

        x -= circle_diagonal
        img_drawer.ellipse([x-r, y-r, x+r, y+r], fill=(0,))







        
        




