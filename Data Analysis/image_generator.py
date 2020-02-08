# -*- coding: utf-8 -*-
#!/usr/bin/env python

# This Python script contains the Image Generator class and 
# the code for visualizing some of the training data.

          ###########################################
          ########## Author: Drew Afromsky ##########
          ####### Email: daa2162@columbia.edu #######
          ############ Date: 02/05/2020 #############

import os
import cv2
import matplotlib.pyplot as plt

class ImageGenerator:
    
    def show(self, images):

        """
        Plot the top 16 images (index 0~15) for visualization.
        :param images: images to be shown coming from the directory with the training images
        """
        
        home = '/Users/DrewAfromsky/Desktop/Projects/Behold-ai'

        fig = plt.figure(figsize=(12,12))
        fig.set_tight_layout(True)

        os.chdir(images)

        for r in range(16):
            l = images + '/train_' + str(r) + '.png'
            img = cv2.imread(l)
            ax_img = fig.add_subplot(4, 4, r+1)
            ax_img.imshow(img)
            ax_img.set_title('train_' + str(r) + '.png')
            ax_img.axis("off")

        os.chdir(home)