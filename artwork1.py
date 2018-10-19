# artwork1.py
# import as function or run as standalone py file
# inputs jpg image
# manipulates the rgb values 
# and saves new jpg image

import matplotlib.pyplot as plt
import numpy as np

def artwork(filename):
    im_in = plt.imread(filename)
    im_out = np.absolute(im_in[:,:,2] - im_in[:,:,0])
    plt.imsave('art.jpg',im_out, format = 'jpg')

if __name__ == '__main__':
    filename = input('please input the filename: ')
    artwork(filename)
