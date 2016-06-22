from nltk.corpus import wordnet as wn
all_nouns = list(wn.all_synsets('n'))
import numpy as np

# get mapping of synset id to index
id2index = {}
for i in range(len(all_nouns)):
    id2index[all_nouns[i].name()] = i
    
# get hypernym relations
hypernyms = []
for synset in all_nouns:
    for h in synset.hypernyms() + synset.instance_hypernyms():
        hypernyms.append([id2index[synset.name()], id2index[h.name()]])
hypernyms = np.array(hypernyms)

# save hypernyms
import h5py
f = h5py.File('dataset/wordnet.h5', 'w')
f.create_dataset('hypernyms', data = hypernyms)
f.close()
# save list of synset names
names = map(lambda s: s.name(), all_nouns)
import json
json.dump(names, open('dataset/synset_names.json', 'w'))
