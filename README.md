# Dicify
put dices next to each other to create an image.    
this code first quantize the image to square blocks (tiles) and calculates average color for each block. then scales the average color to numbers between 1 and 6. after that it put dices (squares which look like dice using pillow ellipse and rectangle draw functions) next together and tries to create the pattern.

## Examples
- Input image
<img src='docs/linux.png' />
- Result image with 3350 dices
<img src='docs/3350_dice.jpg />
- Result image with 120 dice
<img src='docs/120_dice.jpg />

## Dependency
- python 3
- pillow: version 5
* check <b>requirements.txt</b>
