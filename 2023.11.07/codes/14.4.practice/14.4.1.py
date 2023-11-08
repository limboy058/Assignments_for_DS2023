import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt

from wordcloud import WordCloud

mask = np.array(Image.open(r"2023.11.07\codes\14.4.practice\stormtrooper_mask.png"))
text = open(r"2023.11.07\codes\14.4.practice\a_new_hope.txt").read()
wc = WordCloud(max_words=1000, mask=mask, margin=10,
               random_state=1).generate(text)

default_colors = wc.to_array()
plt.imshow(wc.recolor(random_state=3),
           interpolation="bilinear")
plt.axis("off")
plt.show()