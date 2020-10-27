from PIL import Image
import glob
import os

# for each pokemon in the new image dataset 
pokemon_count = 1
for pokemon in os.listdir('downloads'):

    # keeping track of progress
    print("{}: {}".format(str(pokemon_count), pokemon))
    pokemon_count += 1

    # for each image file
    if pokemon[0] != '.':
        for file in os.listdir('downloads/' + pokemon):

            # if current format is PNG
            if file.endswith(".png"):

                # open and convert to JPG
                path = 'downloads/' + pokemon + '/' + file
                image = Image.open(path).convert('RGB') 

                # replace PNG with converted JPG
                image.save(path.replace("png", "jpg"))