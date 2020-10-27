import os

# Current working directory 
base = os.getcwd()

# Directory with imagsls
dir = 'original_data_clean/validation/'

# for each pokemon in the dataset
for pokemon in os.listdir(dir):
    if pokemon[0] != '.':

        # keep track of image number
        counter = 0

        # rename each image
        path = dir + pokemon
        for image in os.listdir(path):
            src = base + '/' + path + '/' + image
            dst = base + '/' + path + '/' "{}_{:0>3d}.jpg".(pokemon, counter)
            os.rename(src, dst)

            # update image number
            counter += 1