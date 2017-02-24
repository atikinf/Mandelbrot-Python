import png
from PIL import Image

ESCAPE_CONSTANT = 2
ITERATE_NUM = int(input("Enter number of iterations: "))
SIZE = int(input("Enter desired image size (Between 600 and 8,000 recc.): "))
PNG_HEIGHT = SIZE
PNG_WIDTH = SIZE


image_mut = [[0 for i in range(PNG_WIDTH)] for i in range(PNG_HEIGHT)];

# generates the list for use in making an image
def genImageList():
    for row in range(len(image_mut)):
        print(str(row) + " / " + str(PNG_HEIGHT)) # progress indicator (slows towards middle)
        for col in range(len(image_mut[0])):
            comp = genCompCoord(col, row)
            check = mandelIterate(comp, ITERATE_NUM, comp)
            if check:
                image_mut[row][col] = 1

# gets a complex number appropriate for the canvas based on given coordinates
def genCompCoord(x, y):
    # scales and centeres given coordinates
    relX = (x - PNG_WIDTH // 2) / (PNG_WIDTH // 4)
    relY = (y - PNG_HEIGHT // 2) / (PNG_HEIGHT // 4)
    return complex(relX, relY)

# iterates a given number of times until escape or end
def mandelIterate(comp, num, c):
    if num == 0:
        return True
    elif abs(comp) > ESCAPE_CONSTANT:
        return False
    else:
        return mandelIterate(pow(comp, 2) + c, num - 1, c)

# [UNECESSARY] convertes a given list of lists of ints into a list of strings
# def convertToImmut(mut_list):
#     immut_list = [''.join(str(i) for i in mut_list[o]) for o in range(len(mut_list))]
#     return immut_list

def main():
    genImageList()
    image_list = image_mut
    file = open('MandelbrotTest_General.png', 'wb')
    writer = png.Writer(len(image_list[0]), len(image_list), greyscale = True, bitdepth = 1)
    writer.write(file, image_list)
    file.close()
    # displays the image 
    img = Image.open('MandelbrotTest_General.png')
    img.show()
    run_again = input("Again? Y/N: ")
    if run_again.lower().startswith("y"):
        main()
    
main()
