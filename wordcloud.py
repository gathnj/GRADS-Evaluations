import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from google.colab import files
import matplotlib.pyplot as plt
% matplotlib inline



uploaded = files.upload()
dataset = pd.read_excel('D.R.E.A.M. Office Public Health Workshop Feedback Form (Responses).xlsx')
print('....UPLOAD COMPLETE....')


dataset.head() #confirm data look correct

#Extract "things done well" column:
text = dataset.iloc[:,11]
text.dropna(inplace= True)
text.head()
text_unified = text.str.cat()
# Create and generate a word cloud image:
wordcloud = WordCloud().generate(text_unified)

# Display the generated image:
plt.figure( figsize=(20,10) )
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
#plt.show()
plt.savefig("word_cloud.png")
files.download("word_cloud.png")