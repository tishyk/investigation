from PIL import Image 

def new_image( ):
    size = width,height = 320, 240
    image = Image.new("RGBA", size, 'salmon')
    """
    1 -monogramm, L-greyscale,RGB, RGBA - 3 bites/pixel, CMYK - 4 b/p, I - 32 b/p
    
    black, red, salmon, #ffffff, #adef32,
    "rgb(205,100,25)", "rgb(20%,10%,25%)",
    "hsl(0,10%,25%)" - saturation,lightness, black
    """
    image.show()
    del image

def read_image(filename = 'butterfly.jpg'):
    #filename = 'butterfly.jpg'
    # or file_handle = open('butterfly.jpg')
    image = Image.open(filename,'r')
    #image.show()
    return image


    
def compare_image():   
    img1 = Image.open('butterfly.jpg')
    img2 = read_image('butterfly2.jpg')
    
    img_blended = Image.blend(img1,img2,0.5) #  same image size!!!
    img_blended.show()

    del img1, img2
    
if __name__ == '__main__':
    #new_image()
    #read_image()
    compare_image()

#im = Image.open("butterfly.jpg")
