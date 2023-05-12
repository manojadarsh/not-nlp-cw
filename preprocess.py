from utils import *
from collections import Counter


def preprocess(dataset):
    print(dataset[0:3], "")
    # load and reduce dataset
    #dataset['train'] = dataset['train'].select(list(range(0,10000)))
    #dataset['validation'] = dataset['validation'].select(list(range(0,2000)))
    #dataset['test'] = dataset['test'].select(list(range(0,2000)))
    dataset = dataset['test']
    
    #labels = dataset['train']['labels']
    #labels2 = dataset['validation']['labels']
    labels3 = dataset['labels']

    #a_labels = remove_dupes(replace_labels(labels)) # convert these to the reduced 13 labels
    #a_labels2 = remove_dupes(replace_labels(labels2))
    a_labels3 = remove_dupes(replace_labels(labels3))



    #dataset['train'] = dataset['train'].remove_columns('labels')
    #dataset['train'] = dataset['train'].add_column('labels', a_labels)
    #dataset['validation'] = dataset['validation'].remove_columns('labels')
    #dataset['validation'] = dataset['validation'].add_column('labels', a_labels2)
    dataset = dataset.remove_columns('labels')
    dataset= dataset.add_column('labels', a_labels3)

    #train = dataset["train"].to_pandas()
    #valid = dataset["validation"].to_pandas()
    test = dataset.to_pandas()
    
    dict_c = class_freq(dataset)
    class_dict = Counter(dict_c)

    a_labels3 = multilabel2multiclass(a_labels3, class_dict)

    dataset = dataset.remove_columns('labels')
    dataset = dataset.add_column('labels', a_labels3)

    test = dataset.to_pandas()

    return test




