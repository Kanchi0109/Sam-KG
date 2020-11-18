import json
import codecs
import more_itertools as mt

data = json.load(codecs.open('sample-json.json', 'r', 'utf-8-sig'))
counts = {}

def collapse(l):
    list(mt.collapse(l, base_type=dict))
    label = [d['tags']['label'] for d in mt.collapse(l, base_type=dict)]
    shape = [d['type'] for d in mt.collapse(l, base_type=dict)]
    for i in range(len(label)):
        key = label[i]+'_'+shape[i]
        counts[key] = counts.get(key,0) + 1
    return counts, set(shape)


for i in range(len(data)):
    counts, shape = collapse((data[i]['taggable image']))
print("Frequency of each shape and all labels associated with the shapes:\n", counts)
print("Number of unique shape types\n", shape)



