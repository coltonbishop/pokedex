import os
import matplotlib.pyplot as plt 

# creating a dictionary of pokemon names and image counts 
counts = {}
for pokemon in os.listdir('balanced_data'):
    if pokemon[0] != '.':
        counts[pokemon] = len(os.listdir('balanced_data/' + pokemon))
        #print("{} : {}".format(pokemon, str(counts[pokemon])))

count_pairs = list(counts.items())
count_pairs.sort(key = lambda x: x[1])
print(count_pairs)

# plotting the number of images for each pokemon in the dataset
plt.figure(figsize=(35,7))
plt.plot(list(counts.values()))
plt.xticks(list(range(len(counts))), list(counts.keys()), rotation=90, fontsize=6)
plt.title("Number of Images for each Pokemon in New Dataset")
plt.ylabel("Number of Images")
plt.ylim((0, 300))
plt.show()
