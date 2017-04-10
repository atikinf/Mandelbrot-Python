import png
from PIL import Image
# Specify the image center
# Specify the width/ height (same)
# Get the good stuff
# (a png is generated and then opened using default veiwer)

ESCAPE_CONSTANT = 2
ITERATIONS = 100
PNG_SIZE = 600
WIDTH = float(input("Enter width: "))
CENTER_X, CENTER_Y = [float(x) for x in input("Enter X and Y of center: ").split()]
print(CENTER_X, CENTER_Y)
image = [[0 for i in range(PNG_SIZE)] for i in range(PNG_SIZE)]

# Generates 2-dimensional list to store greyscale pixel data
def genImageList():
    for row in range(len(image)):
        print(str(row) + " / " + str(PNG_SIZE))
        for col in range(len(image[0])):
            comp = genCompCoord(col, row)
            if mandelIterate(comp, ITERATIONS, comp):
                image[row][col] = 1

# Note: (0, 0) in pixels is top left of image.
# Returns a complex number corresponding to given pixel coordinates.
def genCompCoord(x, y):
    realX = ((x - PNG_SIZE // 2) / PNG_SIZE * 2) * WIDTH / 2 + CENTER_X
    compY = ((y - PNG_SIZE // 2) / PNG_SIZE * 2) * WIDTH / 2 + CENTER_Y
# print(x, y, realX, compY)
    return complex(realX, compY)

# Iterates a given number of times until escape or end.
# Returns False if it escapes, otherwise returns True.
def mandelIterate(comp, num, c):
    if num == 0:
        return True
    elif abs(comp) > ESCAPE_CONSTANT:
        return False
    else:
        return mandelIterate(pow(comp, 2) + c, num - 1, c)

def main():
    genImageList() 
    file = open('MandelbrotTest_Mk2.png', 'wb')
    # Generates image file
    writer = png.Writer(len(image[0]), len(image),
                        greyscale = True, bitdepth = 1)
    writer.write(file, image)
    file.close()
    # displays the image 
    img = Image.open('MandelbrotTest_Mk2.png')
    img.show()
    
main()
