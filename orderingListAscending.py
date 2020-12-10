from collections import OrderedDict
import json

def orderingListAscendingFunction(list_name, list_occurance):

    list_name_ordered = []
    list_occurance_ordered = []
    
    for x in range(0, len(list_occurance_ordered)):
        if list_occurance_ordered[x] == 0:
            list_occurance_ordered.append(list_occurance[x])
            list_name_ordered.append(list_name[x])



    return list_name_ordered, list_occurance_ordered