# adapted from https://github.com/ashrefm/multi-label-soft-f1.git

def removeRareLabels(movies):

  # Get label frequencies in descending order
  label_freq = (movies['Genre']
                .apply(lambda s: str(s).split('|'))
                .explode().value_counts().sort_values(ascending=False))

  # Create a list of rare labels
  rare = list(label_freq[label_freq<1000].index)
  print("We will be ignoring these rare labels:", rare)

  # Transform Genre into a list of labels and remove the rare ones
  movies['Genre'] = (movies['Genre']
                     .apply(lambda s: [l for l in str(s).split('|') if l not in rare]))

  return(movies)