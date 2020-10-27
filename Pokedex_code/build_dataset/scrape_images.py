import os
import matplotlib.pyplot as plt 
from google_images_download import google_images_download

# creating a dictionary of pokemon names and image counts 
counts = {}
for pokemon in os.listdir('data'):
    if pokemon[0] != '.':
        counts[pokemon] = len(os.listdir('data/' + pokemon))
total = len(counts)

# class instantiation of scraping library
response = google_images_download.googleimagesdownload()

# keeping track of already downloaded pokemon data
seen_dirs = os.listdir("downloads")
seen_pokemon = set()
for pokemon in seen_dirs:
    seen_pokemon.add(pokemon.replace(" pokemon", ''))

# for each pokemon class in the dataset
for num, pokemon in enumerate(counts):

    # keeping track of scraping progress
    print("({}/{}): {}".format(str(num), str(total), pokemon))

    # if the current class needs to be augmented, set an upper limit
    if counts[pokemon] < 150 and pokemon not in seen_pokemon:
        limit = 150 - counts[pokemon]

        # create search term for current pokemon
        arguments = {"keywords":pokemon, 
                    "limit":limit,
                    "suffix_keywords":"pokemon",
                    "chromedriver":"/Applications/chromedriver"}

        # downloading the necessary images
        paths = response.download(arguments)   