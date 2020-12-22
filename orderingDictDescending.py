from collections import OrderedDict
import json

def orderingDictDescendingFunction(item_dict):

    item_dict_ordered = {}
    
    # ordered key
    item_dict_ordered_keys = sorted(item_dict, key=item_dict.get, reverse=True)

    for x in item_dict_ordered_keys:
        item_dict_ordered[x] = item_dict[x] 

    return item_dict_ordered