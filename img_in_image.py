import logging
from PIL import Image

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

img1 = Image.open('butterfly.jpg')
img2 = Image.open('butt_part.png')

size1 = w1,h1  = img1.size
size2 = w2,h2  = img2.size

pix=0,0
pix1_start = 0,0

for i in xrange(0,w1):
    if pix[0]==w1-1:
        print 'Image found!'
        break
    for j in xrange(0,h1):
        cur_pix = img1.getpixel((i,j))      
        logging.debug('Main Image: (%s,%s) - %s'% (i,j,cur_pix))
        find_pix = img2.getpixel(pix)
        logging.debug('Find Image: (%s,%s) - %s'% (pix[0],pix[1],find_pix))
        
        if cur_pix == find_pix:
            pix = pix[0],pix[1]+1
            #print pix,find_pix, i,j, cur_pix
            if pix[1]==h2:
                print '-'*80
                break
        else:
            pix=0,0

